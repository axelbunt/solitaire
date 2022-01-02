import pygame as pg
from typing import Tuple

import app_setup
from app_setup import app_settings
from font_params import FontParams
from load_image import load_image


class Button:
    def __init__(self, x_pos: int, y_pos: int, text: str, font_params: FontParams,
                 color: Tuple[int, int, int], border: bool = True, visible: bool = True,
                 custom_btn_size_name: str = None, background_image_name: str = None,
                 *group) -> None:
        super().__init__(*group)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.visible = visible
        self.clicked = False

        self.custom_btn_size_name = custom_btn_size_name

        self.color = color
        self.border = border

        self.font = app_setup.choose_font(font_params)
        self.initial_text = text
        self.text = self.font.render(text, True, self.color)
        self.hoovered_text = self.font.render(self.initial_text, True,
                                              app_settings.background_color)
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()

        if background_image_name is not None:
            self.image = load_image(background_image_name)
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x_pos, self.y_pos)
        else:
            self.image = None
            self.rect = pg.Rect(self.x_pos - app_settings.menu_buttons_size[0] / 2,
                                self.y_pos - app_settings.menu_buttons_size[1] / 2,
                                app_settings.menu_buttons_size[0],
                                app_settings.menu_buttons_size[1])

    def draw(self, screen: pg.Surface) -> bool:
        """Draw button"""
        if not self.visible:
            return False

        if self.border and self.custom_btn_size_name is None:
            pg.draw.rect(screen, self.color,
                         (self.x_pos - app_settings.menu_buttons_size[0] // 2,
                          self.y_pos - app_settings.menu_buttons_size[1] // 2,
                          app_settings.menu_buttons_size[0],
                          app_settings.menu_buttons_size[1]),
                         2 * (0 if self.is_hovered() else 2))
        elif self.border and self.custom_btn_size_name is not None:
            if self.custom_btn_size_name == 'back_button_size':
                pg.draw.rect(screen, self.color,
                             (self.x_pos - app_settings.back_button_size[0] // 2,
                              self.y_pos - app_settings.back_button_size[1] // 2,
                              app_settings.back_button_size[0],
                              app_settings.back_button_size[1]),
                             2 * (0 if self.is_hovered() else 2))
        screen.blit(self.hoovered_text if self.is_hovered() else self.text,
                    (self.x_pos - self.text_w // 2, self.y_pos - self.text_h // 2))

        if self.image is not None:
            screen.blit(self.image, (self.rect.x, self.rect.y))

        return self.is_clicked()

    def is_hovered(self) -> bool:
        """Check if button is hovered"""
        action = False
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            action = True

        return action

    def is_clicked(self) -> bool:
        """Check if button is clicked"""
        action = False
        if self.is_hovered() and pg.mouse.get_pressed()[0] == 1 and self.clicked is False:
            self.clicked = True
            action = True
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

    def onclick(self) -> None:
        """Some function that run if button is clicked"""
        pass

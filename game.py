import card
import pygame as pg

from app_setup import app_settings
from button import Button
from card import Card, CardParams
from load_image import load_image
from typing import Optional


def draw_field(screen: pg.Surface) -> None:
    # 97 72
    color = pg.Color(255, 255, 255)
    for i in range(200, 900, 100):
        if i != 400:
            pg.draw.rect(screen, color, (i, 100, 72, 97))
        pg.draw.rect(screen, color, (i, 250, 72, 97))


def setup_cards() -> None:
    sheet = load_image('cards.png')
    rows, columns = 4, 13
    rect = pg.Rect(0, 0, sheet.get_width() // columns,
                   sheet.get_height() // rows)
    frames = []
    for j in range(rows):
        for i in range(columns):
            frame_location = (rect.w * i, rect.h * j)
            frames.append(sheet.subsurface(pg.Rect(frame_location, rect.size)))

    card_img_num = 0
    for j in range(rows):
        for i in range(columns):
            new_card = Card(10 + i * 100, 10 + j * 110 + i * 10,
                            CardParams('red' if j > 1 else 'black',
                                       str(card.list_card_values_inf[i]), str(j + 1)),
                            frames[card_img_num])
            cards.append(new_card)
            card_img_num += 1


cards = []
last_clicked_card: Optional[Card] = None
last_selected_card_num = None

pause_btn = Button(100, 60, 'Пауза', app_settings.menu_buttons_font,
                   app_settings.menu_buttons_color, custom_btn_size_name='back_button_size')

pause_menu_buttons = []
for i, btn_name in enumerate(('Продолжить', 'В главное меню'), -2):
    new_btn = Button(app_settings.window_width // 2,
                     app_settings.window_height // 2 + i * app_settings.menu_buttons_indent,
                     btn_name, app_settings.menu_buttons_font,
                     app_settings.menu_buttons_color)
    pause_menu_buttons.append(new_btn)


def switch_state_to_pause_menu() -> None:
    app_settings.game_state = 'showing pause menu'


def switch_state_to_game_running() -> None:
    app_settings.game_state = 'game running'


def switch_state_to_showing_menu() -> None:
    app_settings.game_state = 'showing menu'


pause_btn.onclick = switch_state_to_pause_menu
pause_menu_buttons[0].onclick = switch_state_to_game_running
pause_menu_buttons[1].onclick = switch_state_to_showing_menu

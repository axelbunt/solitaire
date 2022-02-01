import game
import pygame as pg

from card_params import CardParams
from typing import Optional

# todo: A: 1, 2: 2....
card_values_inf = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8,
                   '10': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
list_card_values_inf = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']


class Card:
    def __init__(self, x_pos: int, y_pos: int, card_info: CardParams,
                 image: Optional[pg.Surface]) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.card_info = card_info
        self.image = image
        self.clicked = False
        self.state = 'static'  # ready to move, turned upside down
        self.rect = pg.Rect(self.x_pos, self.y_pos, self.image.get_width(), self.image.get_height())

    def change_state(self) -> None:
        if self.state == 'turned upside down':
            self.state = 'static'
        elif self.state == 'ready to move':
            self.state = 'static'
        else:
            self.state = 'ready to move'

    def draw(self, screen: pg.Surface) -> bool:
        """Draw card"""
        if self.state != 'turned upside down':
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pg.draw.rect(screen, (255, 255, 255), self.rect, 3)
            pg.draw.rect(screen, (0, 0, 0), self.rect, 1)
            if self.state == 'ready to move':
                pg.draw.rect(screen, (0, 0, 0), self.rect, 3)
        else:
            pg.draw.rect(screen, (0, 0, 0), self.rect)

        return self.is_clicked()

    def draw_at(self, screen, x, y):
        self.rect = pg.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.draw(screen)

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
        self.change_state()
        # print(self.card_info, self.state)
        if game.last_clicked_card is None:
            game.last_clicked_card = self
        elif game.last_clicked_card != self:
            game.last_clicked_card.state = 'static'
            game.last_clicked_card = self

    def is_ace(self):
        return self.card_info.value == '1'

    def is_previous(self, other):
        return self.card_info.suit == other.card_info.suit and \
               int(self.card_info.value) - 1 == int(other.card_info.value)

    def is_king(self):
        return self.card_info.value == '13'

    def is_previous_other_color(self, other):
        return self.card_info.color != other.card_info.color and \
               int(self.card_info.value) == int(other.card_info.value) - 1

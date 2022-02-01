from dataclasses import dataclass
from typing import Tuple

from font_params import FontParams


@dataclass
class AppSettings:
    game_title: str
    game_state: str
    menu_buttons: Tuple[str, str, str, str]  # todo: add 'Статистика'
    background_color: Tuple[int, int, int]
    back_button_size: Tuple[int, int]
    menu_buttons_size: Tuple[int, int]
    menu_buttons_indent: int
    menu_buttons_color: Tuple[int, int, int]
    text_indent: int
    game_title_font: FontParams
    menu_buttons_font: FontParams
    window_size: Tuple[int, int]
    window_width: int
    window_height: int

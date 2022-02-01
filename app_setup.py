import pygame as pg

from app_settings_dataclass import AppSettings
from font_params import FontParams

pg.init()

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1100, 750

app_settings = AppSettings(game_title='Пасьянс "Косынка"',
                           game_state='showing menu',
                           menu_buttons=('Играть', 'Правила', 'О разработчиках',
                                         'Выход'),  # todo: add 'Статистика'
                           background_color=(34, 139, 34),
                           back_button_size=(130, 50),
                           menu_buttons_size=(300, 50),
                           menu_buttons_indent=70,
                           menu_buttons_color=(255, 255, 255),
                           text_indent=40,
                           game_title_font=FontParams('Arial', 80),
                           menu_buttons_font=FontParams('Arial', 35),
                           window_size=WINDOW_SIZE,
                           window_width=WINDOW_WIDTH,
                           window_height=WINDOW_HEIGHT)


# todo: 'app_font' in app_settings but not 'menu_buttons_font'
def draw_text(screen: pg.Surface, text: str, font_name: str, text_x: int, text_y: int) -> None:
    """Draw some text on screen"""
    if font_name == 'game_title_font':
        font = choose_font(app_settings.game_title_font)
    else:
        font = choose_font(app_settings.menu_buttons_font)
    text = font.render(text, True, app_settings.menu_buttons_color)
    text_x -= text.get_width() // 2
    text_y -= text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def choose_font(font_params: FontParams) -> pg.font.Font:
    try:
        return pg.font.Font(font_params.font_name, font_params.font_size)
    except FileNotFoundError:
        return pg.font.SysFont(font_params.font_name, font_params.font_size)

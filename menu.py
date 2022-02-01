import pygame as pg
import sys

from app_setup import draw_text
from app_setup import app_settings
from button import Button


def draw_game_title(screen: pg.Surface) -> None:
    """Draw game title on menu screen"""
    draw_text(screen, app_settings.game_title, 'game_title_font',
              app_settings.window_width // 2, app_settings.window_height // 2 -
              2.5 * app_settings.menu_buttons_indent)


# todo: add image for exit button and move it to top right corner
menu_buttons = []
for i, btn_name in enumerate(app_settings.menu_buttons, -1):
    new_btn = Button(app_settings.window_width // 2,
                     app_settings.window_height // 2 + i * app_settings.menu_buttons_indent,
                     btn_name, app_settings.menu_buttons_font,
                     app_settings.menu_buttons_color)
    menu_buttons.append(new_btn)

back_btn = Button(100, 70, 'Назад', app_settings.menu_buttons_font,
                  app_settings.menu_buttons_color, visible=False,
                  custom_btn_size_name='back_button_size')


def switch_state_to_showing_tmp_text() -> None:
    app_settings.game_state = 'showing in development screen'
    back_btn.visible = True


def switch_state_to_game_starting() -> None:
    app_settings.game_state = 'game starting'
    back_btn.visible = True


def switch_state_to_showing_rules() -> None:
    app_settings.game_state = 'showing rules'
    back_btn.visible = True


def switch_state_to_showing_developer() -> None:
    app_settings.game_state = 'showing developer info'
    back_btn.visible = True


def switch_state_to_showing_menu() -> None:
    app_settings.game_state = 'showing menu'
    back_btn.visible = False


def show_tmp_text(screen: pg.Surface) -> None:
    draw_text(screen, 'В разработке...', 'menu_buttons_font',
              app_settings.window_width // 2,
              app_settings.window_height // 2)


# todo: auto-wrap text
def show_rules(screen: pg.Surface) -> None:
    text_parts_to_draw = ['Цель игры — разложить все карты по мастям в порядке от туза',
                          'до короля в четыре стопки "дома" (сначала кладутся тузы,',
                          'затем двойки, тройки и так далее до короля). Играется одной',
                          'колодой в 52 карты. Карту можно перекладывать на другую',
                          'рангом выше, но другого цвета (чёрного или красного).',
                          'Карты можно сдавать из оставшейся от раздачи колоды (в',
                          'левом верхнем углу) по одной штуке. В свободную ячейку (не',
                          ' дом) можно положить только короля.',
                          'Игра заканчивается, когда все карты разложены.']
    for indent, text_part in enumerate(text_parts_to_draw, -4):
        draw_text(screen, text_part, 'menu_buttons_font', app_settings.window_width // 2,
                  app_settings.window_height // 2 + indent * app_settings.text_indent)


def show_developer_info(screen: pg.Surface) -> None:
    text_parts_to_draw = ['Разработчики: Axelbunt 54, stival06', 'Версия: v0.5']
    for indent, text_part in enumerate(text_parts_to_draw, -1):
        draw_text(screen, text_part, 'menu_buttons_font', app_settings.window_width // 2,
                  app_settings.window_height // 2 + indent * app_settings.text_indent)


def exit_app():
    pg.quit()
    sys.exit()


menu_buttons[0].onclick = switch_state_to_game_starting
menu_buttons[1].onclick = switch_state_to_showing_rules
# menu_buttons[2].onclick = switch_state_to_showing_tmp_text
menu_buttons[2].onclick = switch_state_to_showing_developer
menu_buttons[3].onclick = exit_app
back_btn.onclick = switch_state_to_showing_menu

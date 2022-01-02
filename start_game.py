import pygame as pg

from app_setup import app_settings
import menu


def start() -> None:
    screen = pg.display.set_mode(app_settings.window_size)
    pg.display.set_caption(app_settings.game_title)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill(app_settings.background_color)

        if app_settings.game_state == 'showing menu':
            menu.draw_game_title(screen)
            for button in menu.menu_buttons:
                if button.draw(screen):
                    # print(button.initial_text, 'clicked!')
                    button.onclick()
        if app_settings.game_state == 'showing in development screen':
            if menu.back_btn.draw(screen):
                menu.back_btn.onclick()
            menu.show_tmp_text(screen)
        if app_settings.game_state == 'showing rules':
            if menu.back_btn.draw(screen):
                menu.back_btn.onclick()
            menu.show_rules(screen)
        if app_settings.game_state == 'showing developer info':
            if menu.back_btn.draw(screen):
                menu.back_btn.onclick()
            menu.show_developer_info(screen)

        pg.display.flip()
    pg.quit()

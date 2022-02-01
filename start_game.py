import game
import menu
import pygame as pg
import board_info

from app_setup import app_settings


# todo: list of current buttons located on screen
def start() -> None:
    screen = pg.display.set_mode(app_settings.window_size)
    pg.display.set_caption(app_settings.game_title)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN and app_settings.game_state == 'game running':
                x, y = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
                if board.cell_coloda.rect.collidepoint((x, y)):
                    if len(board.cell_coloda.closed) != 0:
                        card = board.cell_coloda.closed[-1]
                        board.cell_coloda.openned.append(card)
                        board.cell_coloda.closed = board.cell_coloda.closed[:-1]
                    else:
                        board.cell_coloda.closed = board.cell_coloda.openned[::-1]
                        board.cell_coloda.openned = []
                    board.sost = None
                elif board.sost is None:
                    board.find_work_card()
                else:
                    board.get_cell_for_movement(x, y)

        screen.fill(app_settings.background_color)

        if app_settings.game_state == 'showing menu':
            menu.draw_game_title(screen)
            for button in menu.menu_buttons:
                if button.draw(screen):
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
        if app_settings.game_state == 'game starting':
            game.setup_cards()
            board = board_info.Boardinfo(game.cards)
            app_settings.game_state = 'game running'
        if app_settings.game_state == 'game running':
            game.draw_field(screen)
            board.draw_cards(screen)
            if game.pause_btn.draw(screen):
                game.pause_btn.onclick()
            if board.is_game_ended():
                app_settings.game_state = 'game ended'
        if app_settings.game_state == 'showing pause menu':
            for button in game.pause_menu_buttons:
                if button.draw(screen):
                    button.onclick()
        if app_settings.game_state == 'game ended':
            game.draw_field(screen)
            board.draw_cards(screen)
            game.pause_menu_buttons[1].x_pos = 100
            game.pause_menu_buttons[1].y_pos = 70
            if game.pause_menu_buttons[1].draw():
                game.pause_menu_buttons[1].onclick()

        pg.display.flip()
    pg.quit()

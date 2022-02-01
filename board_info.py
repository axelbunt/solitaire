import random
import pygame as pg

import game
from load_image import load_image


class Cell:
    def __init__(self, openned, closed, x_pos, y_pos):
        self.openned = openned
        self.closed = closed
        self.rect = pg.Rect(x_pos, y_pos, 72, 97)

    def get_clicked_card(self):
        j = len(self.openned)
        for i in range(j):
            if self.openned[j - i - 1].is_clicked():
                return j - i - 1
        return None

    def selected_for_movement(self, x, y):
        if len(self.openned) == 0:
            return self.rect.collidepoint((x, y))
        else:
            return self.openned[-1].is_clicked()

    def drop_last_card(self):
        self.openned = self.openned[:-1]
        if len(self.openned) == 0 and len(self.closed) != 0:
            self.openned.append(self.closed[-1])
            self.closed = self.closed[:-1]


class Boardinfo:
    def __init__(self, cards):
        self.back = load_image('back.png')
        cards = cards.copy()
        random.shuffle(cards)
        self.cell_coloda = Cell([], cards[:24], 200, 100)
        self.top_cells = [Cell([], [], (i + 5) * 100, 100) for i in range(4)]
        self.work_cells = [Cell([], [], (i + 2) * 100, 250) for i in range(7)]
        index = 24
        for i in range(7):
            self.work_cells[i].openned.append(cards[index])
            index += 1
            for j in range(i):
                self.work_cells[i].closed.append(cards[index])
                index += 1

        self.selected = None
        self.sost = None

    def draw_cards(self, screen):
        for i in range(7):
            cell = self.work_cells[i]
            x = 200 + 100 * i
            y = 250
            for card in cell.closed:
                screen.blit(self.back, (x, y))
                y += 15

            for card in cell.openned:
                card.draw_at(screen, x, y)
                y += 15

        for i in range(4):
            cell = self.top_cells[i]
            if len(cell.openned) != 0:
                x = 400 + 100 * (i + 1)
                y = 100

                cell.openned[-1].draw_at(screen, x, y)

        if len(self.cell_coloda.closed) != 0:
            screen.blit(self.back, (200, 100))
        if len(self.cell_coloda.openned) != 0:
            card = self.cell_coloda.openned[-1]
            card.draw_at(screen, 300, 100)

    def find_work_card(self):
        for i in range(len(self.work_cells)):
            j = self.work_cells[i].get_clicked_card()
            if j is not None:
                self.sost = 'selected'
                self.selected = (i, j)
                # self.work_cells[i].openned[j].onclick()
                # print('Selected: ', i, j)
                break

        if len(self.cell_coloda.openned) != 0:
            j = self.cell_coloda.get_clicked_card()
            if j is not None:
                self.sost = 'selected'
                self.selected = (8, j)
                # self.cell_coloda.openned[j].onclick()
                # print('Selected: ', 8, j)

        if self.selected is not None:
            # if self.selected == game.last_selected_card_num:
            #     self.selected = None
            #     self.sost = None
            #     return

            i, j = self.selected
            if self.selected[0] == 8:
                self.cell_coloda.openned[j].onclick()
            else:
                self.work_cells[i].openned[j].onclick()

            if game.last_selected_card_num != self.selected:
                game.last_selected_card_num = self.selected

    def get_cell_for_movement(self, x, y):
        if self.selected[0] == 8:
            cell_from = self.cell_coloda
        else:
            cell_from = self.work_cells[self.selected[0]]
        card = cell_from.openned[self.selected[1]]

        card.onclick()

        for i in range(len(self.top_cells)):
            if self.top_cells[i].selected_for_movement(x, y):
                cell_to = self.top_cells[i]
                if len(cell_from.openned) - 1 == self.selected[1]:
                    if len(cell_to.openned) == 0 and card.is_ace() or len(cell_to.openned) > 0 and \
                            card.is_previous(cell_to.openned[-1]):
                        cell_to.openned.append(card)
                        cell_from.drop_last_card()
                self.sost = None
                self.selected = None
                return

        for i in range(len(self.work_cells)):
            if self.work_cells[i].selected_for_movement(x, y):
                cell_to = self.work_cells[i]
                if len(cell_to.openned) == 0 and card.is_king() or len(cell_to.openned) > 0 and \
                        card.is_previous_other_color(cell_to.openned[-1]):
                    for k in range(self.selected[1], len(cell_from.openned)):
                        cell_to.openned.append(cell_from.openned[k])
                    # print(len(cell_from.openned), self.selected[1])
                    while len(cell_from.openned) > self.selected[1] + 1:
                        cell_from.drop_last_card()
                    cell_from.drop_last_card()
                self.sost = None
                self.selected = None
                return

    def is_game_ended(self) -> bool:
        for i in range(len(self.top_cells)):
            if self.top_cells[i].openned + self.top_cells[i].closed != 13:
                return False
        return True

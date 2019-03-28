import g2d
from boardgame import BoardGame
from time import time

W, H = 40, 40

class BoardGameGui:
    def __init__(self, g: BoardGame):
        self._game = g
        self._downtime = 0
        g2d.init_canvas((g.cols() * W, g.rows() * H))
        self.update_buttons()

    def main_loop(self):
        self._game.flag_at(self._game._y, self._game._x)
        self.update_buttons()
        
    def update_buttons(self):
        g2d.fill_canvas((255, 255, 255))
        rows, cols = self._game.rows(), self._game.cols()
        for y in range(1, rows):
            g2d.draw_line((0, 0, 0), (0, y * H), (cols * W, y * H))
        for x in range(1, cols):
            g2d.draw_line((0, 0, 0), (x * W, 0), (x * W, rows * H))
        for y in range(rows):
            for x in range(cols):
                g2d.draw_text_centered(self._game.get_val(x, y), (0, 0, 0),
                                       (x * W + W//2, y * H + H//2), H//2)
        g2d.update_canvas()

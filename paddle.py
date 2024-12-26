import pyxel

class Paddle:
    def __init__(self) -> None:

        self.w_layout = 120
        self.h_layout = 200

        self.x_paddle = 45
        self.y_paddle = 160

        self.w_paddle = 22
        self.h_paddle = 10

        self.dx = 3

    def update(self):
        # always ensure that the mouse is within layout before moving
        if pyxel.mouse_x > self.w_paddle / 2 + self.x_paddle and (0 < pyxel.mouse_y <= self.h_layout):
            self.x_paddle += self.dx

        if pyxel.mouse_x < self.w_paddle / 2 + self.x_paddle and (0 < pyxel.mouse_y <= self.h_layout):
            self.x_paddle -= self.dx

        # horizontal border
        self.x_paddle = max(0, min(self.x_paddle, pyxel.width - self.w_paddle))

    def draw(self):
        pyxel.blt(self.x_paddle, self.y_paddle, 0, 0, 136, self.w_paddle, self.h_paddle, 0)
        # pyxel.blt(self.x_paddle, self.y_paddle, 0, 24, 136, self.w_paddle, self.h_paddle, 0)
        if (0 < pyxel.mouse_x <= self.w_layout) and (0 < pyxel.mouse_y <= self.h_layout):
            pyxel.text(5, 190, f'x: {pyxel.mouse_x}', pyxel.COLOR_BLACK, None)
            # pyxel.text(5, 190, f'x: {pyxel.mouse_x}', pyxel.COLOR_WHITE, None)

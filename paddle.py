import pyxel

class Paddle:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200

        self.x_paddle = 45
        self.y_paddle = 160

        self.w_paddle = 30
        self.h_paddle = 5

        self.dx = 2

    def update(self):
        # always ensure that the mouse is within layout before moving
        if pyxel.mouse_x > (self.w_layout/2) and (0 < pyxel.mouse_x <= self.w_layout):
            self.x_paddle += self.dx
        elif pyxel.mouse_x < (self.w_layout/2) and (0 < pyxel.mouse_x <= self.w_layout):
            self.x_paddle -= self.dx

        # horizontal border
        self.x_paddle = max(0, min(self.x_paddle, pyxel.width - self.w_paddle))

    def draw(self):
        pyxel.rect(self.x_paddle, self.y_paddle, self.w_paddle, self.h_paddle, pyxel.COLOR_GREEN)
        pyxel.text(5, 190, f'x: {self.x_paddle}', pyxel.COLOR_WHITE, None)

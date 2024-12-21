import pyxel

class Breakout:
    def __init__(self):
        self.w_layout = 135
        self.h_layout = 190

        self.x_ball = 67.5
        self.y_ball = 125

        self.x_paddle = 52.5
        self.y_paddle = 145

        pyxel.init(self.w_layout, self.h_layout)
        pyxel.run(self.update, self.draw)

    def update(self):
        ...

    def draw(self):
        pyxel.cls(0)
        ball = pyxel.circ(self.x_ball, self.y_ball, 2, pyxel.COLOR_DARK_BLUE)
        paddle = pyxel.rect(self.x_paddle, self.y_paddle, 30, 5, pyxel.COLOR_GREEN)

Breakout()

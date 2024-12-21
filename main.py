import pyxel

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200

        self.x_ball = 60
        self.y_ball = 145

        self.r_ball = 3

        self.x_paddle = 45
        self.y_paddle = 165

        self.w_paddle = 30
        self.h_paddle = 5

        pyxel.init(self.w_layout, self.h_layout)
        pyxel.run(self.update, self.draw)

    def update(self):
        ...

    def draw(self):
        pyxel.cls(0)
        ball = pyxel.circ(self.x_ball, self.y_ball, self.r_ball, pyxel.COLOR_DARK_BLUE)
        paddle = pyxel.rect(self.x_paddle, self.y_paddle, self.w_paddle, self.h_paddle, pyxel.COLOR_GREEN)

Breakout()

import pyxel
from paddle import Paddle

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200

        self.x_ball = 60
        self.y_ball = 145

        self.r_ball = 2

        self.paddle = Paddle()

        pyxel.init(self.w_layout, self.h_layout)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.paddle.update()

    def draw(self):
        pyxel.cls(0)
        self.paddle.draw()
        
        ball = pyxel.circ(self.x_ball, self.y_ball, self.r_ball, pyxel.COLOR_DARK_BLUE)

Breakout()

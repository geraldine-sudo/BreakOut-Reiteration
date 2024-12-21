import pyxel
from paddle import Paddle
from ball import Ball

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200
        self.ball = Ball()
        self.paddle = Paddle()

        pyxel.init(self.w_layout, self.h_layout, title='Breakout')

        pyxel.run(self.update, self.draw)

    def update(self):
        self.paddle.update()

    def draw(self):
        pyxel.cls(0)
        self.paddle.draw()
        self.ball.draw()
        
        pyxel.mouse(visible=True)
        
Breakout()

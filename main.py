
import pyxel
from paddle import Paddle
from ball import Ball

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200

        self.paddle = Paddle()
        self.ball = Ball(self.w_layout//2, self.paddle.y_paddle-4)

        pyxel.init(self.w_layout, self.h_layout, title='Breakout')

        pyxel.run(self.update, self.draw)

    def update(self):
        self.paddle.update()
        self.ball.update(self.paddle.x_paddle, self.paddle.w_paddle)

    def draw(self):
        pyxel.cls(0)
        self.paddle.draw()
        self.ball.draw()
        
        pyxel.mouse(visible=True)
        
        
Breakout()

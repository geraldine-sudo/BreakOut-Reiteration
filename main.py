
import pyxel
from paddle import Paddle
from ball import Ball
from bricks import Bricks

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200

        pyxel.init(self.w_layout, self.h_layout, title='Breakout')

        self.paddle = Paddle()
        self.ball = Ball(self.w_layout//2, self.paddle.y_paddle-4)
        self.bricks = Bricks()

        pyxel.load('paddle.pyxres')

        pyxel.run(self.update, self.draw)

    def update(self):
        self.paddle.update()
        self.ball.update(self.paddle.x_paddle, self.paddle.w_paddle)

    def draw(self):
        pyxel.cls(0)
        self.bricks.draw()
        self.paddle.draw()
        self.ball.draw()

        # hardcoded lives display
        pyxel.blt(105, 187, 2, 0, 0, 8, 8)
        pyxel.blt(95, 187, 2, 0, 0, 8, 8)
        pyxel.blt(85, 187, 2, 0, 0, 8, 8)

        # hardcoded bricks
        pyxel.blt(5, 35, 0, 16, 0, 8, 16)
        pyxel.blt(15, 55, 0, 32, 0, 8, 16)

        pyxel.blt(25, 75, 0, 24, 0, 8, 16)

        pyxel.blt(100, 75, 0, 32, 0, 8, 16)

        pyxel.blt(105, 20, 0, 40, 0, 8, 16)
        pyxel.blt(95, 45, 0, 16, 0, 8, 16)
        

        pyxel.mouse(visible=True)

        
Breakout()

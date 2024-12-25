
import pyxel
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from stage3map import Stage3Map

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200

        pyxel.init(self.w_layout, self.h_layout, title='Breakout')

        self.paddle = Paddle()
        self.ball = Ball(self.w_layout//2, self.paddle.y_paddle-3, self.paddle.w_paddle, self.paddle.h_paddle)
        
        pyxel.load('assets.pyxres')

        self.stage3map = Stage3Map()

        # brick testing
        self.bricks = [Bricks(60, 55, '1')]

        pyxel.run(self.update, self.draw)

    def update(self):
        self.paddle.update()
        self.ball.update(self.paddle.x_paddle)

    def draw(self):

        # # iterate over list of bricks
        # for i in self.bricks:
        #     i.draw()

        pyxel.cls(0)
        self.stage3map.draw()

        self.paddle.draw()
        self.ball.draw()

        # hardcoded lives display

        pyxel.blt(100, 180, 0, 0, 120, 16, 16, 0)
        pyxel.blt(85, 180, 0, 0, 120, 16, 16, 0)
        pyxel.blt(70, 180, 0, 0, 120, 16, 16, 0)
        
        # pyxel.blt(105, 187, 0, 0, 16, 8, 8, 0)
        # pyxel.blt(95, 187, 0, 0, 16, 8, 8, 0)
        # pyxel.blt(85, 187, 0, 0, 16, 8, 8, 0)
        
        pyxel.mouse(visible=True)

        
Breakout()

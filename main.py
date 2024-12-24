
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
        self.ball = Ball(self.w_layout//2, self.paddle.y_paddle-3, self.paddle.w_paddle)
        
        pyxel.load('assets.pyxres')

        # brick testing
        self.bricks = [Bricks(60, 55, '1')]

        pyxel.run(self.update, self.draw)

    def update(self):
        self.paddle.update()
        self.ball.update(self.paddle.x_paddle)

    def draw(self):
        pyxel.cls(0)

        # cosmetics
        for i in range(0, 160, 15):
            pyxel.line(0, 0, pyxel.width, i, pyxel.COLOR_WHITE)
        for i in range(0, 160, 15):
            pyxel.line(pyxel.width, 0, 0, i, pyxel.COLOR_WHITE)

        # iterate over list of bricks
        for i in self.bricks:
            i.draw()

        self.paddle.draw()
        self.ball.draw()

        # hardcoded lives display
        pyxel.blt(105, 187, 0, 0, 16, 8, 8)
        pyxel.blt(95, 187, 0, 0, 16, 8, 8)
        pyxel.blt(85, 187, 0, 0, 16, 8, 8)
        
        pyxel.mouse(visible=True)

        
Breakout()

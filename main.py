
import pyxel
from paddle import Paddle
from ball import Ball
from bricks import check_levels, load_level
from stages import Stage1Map, Stage2Map, Stage3Map

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200

        pyxel.init(self.w_layout, self.h_layout, title='Breakout')

        self.paddle = Paddle()
        self.ball = Ball(self.w_layout//2, self.paddle.y_paddle-3, self.paddle.w_paddle, self.paddle.h_paddle)
        
        pyxel.load('assets.pyxres')

        self.stagemaps = ['stage1', 'stage2', 'stage3']
        self.stage_x = 0

        self.levels = check_levels()

        self.curlevel = self.stagemaps[self.stage_x]

        self.bricks = None

        self.load_new_game()

        pyxel.run(self.update, self.draw)

    def load_new_game(self):
        self.stage_x = 0
        self.curlevel = self.stagemaps[self.stage_x]

        self.bricks = load_level(self.curlevel) 

        # set starting point here
        # set game status here

    def load_next_level(self):
        self.stage_x += 1
        self.curlevel = self.stagemaps[self.stage_x]

        self.bricks = load_level(self.curlevel) 


    def update(self):
        self.paddle.update()
        self.ball.update(self.paddle.x_paddle)

    def draw(self):
        pyxel.cls(0)
        if self.curlevel == 'stage1':
            Stage1Map().draw()
            
            pyxel.blt(105, 187, 0, 0, 16, 8, 8, 0)
            pyxel.blt(95, 187, 0, 0, 16, 8, 8, 0)
            pyxel.blt(85, 187, 0, 0, 16, 8, 8, 0)

        elif self.curlevel == 'stage2':
            Stage2Map().draw()

            pyxel.blt(105, 187, 0, 0, 16, 8, 8, 0)
            pyxel.blt(95, 187, 0, 0, 16, 8, 8, 0)
            pyxel.blt(85, 187, 0, 0, 16, 8, 8, 0)

        elif self.curlevel == 'stage3':
            Stage3Map().draw()

            pyxel.blt(100, 180, 0, 0, 120, 16, 16, 0)
            pyxel.blt(85, 180, 0, 0, 120, 16, 16, 0)
            pyxel.blt(70, 180, 0, 0, 120, 16, 16, 0)
            
        self.paddle.draw()
        self.ball.draw()

        for brick in self.bricks:
            brick.draw()
        
        pyxel.mouse(visible=True)

        
Breakout()

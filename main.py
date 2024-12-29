
import pyxel
from paddle import Paddle
from ball import Ball
from bricks import load_level
from stages import Stage1Map, Stage2Map, Stage3Map

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200
        self.ball_diameter = 7
        self.launch = False

        pyxel.init(self.w_layout, self.h_layout, title='Breakout')

        self.paddle = Paddle()

        
        pyxel.load('assets.pyxres')

        self.stagemaps = ['stage1', 'stage2', 'stage3']
        self.stage_x = 0

        self.curlevel = self.stagemaps[self.stage_x]

        self.bricks = None
        self.lives = 3
        self.lives_display = None

        self.load_restart()

        self.ball = Ball(self.w_layout//2 -self.ball_diameter//2, self.paddle.y_paddle - self.ball_diameter,self.paddle ,self.bricks, self.lives, self.launch)

        pyxel.run(self.update, self.draw)

    def load_restart(self):
        self.stage_x = 0
        self.curlevel = self.stagemaps[self.stage_x]

        self.bricks, self.lives_display = load_level(self.curlevel, self.lives) 

        # set starting point here
        # set game status here

    def load_next_level(self):
        self.stage_x += 1
        self.curlevel = self.stagemaps[self.stage_x]

        self.bricks = load_level(self.curlevel) 

    def update(self):
        self.paddle.update()
        self.ball.update()
        for b in self.bricks:
            b.update()

    def draw(self):
        pyxel.cls(0)
        if self.curlevel == 'stage1':
            Stage1Map().draw()
        
        elif self.curlevel == 'stage2':
            Stage2Map().draw()

        elif self.curlevel == 'stage3':
            Stage3Map().draw()
            
        self.paddle.draw()
        self.ball.draw()

        for brick in self.bricks:
            if brick.alive:
                brick.draw()

        for i in self.lives_display:
            i.draw()

        
        pyxel.mouse(visible=True)

        
Breakout()

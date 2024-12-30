
import pyxel
from paddle import Paddle
from ball import Ball
from bricks import load_level
from stages import Stage1Map, Stage2Map, Stage3Map
from game_progression import GameOver, NextStage1_2
from time import sleep

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
        self.lenbricks = None
        self.lives = None
        self.lives_display = None

        self.flag_brick_collide = False
        self.loading_next_level = False

        self.gamestate = 'playing'

        self.load_restart()

        self.ball = Ball(self,self.w_layout//2 -self.ball_diameter//2, self.paddle.y_paddle - self.ball_diameter,self.paddle ,self.bricks, self.lives, self.launch)

        pyxel.run(self.update, self.draw)

    def load_restart(self):
        self.stage_x = 0
        self.lives = 3

        self.curlevel = self.stagemaps[self.stage_x]

        self.bricks, self.lives_display = load_level(self.curlevel, self.lives) 
        self.lenbricks = len(self.bricks)
        # self.lenbricks = 1

    def load_next_level(self):
        self.stage_x += 1
        self.curlevel = self.stagemaps[self.stage_x]

        self.bricks, self.lives_display = load_level(self.curlevel, self.lives) 

    def update(self):
        if self.lives > self.ball.update_lives():
            self.lives -= 1
            self.lives_display.pop()
            self.ball = Ball(self, self.w_layout // 2 - self.ball_diameter // 2, self.paddle.y_paddle - self.ball_diameter, self.paddle, self.bricks, self.lives, self.launch)

        self.paddle.update()
        self.ball.update()
        for b in self.bricks:
            b.update()

        if self.ball.is_brick_colliding() and not self.flag_brick_collide:
            self.lenbricks -= 1
            self.flag_brick_collide = True

        elif not self.ball.is_brick_colliding():
            self.flag_brick_collide = False

        if self.lenbricks == 0 and not self.loading_next_level:
            self.flag_brick_collide = False
            self.gamestate = 'loading next level'
            self.lenbricks = len(self.bricks)
            self.load_next_level()
            
        if self.lives == 0:
            self.gamestate = 'gameover'

        if pyxel.btnp(pyxel.KEY_SPACE) and self.gamestate == 'gameover':
            self.load_restart()
            self.gamestate = 'playing'
    
    def draw(self):
        pyxel.cls(0)

        if self.curlevel == 'stage1' and self.gamestate == 'playing':
            Stage1Map().draw()
        
        elif self.curlevel == 'stage2' and self.gamestate == 'playing':
            Stage2Map().draw()

        elif self.curlevel == 'stage3' and self.gamestate == 'playing':
            Stage3Map().draw()
            
        self.ball.draw()
        self.paddle.draw()

        for brick in self.bricks:
            if brick.alive:
                brick.draw()

        for i in self.lives_display:
            i.draw()

        if self.gamestate == 'gameover':
            GameOver().draw()
            self.paddle.launch = False
                    
        if self.gamestate == 'loading next level':
            NextStage1_2().draw()
            pyxel.flip()  
            sleep(1)
            self.gamestate = 'playing'
            self.paddle.launch = False

        
        pyxel.mouse(visible=True)

        
Breakout()

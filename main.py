import pyxel
from paddle import Paddle
from ball import Ball
from bricks import load_level
from stages import Stage1Map, Stage2Map, Stage3Map
from game_progression import GameOver, NextStage1_2
from time import sleep
from score_object import Score_Object
from random import randint

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200
        self.ball_diameter = 7
        self.launch = False
        self.score_object: list[Score_Object] = []
        self.score = 0

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
        self.ball = Ball(
            self,
            self.w_layout // 2 - self.ball_diameter // 2,
            self.paddle.y_paddle - self.ball_diameter,
            self.paddle,
            self.bricks,
            self.lives,
            self.launch
        )


        pyxel.run(self.update, self.draw)

    def load_restart(self):
        self.score_object.clear()
        self.score = 0
        self.stage_x = 0
        self.lives = 3
        self.flag_brick_collide = False
        self.loading_next_level = False
        self.gamestate = 'playing'


        # Reload the current level and initialize fresh bricks
        self.curlevel = self.stagemaps[self.stage_x]
        self.bricks, self.lives_display = load_level(self.curlevel, self.lives)

        self.paddle = Paddle()

        # Reset brick states
        self.lenbricks = len(self.bricks)
        # self.lenbricks = 1

        # Reinitialize the Ball with the updated bricks
        self.ball = Ball(
            self,
            self.w_layout // 2 - self.ball_diameter // 2,
            self.paddle.y_paddle - self.ball_diameter,
            self.paddle,
            self.bricks,
            self.lives,
            self.launch
        )

    def load_next_level(self):
        self.stage_x += 1
        self.curlevel = self.stagemaps[self.stage_x]
        self.bricks, self.lives_display = load_level(self.curlevel, self.lives)
        self.paddle = Paddle()
        self.ball = Ball(
            self,
            self.w_layout // 2 - self.ball_diameter // 2,
            self.paddle.y_paddle - self.ball_diameter,
            self.paddle,
            self.bricks,
            self.lives,
            self.launch
        )

    def update(self):
        if self.ball.to_update_lives():
            self.lives -= 1
            self.lives_display.pop()
            self.paddle = Paddle()
            self.ball = Ball(
                self,
                self.w_layout // 2 - self.ball_diameter // 2,
                self.paddle.y_paddle - self.ball_diameter,
                self.paddle,
                self.bricks,
                self.lives,
                self.launch
            )
        
        self.paddle.update()
        self.ball.update()

        for i in range(len(self.score_object) - 1, -1, -1):  # Iterate backwards

            s = self.score_object[i]
            print(s.alive)
            if s.acquired:
                self.score += s.points
                self.score_object.pop(i)  # Remove directly by index

            elif not s.alive:
                self.score_object.pop(i)  # Remove directly by index

            else:
                s.update()

        for b in self.bricks:
            if b.hit and b.hits == 1:

                for _ in range(2):
                    self.score_object.append(Score_Object(randint(b.x + 1, b.x - 1 + b.w), randint(b.y + 1, b.y - 1 + b.h), b.score, self.paddle ))
            b.update()


        if self.lenbricks == 0 and not self.loading_next_level and len(self.score_object) == 0:
            self.gamestate = 'loading next level'
            self.loading_next_level = True
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
            elif not brick.counted:
                self.lenbricks -= 1
                brick.counted = True

        for s in self.score_object:
            s.draw()

        for i in self.lives_display:
            i.draw()

        if self.gamestate == 'gameover':
            GameOver().draw()
                    
        if self.gamestate == 'loading next level':
            NextStage1_2().draw()
            pyxel.flip()  
            sleep(1)
            self.gamestate = 'playing'

        
        pyxel.mouse(visible=True)

        
Breakout()

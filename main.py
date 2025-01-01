import pyxel
from paddle import Paddle
from ball import Ball
from bricks import load_level
from stages import Stage1Map, Stage2Map, Stage3Map
from game_progression import GameOver, NextStage1_2, NextStage2_3, Win, Start, Pregame
from time import sleep
from score_object import Score_Object
from random import randint
import math

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200
        self.ball_diameter = 7
        self.launch = False
        self.score_object: list[Score_Object] = []
        self.G = 3 # need to make it configurable
        self.K = 2
        self.Q = 10  # need to make it configurable
        self.X = 20 # need to make configurable
        self.score = 0
        self.streak = 0

        pyxel.init(self.w_layout, self.h_layout, title='Breakout')

        self.paddle = Paddle()
        pyxel.load('assets.pyxres')

        self.stagemaps = ['stage1', 'stage2', 'stage3']
        self.stage_x = 0

        self.curlevel = self.stagemaps[self.stage_x]
        self.bricks: list[Brick] = []
        self.lenbricks = None
        self.lives = 3
        self.lives_display = None

        self.flag_brick_collide = False
        self.loading_next_level = False
        self.gamestate = None

        self.launch_game()

        self.balls = [Ball(
            self.w_layout // 2 - self.ball_diameter // 2,
            self.paddle.y_paddle - self.ball_diameter,
            self.paddle, self.G,
            self.bricks,
            self.lives,
            self.launch
        )]
        pyxel.run(self.update, self.draw)

    def launch_game(self):
        self.gamestate = 'starting'

    def load_restart(self):
        self.streak = 0
        self.score_object.clear()
        self.score = 0
        self.stage_x = 0
        self.lives = 3
        self.flag_brick_collide = False
        self.loading_next_level = False
        self.gamestate = 'playing level 1'


        # Reload the current level and initialize fresh bricks
        self.curlevel = self.stagemaps[self.stage_x]
        self.bricks, self.lives_display = load_level(self.curlevel, self.lives)

        self.paddle = Paddle()

        # Reset brick states
        #self.lenbricks = len(self.bricks)
        self.lenbricks = 1

        self.balls: list[Ball] = [Ball(
            self.w_layout // 2 - self.ball_diameter // 2,
            self.paddle.y_paddle - self.ball_diameter,
            self.paddle, self.G,
            self.bricks,
            self.lives,
            self.launch
        )]

        # Reinitialize the Ball with the updated bricks

    def load_next_level(self):
        self.streak = 0
        self.stage_x += 1
        self.curlevel = self.stagemaps[self.stage_x]
        self.bricks, self.lives_display = load_level(self.curlevel, self.lives)
        self.lenbricks = len(self.bricks)
        
        self.paddle = Paddle()
        self.balls = [Ball(
                self.w_layout // 2 - self.ball_diameter // 2,
                self.paddle.y_paddle - self.ball_diameter,
                self.paddle, self.G,
                self.bricks,
                self.lives,
                self.launch
            )]
        
    def update(self):

        if pyxel.btnp(pyxel.KEY_A) and self.gamestate == 'starting':
            self.gamestate = 'loading level 1'

        not_alive = all(not ball.alive for ball in self.balls)

        if not_alive and self.lives >= 0:
            self.streak = 0
            self.lives -= 1
            self.lives_display.pop()
            self.paddle = Paddle()
            self.balls = [Ball(
                self.w_layout // 2 - self.ball_diameter // 2,
                self.paddle.y_paddle - self.ball_diameter,
                self.paddle,self.G,
                self.bricks,
                self.lives,
                self.launch
            )]

        self.paddle.update()
        for ball in self.balls:
            ball.update()

        for i in range(len(self.score_object) - 1, -1, -1):  # Iterate backwards

            s = self.score_object[i]
            print(s.alive)
            if s.acquired:
                self.streak += 1
                self.score += s.points + self.Q*self.streak
                self.score_object.pop(i)  # Remove directly by index

            elif not s.alive:
                self.streak = 0
                self.score_object.pop(i)  # Remove directly by index

            else:
                s.update()

        for b in self.bricks:
            if b.hit and b.hits == 1:

                if b.brick_level == "5":
                    ball = Ball(b.x + 5, b.y + 3, self.paddle, self.G, self.bricks, self. lives, True)
                    ball.active = False
                    ball.degree = randint(190, 350) 
                    ball.angle = math.radians(ball.degree)
                    ball.trig_multiplier()
                    v = randint(-210, -179)
                    ball.vx = -v*ball.cos_angle
                    ball.vy = v*ball.sin_angle

                    self.balls.append(ball)

                else:


                    for _ in range(2):
                        self.score_object.append(Score_Object(randint(b.x + 1, b.x - 1 + b.w), randint(b.y + 1, b.y - 1 + b.h), b.score, self.paddle ))
            b.update()

        print(self.lenbricks, len(self.score_object))

        if self.lenbricks == 0 and not self.loading_next_level and self.gamestate == 'playing level 1':
            self.gamestate = 'loading level 2'
            self.loading_next_level = True
            self.load_next_level()

        if self.lenbricks == 0 and not self.loading_next_level and self.gamestate == 'playing level 2':
            self.gamestate = 'loading level 3'
            self.loading_next_level = True
            self.load_next_level()

        if self.lives == 0:
            self.gamestate = 'gameover'

        if pyxel.btnp(pyxel.KEY_SPACE) and (self.gamestate == 'gameover' or self.gamestate == 'win'):
            self.load_restart()
            self.gamestate = 'playing level 1'


    
    def draw(self):
        pyxel.cls(0)

        if self.gamestate == 'starting':
            Start().draw()

        if self.curlevel == 'stage1' and self.gamestate == 'playing level 1':
            Stage1Map().draw()
        
        elif self.curlevel == 'stage2' and self.gamestate == 'playing level 2':
            Stage2Map().draw()

        elif self.curlevel == 'stage3' and self.gamestate == 'playing level 3':
            Stage3Map().draw()
            
        if self.gamestate == 'playing level 1' or self.gamestate == 'playing level 2' or self.gamestate == 'playing level 3':
            for b in self.balls:
                b.draw()
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
        
        #####
        pyxel.mouse(visible=True)

        if self.gamestate == 'loading level 1':
            Pregame().draw()
            pyxel.flip()  
            sleep(1)
            self.load_restart()

        if self.gamestate == 'loading level 2':
            NextStage1_2().draw()
            pyxel.flip()  
            sleep(1)
            self.gamestate = 'playing'

        
        pyxel.mouse(visible=True)

        
Breakout()

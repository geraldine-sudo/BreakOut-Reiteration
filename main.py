import pyxel
from paddle import Paddle
from ball import Ball
from bricks import Bricks, access_json
from stages import Stage1Map, Stage2Map, Stage3Map
from game_progression import GameOver, NextStage1_2, NextStage2_3, Win, Start, Pregame
from time import sleep
from score_object import Score_Object, Streak_Score, Powerup_Text
from random import randint
import math
import json

def load_level(level: str, lives: int):
    this_level = []
    lives_display = []

    possible_bricks = ["1", "2", "3", "4", "5"]

    with open('stages.json', 'r') as f:
        stage = json.load(f)

        y = 0
        for i in stage[level]['brick_placement']:
            x = 16 * (len(i) - 1)  # Start from the rightmost column
            for j in reversed(i):  # Iterate over the row in reverse
                if j in possible_bricks:
                    this_level.append(Bricks(x, y, j))
                elif (j == '6' or j == '7') and len(lives_display) < lives:
                    lives_display.append(Bricks(x, y, j))
                x -= 16  # Move to the left for the next brick
            y += 16  # Move to the next row
    return this_level, lives_display

def configs(curstage):
    stages = access_json('stages')
    return (stages[curstage]['G'], stages[curstage]['Qtty_scoreObjects'], stages[curstage]['Q'], stages[curstage]['X'],  stages[curstage]['Points'])

class Breakout:
    def __init__(self):
        self.w_layout = 120
        self.h_layout = 200
        self.ball_diameter = 7
        self.launch = False
        self.score_object: list[Score_Object] = []
        self.powerup_text: list[Powerup_Text] = []

        # self.G = 3 # need to make it configurable
        # self.K = 2
        # self.Q = 10  # need to make it configurable
        # self.X = 20 # need to make configurable

        # score
        self.streak_score: list[Streak_Score]= []
        self.score = 0
        self.streak = 0

        #powerups
        self.extra_lives = 0
        self.anti_gravity = False
        self.extend_paddle = False
        self.t_anti_gravity = 0
        self.t_extend_paddle = 0
        
        pyxel.init(self.w_layout, self.h_layout, title='Breakout')

        self.paddle = Paddle(self)
        pyxel.load('assets.pyxres')

        self.stagemaps = ['stage1', 'stage2', 'stage3']
        self.stage_x = 0

        self.curlevel = self.stagemaps[self.stage_x]

        # need to add P as configurable
        self.G, self.K, self.Q, self.X, self.P = (configs(self.curlevel))

        self.bricks: list[Bricks] = []
        self.lenbricks = None
        self.lives = 3
        self.lives_display = None

        self.flag_brick_collide = False
        self.loading_next_level = False
        self.gamestate = None

        self.launch_game()

        self.balls = [Ball(self,
            self.w_layout // 2 - self.ball_diameter // 2,
            self.paddle.y_paddle - self.ball_diameter,
            self.paddle, self.G,
            self.bricks,
            self.launch
        )]
        pyxel.run(self.update, self.draw)

    def launch_game(self):
        self.gamestate = 'starting'

    def load_restart(self):
        self.powerup_text.clear()
        self.anti_gravity = False
        self.t_anti_gravity = 0
        self.extend_paddle = False
        self.t_extend_paddle = 0
        self.streak = 0
        self.score_object.clear()
        self.streak_score.clear()
        self.score = 0
        self.stage_x = 0
        self.lives = 3
        self.flag_brick_collide = False
        self.loading_next_level = False
        self.gamestate = 'playing level 1'

        # Reload the current level and initialize fresh bricks
        self.curlevel = self.stagemaps[self.stage_x]
        self.bricks, self.lives_display = load_level(self.curlevel, self.lives)

        self.paddle = Paddle(self)

        # Reset brick states
        self.lenbricks = sum(1 for brick in self.bricks if brick.brick_level != "4")
        # self.lenbricks = 1

        self.balls: list[Ball] = [Ball(self,
            self.w_layout // 2 - self.ball_diameter // 2,
            self.paddle.y_paddle - self.ball_diameter,
            self.paddle, self.G,
            self.bricks,
            self.launch
        )]
        # Reinitialize the Ball with the updated bricks

    def load_next_level(self):
        self.powerup_text.clear()
        self.loading_next_level = False
        self.extend_paddle = False
        self.t_extend_paddle = 0
        self.anti_gravity = False
        self.t_anti_gravity = 0
        self.streak = 0
        self.stage_x += 1
        self.curlevel = self.stagemaps[self.stage_x]
        self.streak_score.clear()
        self.bricks, self.lives_display = load_level(self.curlevel, self.lives)
        self.lenbricks = sum(1 for brick in self.bricks if brick.brick_level != "4")
        
        self.paddle = Paddle(self)
        self.balls = [Ball(self,
                self.w_layout // 2 - self.ball_diameter // 2,
                self.paddle.y_paddle - self.ball_diameter,
                self.paddle, self.G,
                self.bricks,
                self.launch
            )]
        
    def update(self):
        self.G, self.K, self.Q, self.X, self.P = (configs(self.curlevel))

        # print(self.G, self.K, self.Q, self.X, self.P)

        if pyxel.btnp(pyxel.KEY_A) and self.gamestate == 'starting':
            self.gamestate = 'loading level 1'

        if self.gamestate[0] == "p":


            if self.extend_paddle:
                self.t_extend_paddle -= 1
                if self.t_extend_paddle < 0:
                    self.extend_paddle = False

            if self.anti_gravity:
                self.t_anti_gravity -= 1
                if self.t_anti_gravity < 0:
                    self.anti_gravity= False

            not_alive = all(not ball.alive for ball in self.balls)

            if not_alive and self.lives >= 0:
                self.powerup_text.clear()
                self.anti_gravity = False
                self.t_anti_gravity = 0
                self.extend_paddle = False
                self.t_extend_paddle = 0
                self.streak = 0
                self.lives -= 1
                self.lives_display.pop()
                self.paddle = Paddle(self)
                self.balls = [Ball(self,
                    self.w_layout // 2 - self.ball_diameter // 2,
                    self.paddle.y_paddle - self.ball_diameter,
                    self.paddle,self.G,
                    self.bricks,
                    self.launch
                )]

            self.paddle.update()
            for ball in self.balls:
                ball.update()

            for i in range(len(self.streak_score) - 1, -1, -1):
                s = self.streak_score[i]

                s.update()
                if s.t > 30:
                    self.streak_score.pop(i)



            for i in range(len(self.score_object) - 1, -1, -1):  # Iterate backwards

                s = self.score_object[i]

                if s.acquired:
                    self.streak += 1
                    self.score += self.P + self.Q*(self.streak -1)
                    self.streak_score.append(Streak_Score(s.x_obj, s.y_obj, self.P + self.Q*(self.streak -1)))
                    self.score_object.pop(i)  # Remove directly by index

                elif not s.alive:
                    self.streak = 0
                    self.score_object.pop(i)  # Remove directly by index

                else:
                    s.update()

            for b in self.bricks:
                if b.hit and b.hits == 1:

                    if b.brick_level == "5":
                        ball = Ball(self, b.x + 5, b.y + 3, self.paddle, self.G, self.bricks, True)
                        ball.active = False
                        ball.degree = randint(190, 350) 
                        ball.angle = math.radians(ball.degree)
                        ball.trig_multiplier()
                        v = randint(-210, -179)
                        ball.vx = -v*ball.cos_angle
                        ball.vy = v*ball.sin_angle

                        self.balls.append(ball)

                    else:

                        for _ in range(self.K):
                            self.score_object.append(Score_Object(self,randint(b.x + 1, b.x - 1 + b.w), randint(b.y + 1, b.y - 1 + b.h), b.brick_level, self.paddle, self.G, self.X ))
                b.update()

            if self.powerup_text:
                self.powerup_text[0].update()
                if self.powerup_text[0].t > 15:
                    self.powerup_text.pop(0)

            self.extra_lives = self.lives - 4
            if self.lives > len(self.lives_display) <4:
                if len(self.lives_display) >= 3:
                    self.lives_display.append(Bricks(self.lives_display[-1].x-16, self.lives_display[-1].y, "6.1"))

                else:
                    
                    self.lives_display.append(Bricks(self.lives_display[-1].x-16, self.lives_display[-1].y, "6"))
            

        if self.lenbricks == 0 and not self.loading_next_level and self.gamestate == 'playing level 1' and len(self.score_object) == 0:
            self.gamestate = 'loading level 2'
            self.loading_next_level = True
            self.load_next_level()


        if self.lenbricks == 0 and not self.loading_next_level and self.gamestate == 'playing level 2' and len(self.score_object) == 0:
            self.gamestate = 'loading level 3'
            self.loading_next_level = True
            self.load_next_level()

        if self.lives == 0:
            self.gamestate = 'gameover'

        if pyxel.btnp(pyxel.KEY_SPACE) and (self.gamestate == 'gameover' or self.gamestate == 'win'):
            self.load_restart()
            self.gamestate = 'playing level 1'

        if self.lenbricks == 0 and self.gamestate == 'playing level 3' and len(self.score_object) == 0:
            self.gamestate = 'win'

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

            if self.extend_paddle:

                if self.extend_paddle:
                    text = f"{math.ceil(self.t_extend_paddle / 30)}s"
                    text_width = len(text) * 4  
                    
                    text_x = 10 - text_width // 2
                    pyxel.circ(10, 140, 8, pyxel.COLOR_WHITE)
                    pyxel.blt(7, 135, 0, 136, 88, 7, 7, 0)
                    pyxel.text(text_x, 142, text, pyxel.COLOR_BLACK, None)

            if self.anti_gravity:

                pyxel.circ(110, 140, 8, pyxel.COLOR_WHITE)
                pyxel.blt(107, 135, 0, 128, 88, 7, 7, 0)
                pyxel.text(107, 142, f"{math.ceil(self.t_anti_gravity / 30)}s", pyxel.COLOR_BLACK, None)

            if self.powerup_text:
                self.powerup_text[0].draw()
            for b in self.balls:
                b.draw()
            self.paddle.draw()

            for brick in self.bricks:
                if brick.alive:
                    brick.draw()
                elif not brick.counted:
                    self.lenbricks -= 1
                    brick.counted = True

            for s in self.streak_score:
                s.draw()

            for s in self.score_object:
                s.draw()

            for i in self.lives_display:
                i.draw()

            if self.streak > 1:

                pyxel.text(5, 178, f'Streak: {self.streak}', pyxel.COLOR_BLACK, None)
        
            pyxel.text(5, 185, "Score: " + str(self.score), pyxel.COLOR_BLACK, None)
            if self.extra_lives >0:
                pyxel.text(97, 192, f"{self.extra_lives}X", pyxel.COLOR_BLACK, None)
                pyxel.blt(110,192, 0, 152, 80, 7,5, 0)

        #####

        if self.gamestate == 'loading level 1':
            Pregame().draw()
            pyxel.flip()  
            sleep(1)
            self.load_restart()

        if self.gamestate == 'loading level 2':
            NextStage1_2().draw()
            pyxel.flip()  
            sleep(1)
            self.gamestate = 'playing level 2'

        if self.gamestate == 'loading level 3':
            NextStage2_3().draw()
            pyxel.flip()  
            sleep(1)
            self.gamestate = 'playing level 3'

        if self.gamestate == 'win':
            Win().draw()
            pyxel.text(25, 172, "Your final score: " + str(self.score), pyxel.COLOR_WHITE)

        if self.gamestate == 'gameover':
            GameOver().draw()
        pyxel.mouse(visible=True)

        
Breakout()

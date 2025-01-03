import pyxel
from paddle import Paddle
import random
import json
from pprint import pprint
from bricks import brick_specs


class Powerup_Text:
    def __init__(self, txt_x: int, txt_y: int, txt: str, rec_x: int, rec_y: int, rec_w: int, rec_h: int, rec_color: int) -> None:

        self.txt_x = txt_x
        self.txt_y = txt_y
        self.txt = txt
        self.rec_x = rec_x
        self.rec_y = rec_y
        self.rec_w = rec_w
        self.rec_h = rec_h
        self.rec_color = rec_color
        self.t = 0

    def update(self):
        self.t += 1

    def draw(self):
        pyxel.rect(self.rec_x,self.rec_y, self.rec_w, self.rec_h, self.rec_color)
        pyxel.text(self.txt_x, self.txt_y, self.txt, pyxel.COLOR_WHITE, None)



def randomize_choice( X: int)-> int:
        choices = [1,2,3, 4, 5]
        weights= [(100 - X)*0.01, X* 0.0025,  X* 0.0025,  X* 0.0025,  X* 0.0025]  
        # Probabilities add up to 1 divides X to 4 powerups the rest will be normal score
        return random.choices(choices, weights, k=1)[0] 

def image_ref(x: int, brick_level: str):
    if x == 1:
        if brick_level == "1":
            return "8"
        elif brick_level == "2":
            return "8.1"
        else:
            return "8.2"
    elif x == 2:
        return "9"
    elif x == 3 :
        return "9.2"
    elif x == 4:
        return "9.3"
    else:
        return "9.4"

class Streak_Score:
    def __init__(self, x: float, y : float, score: int):
        self.x = x
        self.y = y
        self.score =score
        self.t = 0

    def update(self):
        self.t+= 1

    def draw(self):
        pyxel.text(self.x, self.y, f"+{self.score}", pyxel.COLOR_WHITE, None)


class Score_Object:

    def __init__(self, main, x: int, y: int, brick_level: str, paddle: Paddle, gravity: int, X: int) -> None:
        self.main = main
        self.X = X
        self.x_obj = x
        self.y_obj = y
        self.brick_level = brick_level
        self.type = randomize_choice(self.X) 
        self.image = image_ref(self.type,self.brick_level)
        self.paddle = paddle
        self.acquired = False
        self.alive = True
        self.G = gravity
        self.vy = 20
        self.acc_y = 0

        # Load brick data once
        # self.obj_data = access_json('bricks')
        # obj = self.obj_data.get(self.image, None)

        obj = brick_specs.get(float(self.image), None)
        if obj:
            self.img = obj['img']
            self.w_obj = obj['w']
            self.h_obj = obj['h']
            self.u = obj['u']
            self.v = obj['v']

    def powerup(self):
        if self.image == "9":
            self.main.lives += 1
            self.main.powerup_text.append(Powerup_Text(40,35, "Life UP!", 33,33,45,9,8))

        elif self.image == "9.2":
            self.main.anti_gravity = True
            self.main.t_anti_gravity += 300
            self.main.powerup_text.append(Powerup_Text(33,35, "Anti-Gravity!", 30,33,55,9,3))
        elif self.image == "9.3":
            self.main.extend_paddle = True
            self.main.t_extend_paddle += 300
            self.main.powerup_text.append(Powerup_Text(43,35, "EXTEND!", 38,33,35,9,13))

        else:
            self.main.powerup_text.append(Powerup_Text(35,35,  f"Better Luck\n Next Time!", 33,33,47,15,9))



    def update(self):
        if self.alive:
            if self.main.anti_gravity:
                self.acc_y = -self.G
            else:
                self.acc_y = 0
            new_y = self.y_obj + self.vy * (1 / 60) + 0.5 * (self.G) * (1 / 60)  # Apply gravity

            if self.acquired:
                self.alive = False
            elif (self.y_obj <= self.paddle.y_paddle - self.h_obj and  
                 self.paddle.x_paddle - self.w_obj < self.x_obj < self.paddle.x_paddle + self.paddle.w_paddle and
                 new_y > self.paddle.y_paddle - self.h_obj):
                
                # checks if the current object is above the paddle and if updated paddle is below
                # will draw at the top of the paddle and add score 
                
                self.y_obj = self.paddle.y_paddle - self.h_obj
                self.acquired = True  
                if self.type != 1:
                    if self.type == 5:
                        self.image = random.choice(["9", "9.1", "9.2", "9.3"])
                    self.powerup()

            elif (self.paddle.x_paddle - self.w_obj <self.x_obj < self.paddle.x_paddle + self.paddle.w_paddle and
                  self.paddle.y_paddle - self.h_obj<= self.y_obj < self.paddle.y_paddle + self.paddle.h_paddle):
                
                # if obj inside the paddle will not be drawn anymore 
                self.acquired = True
                self.alive = False
                if self.type != 1:
                    if self.type == 5:
                        self.image = random.choice(["9", "9.1", "9.2", "9.3"])
                    self.powerup()

            elif self.y_obj >= self.paddle.h_layout:
                self.alive = False
            else:
                # If the object hasn't hit the paddle yet, keep falling
                self.y_obj = new_y

            

            self.vy += (self.acc_y +self.G)
    def draw(self): # testing only
        if self.alive: 
            pyxel.blt(self.x_obj, self.y_obj, self.img,self.u,self.v, self.w_obj,self.h_obj, 0)


            

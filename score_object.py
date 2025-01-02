import pyxel
from paddle import Paddle
import random
import json
from pprint import pprint

brick_specs = {1: {
                    "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 80,
                    "v": 64,
                    "w": 16,
                    "h": 16
                    },
        2: {        "score": 100,
                    "hits": 2,
                    "img": 0,
                    "u": 112,
                    "v": 64,
                    "w": 16,
                    "h": 16
               },
        2.1: {      "score": 100,
                    "hits": 2,
                    "img": 0,
                    "u": 112,
                    "v": 80,
                    "w": 16,
                    "h": 16
               },
        3: {        "score": 150,
                    "hits": 3,
                    "img": 0,
                    "u": 96,
                    "v": 48,
                    "w": 16,
                    "h": 16
                    },
        3.1: {        "score": 150,
                    "hits": 3,
                    "img": 0,
                    "u": 96,
                    "v": 64,
                    "w": 16,
                    "h": 16
                    },
        3.2: {        "score": 150,
                    "hits": 3,
                    "img": 0,
                    "u": 112,
                    "v": 48,
                    "w": 16,
                    "h": 16
                    },
        4: {        "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 80,
                    "v": 80,
                    "w": 16,
                    "h": 16
                    },
        5: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 80,
                    "v": 48,
                    "w": 16,
                    "h": 16
                    },
        6: {     "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 96,
                    "v": 80,
                    "w": 16,
                    "h": 16
                    },
        6.1: {     "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 112,
                    "v": 96,
                    "w": 16,
                    "h": 16
                    },
        6.2: {     "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 152,
                    "v": 80,
                    "w": 7,
                    "h": 7
                    },
        7: {        "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 0,
                    "v": 120,
                    "w": 16,
                    "h": 16
                    },
        8: {        "score": 0,
                    "hits": 1,
                    "img": 0,
                    "u": 144,
                    "v": 32,
                    "w": 7,
                    "h": 7
                    },
        8.1: {       "score": 0,
                    "hits": 1,
                    "img": 0,
                    "u": 152,
                    "v": 32,
                    "w": 7,
                    "h": 7
                    },
        8.2: {        "score": 0,
                    "hits": 1,
                    "img": 0,
                    "u": 144,
                    "v": 40,
                    "w": 7,
                    "h": 7
                    },
        8.3: {        "score": 0,
                    "hits": 1,
                    "img": 0,
                    "u": 152,
                    "v": 40,
                    "w": 7,
                    "h": 7
                    },
        9: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 128,
                    "v": 80,
                    "w": 7,
                    "h": 7
                    },
        9.1: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 136,
                    "v": 80,
                    "w": 7,
                    "h": 7
                    },
        9.2: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 128,
                    "v": 88,
                    "w": 7,
                    "h": 7
                    },
        9.3: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 136,
                    "v": 88,
                    "w": 7,
                    "h": 7
                    },
        9.4: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 144,
                    "v": 80,
                    "w": 7,
                    "h": 7
                    }
}


#store brick specifications in json file
with open('bricks.json', 'w') as f:
    json.dump(brick_specs, f)

def access_json(file: str):
    brick = {}

    with open(file+'.json', 'r') as f:
        brick = json.load(f)

    return brick


def randomize_choice( X: int)-> int:
        choices = [1,2 , 3, 4, 5] # to be updated based on json 
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

    def __init__(self, main, x: int, y: int, brick_level: str, points: int, paddle: Paddle, gravity: int, X: int) -> None:
        self.main = main
        self.X = X
        self.x_obj = x
        self.y_obj = y
        self.brick_level = brick_level
        self.type = randomize_choice(self.X) 
        self.image = image_ref(self.type,self.brick_level)
        self.points = points
        self.paddle = paddle
        self.acquired = False
        self.alive = True
        self.G = gravity  

        # Load brick data once
        self.obj_data = access_json('bricks')
        obj = self.obj_data.get(self.image, None)
        if obj:
            self.img = obj['img']
            self.w_obj = obj['w']
            self.h_obj = obj['h']
            self.u = obj['u']
            self.v = obj['v']

    def powerup(self):
        if self.image == "9":
            print(True, "add heart")
            self.main.lives += 1

        elif self.image == "9.2":
            print(True, "antigravity")
            self.main.anti_gravity = True
            self.main.t_anti_gravity += 300
        elif self.image == "9.3":
            self.main.extend_paddle = True
            self.main.t_extend_paddle += 300

        else:
            pass



    def update(self):
        if self.alive:
            new_y = self.y_obj + self.G  # Apply gravity

            if self.acquired:
                self.alive = False
            elif (self.y_obj <= self.paddle.y_paddle - self.h_obj and  
                 self.paddle.x_paddle - self.w_obj < self.x_obj < self.paddle.x_paddle + self.paddle.w_paddle and
                 new_y > self.paddle.y_paddle - self.h_obj):
                
                # checks if the current object is above the paddle and if updated paddle is below
                # will draw at the top of the paddle and add score 
                
                self.y_obj = self.paddle.y_paddle - self.h_obj
                self.acquired = True  
                self.powerup()


            elif (self.paddle.x_paddle - self.w_obj <self.x_obj < self.paddle.x_paddle + self.paddle.w_paddle and
                  self.paddle.y_paddle - self.h_obj<= self.y_obj < self.paddle.y_paddle + self.paddle.h_paddle):
                
                # if obj inside the paddle will not be drawn anymore 
                self.acquired = True
                self.alive = False
                self.powerup()

            elif self.y_obj >= self.paddle.h_layout:
                self.alive = False
            else:
                # If the object hasn't hit the paddle yet, keep falling
                self.y_obj = new_y
    def draw(self): # testing only
        if self.alive: 
            pyxel.blt(self.x_obj, self.y_obj, self.img,self.u,self.v, self.w_obj,self.h_obj, 0)


            

import pyxel
from paddle import Paddle
import random

def randomize_choice( X: int)-> int:
        choices = [1, 2, 3, 4, 5] # to be updated based on json 
        weights= [(100 - X)*0.01, X* 0.0025,  X* 0.0025,  X* 0.0025,  X* 0.0025]  
        # Probabilities add up to 1 divides X to 4 powerups the rest will be normal score
        return random.choices(choices, weights, k=1)[0] 

class Score_Object:

    def __init__(self, x: int, y: int, points: int, paddle: Paddle, gravity: int, X: int) -> None:
        self.X = X
        self.x_obj = x
        self.y_obj = y
        self.type = randomize_choice(self.X) 
        self.points = points
        self.paddle = paddle
        self.acquired = False
        self.alive = True
<<<<<<< HEAD
        self.G = 5  
        self.h_obj = 8  
        self.w_obj = 8  
=======
        self.G = gravity
        self.h_obj = 3  
        self.w_obj = 3 

>>>>>>> 42dc8b31a699f8f2c75901307b789418a8803dbd

    def update(self):
        if self.alive:
            new_y = self.y_obj + self.G  # Apply gravity

            # Check if the object has reached the paddle's top and is horizontally aligned
            if (self.y_obj + self.h_obj >= self.paddle.y_paddle and
                self.x_obj >= self.paddle.x_paddle and
                self.x_obj <= self.paddle.x_paddle + self.paddle.w_paddle):
                self.y_obj = self.paddle.y_paddle - self.h_obj
                self.acquired = True  
                self.alive = False  
            elif self.y_obj >= self.paddle.h_layout:
                self.alive = False
            else:
                # If the object hasn't hit the paddle yet, keep falling
                self.y_obj = new_y

<<<<<<< HEAD
    def draw(self):
        if self.alive:  
            pyxel.blt(self.x_obj, self.y_obj, 0, 144, 32, self.w_obj, self.h_obj, 0)
=======
    def draw(self): # testing only
        if self.alive: 
            if self.type == 1: 
                pyxel.rect(self.x_obj, self.y_obj, self.w_obj, self.h_obj, pyxel.COLOR_LIME)
            elif self.type == 2:
                pyxel.rect(self.x_obj, self.y_obj, self.w_obj, self.h_obj, pyxel.COLOR_DARK_BLUE)
            elif self.type == 3:
                pyxel.rect(self.x_obj, self.y_obj, self.w_obj, self.h_obj, pyxel.COLOR_PEACH)
            elif self.type == 4:
                pyxel.rect(self.x_obj, self.y_obj, self.w_obj, self.h_obj, pyxel.COLOR_PINK)

            else:
                pyxel.rect(self.x_obj, self.y_obj, self.w_obj, self.h_obj, pyxel.COLOR_GRAY)


            
>>>>>>> 42dc8b31a699f8f2c75901307b789418a8803dbd

import pyxel
from paddle import Paddle

class Score_Object:

    def __init__(self, x: int, y: int, points: int, paddle: Paddle) -> None:
        self.x_obj = x
        self.y_obj = y
        self.points = points
        self.paddle = paddle
        self.acquired = False
        self.alive = True
        self.G = 5  
        self.h_obj = 8  
        self.w_obj = 8  

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

    def draw(self):
        if self.alive:  
            pyxel.blt(self.x_obj, self.y_obj, 0, 144, 32, self.w_obj, self.h_obj, 0)

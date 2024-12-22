
import math
import pyxel
class Ball:
    def __init__(self, x: float, y: float) -> None:
        self.w_layout = 120
        self.h_layout = 200
        self.G = 1
        self.vx = 0
        self.vy = 0
        self.v = 0
        self.t = 0
        self.pad_y = y
        self.MR = math.pi/12

        self.x_ball = x
        self.y_ball = y

        self.r_ball = 2
    
    def update(self, x: float, w_pad: float):


        # free fall only (can be used if nasa gitna)
        # time and initial velocity tantsa lang

        self.new_y_ball = self.y_ball + self.v * self.t + 0.5 * self.G * (self.t**2)


        if self.y_ball <= self.pad_y:

            # Collision with the paddle
            if x <= self.x_ball <= x + w_pad and self.new_y_ball + self.r_ball >= self.pad_y:
                self.y_ball= self.pad_y + 1
                self.v = -math.sqrt(2*self.G*self.pad_y) # Invert velocity for an upward bounce
                self.t = 1/30

            else:
                if self.new_y_ball >= self.h_layout:
                    self.y_ball = self.h_layout -self.r_ball -1
                else:
                    self.y_ball = self.new_y_ball
                    self.v = self.v + self.G*self.t
                    self.t += 1/30

            #    with the ceiling
            if self.y_ball - self.r_ball <= 0:
                self.y_ball = self.r_ball
                self.v = 0 # Invert velocity for a downward bounce
                self.t = 1/30

        else:

            if self.new_y_ball >= self.h_layout:
                    self.y_ball = self.h_layout -self.r_ball -1

            else:
                self.y_ball = self.new_y_ball 

                # Update the ball's velocity due to gravity
                self.v = self.v + self.G*self.t
                self.t += 1/30


    def draw(self):
        ball = pyxel.circ(self.x_ball, self.y_ball, self.r_ball, pyxel.COLOR_DARK_BLUE)

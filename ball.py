
import math
import pyxel
class Ball:
    def __init__(self, x: float, y: float, w_pad: float) -> None:
        self.w_layout = 120
        self.h_layout = 200
        self.G = 1
        self.w_pad = w_pad
        self.x_pad = 0
        self.acceleration = 0
        self.angle = math.pi/36
        self.v_pad = -math.sqrt(2*self.G*(y+3))/ math.sin(math.pi/36)
        self.vx = 0
        self.vy = 0
        self.v = 0
        self.t = 0
        self.pad_y = y
        self.degree: int| None = None

        self.x_ball = x
        self.y_ball = y

        self.r_ball = 2

        self.launch = False
    
    def update(self, x_pad: float):

        self.x_pad = x_pad


        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.launch = True
            self.degree = None

        if self.launch == True:

            if self.vy < 0:  # Moving upward
                self.acceleration = -0.3 * self.G  # Counteract gravity a bit (reduced gravity)
            else:  # Moving downward or at peak
                self.acceleration = 0 

            self.new_y_ball = self.y_ball + (self.vy *self.t) + ((self.G + self.acceleration) * (self.t**2))
            self.new_x_ball = self.x_ball + self.vx*(1/60)

            if self.new_x_ball - self.r_ball -1 <= 0:

                self.x_ball = self.r_ball + 1
                self.vx *=(-1)

            elif self.new_x_ball >= self.w_layout:
                self.x_ball= self.w_layout - self.r_ball -1
                self.vx *= (-1)

            else:
                self.x_ball = self.new_x_ball


            if self.y_ball <= self.pad_y: # for y component

                # Collision with the paddle
                if ((x_pad <= self.x_ball +self.r_ball <= x_pad+ self.w_pad) or (x_pad <= self.x_ball - self.r_ball <= x_pad + self.w_pad))  and (self.new_y_ball +self.r_ball) > self.pad_y+ 1:
                    self.y_ball= self.pad_y + 1
                    self.vy = 3 + self.v_pad*math.sin(self.angle) # Invert velocity for an upward bounce
                    self.t = 1/30

                    if self.vx == 0:
                        print(True)
                        self.vx = -self.v_pad*math.cos(self.angle)
                    elif self.vx > 0:  # Ball is coming from the left side
                        self.vx = abs(self.vx)  # Change direction to the right
                    else:  # Ball is coming from the right side
                        self.vx = -abs(self.vx)  # Change direction to the left


                else:
                    if self.new_y_ball >= self.h_layout:
                        self.y_ball = self.h_layout -self.r_ball -1
                    else:
                        if self.vy <= 0 and self.t % 0.1 == 0:
                            self.acceleration -= 0.5

                        self.y_ball = self.new_y_ball 
                        self.vy = self.vy + (self.G +self.acceleration)*self.t
                        self.t += 1/60

                #    with the ceiling
                if self.y_ball - self.r_ball <= 0:
                    self.y_ball = self.r_ball
                    self.vy =  3 # Invert velocity for a downward bounce
                    self.t = 1/30

            else:
                if self.new_y_ball >= self.h_layout:
                        self.y_ball = self.h_layout -self.r_ball -1

                else:
                    self.y_ball = self.new_y_ball 

                    # Update the ball's velocity due to gravity
                    self.vy = self.vy + self.G*self.t
                    self.t += 1/60
                    self.acceleration = 0.5

        else:
            if ((x_pad <= self.x_ball +self.r_ball <= x_pad+ self.w_pad) or (x_pad <= self.x_ball - self.r_ball <= x_pad + self.w_pad)):
                center_pad = x_pad + (self.w_pad/2)

                if self.x_ball == center_pad:
                    self.degree = 90

                elif self.x_ball <= x_pad:
                    self.degree = 175
                elif self.x_ball >= x_pad + self.w_pad:
                    self.degree = 5

                else:
                    self.degree = int(90 -((85/15)*(self.x_ball - center_pad)))


                self.angle = math.radians(self.degree)
            else:   
                self.degree = None

    def draw(self):

        ball = pyxel.blt(self.x_ball, self.y_ball, 1, 0, 0, 8, 8, 0)

        if self.degree != None:

            if self.x_ball <= self.x_pad + self.w_pad/2:
                angle_cyc = pyxel.text(self.x_pad + self.w_pad -10,self.pad_y -2, f"{self.degree}", pyxel.COLOR_WHITE, None)
            else:
                angle_cyc = pyxel.text(self.x_pad,self.pad_y -2, f"{self.degree}", pyxel.COLOR_WHITE, None)
            length = 15
            x2 = self.x_ball + length * math.cos(self.angle)
            y2 = self.y_ball - length * math.sin(self.angle)

            angled_line = pyxel.line(self.x_ball,self.y_ball,x2,y2, pyxel.COLOR_WHITE)

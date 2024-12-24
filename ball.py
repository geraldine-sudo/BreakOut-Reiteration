
import math
import pyxel
class Ball:
    def __init__(self, x: float, y: float, w_pad: float) -> None:
        #layout
        self.w_layout = 120
        self.h_layout = 200
        self.G = 5
        self.launch = False

        #paddle properties
        self.w_pad = w_pad
        self.x_pad = 0
        self.y_pad = y + 2
        self.MR = 10
        self.ML = 170
        self.start_acc = -300

        #ball properties
        self.acc_y = 0
        self.acc_x = 0
        self.vx = 0
        self.vy = 0
        self.v = 0
        self.t = 0
        self.degree: int| None #angle in degrees
        self.angle = 0 # angle in radians

        # Main Ball Properties
        self.x_ball = x
        self.y_ball: float= y
        self.r_ball = 2
        self.start_yloc = y

    
    def update(self, x_pad: float):

        self.x_pad = x_pad

        def ball_in_horbounds_of_paddle(x:float) -> bool:

            return x_pad <= x+self.r_ball <= (x_pad+ self.w_pad) or  x_pad <= x-self.r_ball <= (x_pad+ self.w_pad)

        def update_angle():
            if ball_in_horbounds_of_paddle(self.x_ball):
                    center_pad = x_pad + (self.w_pad/2)

                    if self.x_ball == center_pad:
                        self.degree = 90

                    elif self.x_ball <= x_pad:
                        self.degree = self.ML
                    elif self.x_ball >= x_pad + self.w_pad:
                        self.degree = self.MR

                    else:
                        self.degree = int(90 -(((90 -self.MR)/(self.w_pad/2))*(self.x_ball - center_pad)))


                    self.angle = math.radians(self.degree)
            else:   
                self.degree = None


        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.launch = True
            self.degree = None
            if ball_in_horbounds_of_paddle(self.x_ball):
                self.vy = self.start_acc*math.sin(self.angle)
                self.vx = self.start_acc*math.cos(self.angle)
                self.acc_y = self.G*(-1)
                self.acc_x = 0
 

        if self.launch:
            
            new_y_ball = self.y_ball + self.vy*(1/60) + 0.5*(self.acc_y + self.G)*(1/60)

            if ball_in_horbounds_of_paddle(self.x_ball):

                if self.y_ball == self.y_pad -2: # on top of paddle
                    self.y_ball = new_y_ball

                elif self.y_ball < self.start_yloc and new_y_ball > self.start_yloc:
                    # from above the paddle the new calculated ball surpassed the paddle

                    self.y_ball = self.start_yloc
                    self.acc_y = self.G*(-1)
                    self.vy = self.start_acc*math.sin(self.angle)

                elif self.y_ball < self.start_yloc and (new_y_ball- self.r_ball) <=0:
                    # from below the paddle and new calculated ball surpassed the height layout
                    self.y_ball = self.r_ball
                    self.acc_y = 0    #tentative
                    self.vy =  (-1)*self.vy +(self.acc_y + self.G)*(1/60)

                else:
                    if new_y_ball- self.r_ball >= self.h_layout:
                        self.y_ball = self.h_layout - self.r_ball
                        self.vy = 0  
                        self.acc_y = 0

                    else:
                        self.y_ball = new_y_ball 
                        self.vy += (self.acc_y + self.G)
            else:

                if (new_y_ball- self.r_ball) <=0:
                    self.y_ball = self.r_ball
                    self.acc_y = 0    #tentative
                    self.vy = (-1)*self.vy + (self.acc_y + self.G)
                
                elif new_y_ball- self.r_ball >= self.h_layout:
                    self.y_ball = self.h_layout - self.r_ball
                    self.vy = 0
                    self.acc_y = 0

                else:
                    self.y_ball = new_y_ball 
                    self.vy += (self.acc_y + self.G)

        else:
            update_angle()

    def draw(self):

        ball = pyxel.blt(self.x_ball, self.y_ball, 0, 8, 0, 8, 8, 0)

        if self.degree != None:

            if self.x_ball <= self.x_pad + self.w_pad/2:
                angle_cyc = pyxel.text(self.x_pad + self.w_pad -10,self.pad_y -2, f"{self.degree}", pyxel.COLOR_BLACK, None)
            else:
                angle_cyc = pyxel.text(self.x_pad,self.pad_y -2, f"{self.degree}", pyxel.COLOR_BLACK, None)
            length = 15
            x2 = self.x_ball + length * math.cos(self.angle)
            y2 = self.y_ball - length * math.sin(self.angle)

            angled_line = pyxel.line(self.x_ball,self.y_ball,x2,y2, pyxel.COLOR_BLACK)

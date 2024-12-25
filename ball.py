
import math
import pyxel
class Ball:
    def __init__(self, x: float, y: float, w_pad: float) -> None:
        #layout
        self.w_layout = 120
        self.h_layout = 200
        self.G = 5
        self.launch = False

        # Main Ball Properties
        self.x_ball = x
        self.y_ball: float= y
        self.r_ball = 2
        self.start_yloc = y

        #paddle properties
        self.w_pad = w_pad
        self.x_pad = 0
        self.y_pad = y + self.r_ball
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
        self.degree: int| None = None #angle in degrees
        self.angle = 0 # angle in radians

        #component multiplier

        self.sin_angle = 1
        self.cos_angle = 1

    def trig_multiplier(self):
        if self.degree == 90:
            self.sin_angle = 1.0  # sin(90 degrees) is exactly 1
            self.cos_angle = 0.0  # cos(90 degrees) is exactly 0
        else:
            self.sin_angle = math.sin(self.angle)
            self.cos_angle = math.cos(self.angle)

    def ball_in_horbounds_of_paddle(self, x:float) -> bool:

            return self.x_pad <= x+self.r_ball <= (self.x_pad+ self.w_pad
            ) or  self.x_pad <= x-self.r_ball <= (self.x_pad+ self.w_pad)
    
    def update_angle(self):
            d = 0
            if not self.launch:
                if self.ball_in_horbounds_of_paddle(self.x_ball):
                    center_pad = self.x_pad + (self.w_pad/2)

                    if self.x_ball == center_pad:
                        self.degree = 90

                    elif self.x_ball <= self.x_pad:
                        self.degree = self.ML
                    elif self.x_ball >= self.x_pad + self.w_pad:
                        self.degree = self.MR

                    else:
                        self.degree = int(90 -(((90 -self.MR)/(self.w_pad/2))*(self.x_ball - center_pad)))

                    self.angle = (math.pi)*self.degree/180
                else:
                       
                    self.degree = None

            else:
                if self.ball_in_horbounds_of_paddle(self.x_ball):
                    if self.vx == 0:
                        center_pad = self.x_pad + (self.w_pad/2)

                        if self.x_ball == center_pad:
                            self.degree = 90

                        elif self.x_ball <= self.x_pad:
                            self.degree = self.ML
                        elif self.x_ball >= self.x_pad + self.w_pad:
                            self.degree = self.MR
                        else:
                            self.degree = int(90 -(((90 -self.MR)/(self.w_pad/2))*(self.x_ball - center_pad)))

                    elif self.x_ball <= self.x_pad:
                        self.degree = self.ML

                    elif self.x_ball >= self.x_ball + self.w_pad:
                        self.degee = self.MR
                        
                    elif self.vx > 0:
                        print(2)
                        d = int(abs(self.x_pad + (self.w_pad/2) - self.x_ball))
                        if d != 0:
                            self.degree = int(self.MR*(self.w_pad/2)/d)
                        else:
                            self.degree = 90

                        if self.degree < self.MR:
                            self.degree = self.MR

                    else:
                        d = int(abs(self.x_pad + (self.w_pad/2) - self.x_ball))
                        if d != 0:
                            self.degree = int(((self.ML-90)/(self.w_pad/2))*d) + 90
                        else:
                            self.degree = 90

                        if self.degree > self.ML:
                            self.degree = 170


                    if self.degree != None:

                        self.angle = (math.pi)*self.degree/180

            print(f"x: {self.x_ball},Degree: {self.degree}, Angle: {self.angle}, Distance from paddle: {d}")



    def line_interpolation(self, x: float, y:float, find:str, coor:float)-> float:
        "coor is your new set coordinate"

        if (x - self.x_ball) != 0 and (y - self.y_ball) != 0 :
            m = (y - self.y_ball)/(x - self.x_ball)
            b = self.y_ball - m*self.x_ball

            if find == "x":
                return (coor + b)/m
            
            else:
                return m*coor + b
            
        else:
            if find == "x":
                return self.x_ball
            else:
                return self.y_ball
    
    def update(self, x_pad: float):

        self.x_pad = x_pad

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if not self.launch and self.ball_in_horbounds_of_paddle(self.x_ball):
                self.trig_multiplier ()
                self.vy = self.start_acc*self.sin_angle
                self.acc_y = self.G*(-1)
                self.vx = -self.start_acc*self.cos_angle

            self.launch = True
 

        if self.launch:

            new_y_ball = self.y_ball + self.vy*(1/60) + 0.5*(self.acc_y + self.G)*(1/60)
            new_x_ball = self.x_ball + self.vx*(1/60) + 0.5*(self.acc_x)*(1/60)

            if new_x_ball - self.r_ball <= 0:
                self.vx*=(-1)
                self.acc_x*=(-1)
                self.x_ball = self.r_ball
                new_y_ball = self.line_interpolation(new_x_ball,new_y_ball,"y", self.x_ball)

            elif new_x_ball +self.r_ball >= self.w_layout:
                self.vx*=(-1)
                self.acc_x*=(-1)
                self.x_ball = self.w_layout -2
                new_y_ball = self.line_interpolation(new_x_ball,new_y_ball,"y", self.x_ball)
            else:
                self.x_ball = new_x_ball


            if self.ball_in_horbounds_of_paddle(self.x_ball):

                if self.y_ball == self.start_yloc: # on top of paddle
                    self.y_ball = new_y_ball

                elif self.y_ball < self.start_yloc and new_y_ball >= self.start_yloc:
                    # from above the paddle the new calculated ball surpassed the paddle
                    self.update_angle()
                    self.y_ball = self.start_yloc
                    self.acc_y = self.G*(-1)
                    self.trig_multiplier ()
                    self.vy = self.start_acc*self.sin_angle
                    self.vx = -self.start_acc*self.cos_angle

                elif (new_y_ball- self.r_ball) <=0:
                    #new calculated y is out of frame

                    self.y_ball = self.r_ball
                    self.acc_y = 0    #tentative
                    self.vy =  (-1)*self.vy +(self.acc_y + self.G)*(1/60)

                    self.x_ball = self.line_interpolation(self.x_ball,new_y_ball,"x", self.y_ball)

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
                    #new calculated y is out of frame
                    self.y_ball = self.r_ball
                    self.acc_y = 0    #tentative
                    self.vy = (-1)*self.vy + (self.acc_y + self.G)
                    self.x_ball = self.line_interpolation(self.x_ball,new_y_ball,"x", self.y_ball)
                
                elif new_y_ball- self.r_ball >= self.h_layout:
                    self.y_ball = self.h_layout - self.r_ball
                    self.vy = 0
                    self.acc_y = 0

                else:
                    self.y_ball = new_y_ball 
                    self.vy += (self.acc_y + self.G)

        else:
            self.update_angle()

    def draw(self):

        ball = pyxel.blt(self.x_ball, self.y_ball, 0, 8, 0, 8, 8, 0)

        if (not self.launch) and self.degree != None:

            if self.x_ball <= self.x_pad + self.w_pad/2:
                angle_cyc = pyxel.text(self.x_pad + self.w_pad -10,self.pad_y -2, f"{self.degree}", pyxel.COLOR_BLACK, None)
            else:
                angle_cyc = pyxel.text(self.x_pad,self.pad_y -2, f"{self.degree}", pyxel.COLOR_BLACK, None)
            length = 15
            x2 = self.x_ball + length * math.cos(self.angle)
            y2 = self.y_ball - length * math.sin(self.angle)

            angled_line = pyxel.line(self.x_ball,self.y_ball,x2,y2, pyxel.COLOR_BLACK)

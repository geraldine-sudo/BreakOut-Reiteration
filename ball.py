
import math
import pyxel
class Ball:
    def __init__(self, x: float, y: float, w_pad: float, h_pad:float) -> None:
        #layout
        self.w_layout = 120
        self.h_layout = 200
        self.G = 5
        self.launch = False

        # Main Ball Properties
        self.x_ball: float = x
        self.y_ball: float= y
        self.r_ball = 2
        self.start_yloc = y

        #paddle properties
        self.w_pad = w_pad
        self.h_pad = h_pad
        self.x_pad = 0
        self.y_pad = y + self.r_ball
        self.MR = 10
        self.ML = 170
        self.NT = 280
        self.NB = 80
        self.MT = 260
        self.MB = 100
        self.start_acc = -300
        self.h_pad = h_pad

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
            self.sin_angle = 1.0  
            self.cos_angle = 0.0 

        elif self.degree == 0 or  self.degree == 360:
            self.sin_angle = 0.0
            self.cos_angle = 1.0 

        elif self.degree == 180:
            self.sin_angle = 0.0  
            self.cos_angle = -1.0
            
        elif self.degree == 270:
            self.sin_angle = -1.0
            self.cos_angle = 0.0

        else:
            self.sin_angle = math.sin(self.angle)
            self.cos_angle = math.cos(self.angle)

    def ball_in_horbounds_of_paddle(self, x:float) -> bool:

            return self.x_pad <= x+self.r_ball <= (self.x_pad+ self.w_pad
            ) or  self.x_pad <= x-self.r_ball <= (self.x_pad+ self.w_pad)
    
    def intersection(self,P1: tuple[float, float], P2: tuple[float, float], P3: tuple[float, float], P4: tuple[float, float])-> None | tuple[float,float]:
        x1, y1 = P1
        x2, y2 = P2
        x3, y3 = P3
        x4, y4 = P4
        # Convert to standard form: Ax + By = C
        a1 = y2 - y1
        b1 = x1 - x2
        c1 = x1*a1 + b1*y1
        
        a2 = y4 - y3
        b2 = x3 - x4
        c2 = x3*a2 + b2*y3
        
        # Check if the lines are coincident
        if a1 * b2 == a2 * b1 and b1 * c2 == b2 * c1 and a1 * c2 == a2 * c1:
            return None # Lines are coincident, and we cannot determine a single intersection point
            # Get the intersection using Cramer's Rule
        
        d= a1 * b2 - b1 * a2  # Determinant of the matrix

        if d == 0:
            return None  # Lines are parallel and do not intersect
        else:
            # Coordinates of the intersection point
            x = (b2 * c1 - b1 * c2) // d
            y = (a1 * c2 - a2 * c1) // d

            # Check if the intersection point lies within the line segments
            if (
                min(x1, x2) <= x <= max(x1, x2)
                and min(y1, y2) <= y <= max(y1, y2)
                and min(x3, x4) <= x <= max(x3, x4)
                and min(y3, y4) <= y <= max(y3, y4)
            ):
                return(x, y)
            else:
                return None

    
    def update_angle(self):
            d = 0
            if not self.launch:
                
                x1, y1 = pyxel.mouse_x, pyxel.mouse_y
                x2, y2 = self.x_ball, self.y_ball
                
                # Vector difference
                dx = x1 - x2
                dy = y2 - y1
                
                # Calculate angle in radians and convert to degrees
                self.angle = math.atan2(dy, dx)
                self.degree = int(math.degrees(self.angle))

                if self.degree < 0:
                    if pyxel.mouse_x >= self.x_ball:
                        self.degree = 0

                    else:
                        self.degree = 180
                self.angle = math.radians(self.degree)
                self.trig_multiplier()

            else:
                if self.y_ball == self.start_yloc:
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

                    elif self.vx > 0:
                        d = int(abs(self.x_pad + (self.w_pad/2) - self.x_ball))
                        if d != 0:
                            if d < (self.w_pad/2):
                                self.degree = int(90 +(self.MR-90)*d/(self.w_pad//2))

                            else:
                                self.degree = self.MR
                        else:
                            self.degree = 90

                    else:
                        d = int(abs(self.x_pad + (self.w_pad/2) - self.x_ball))
                        if d != 0:
                            if d < (self.w_pad/2):
                                self.degree = int(90 +(self.ML-90)*d/(self.w_pad//2)) 
                            else:
                                self.degree = self.ML
                        else:
                            self.degree = 90


                elif self.x_ball == self.x_pad + self.r_ball + self.w_pad:
                    d = int(abs(self.y_pad + (self.h_pad/2) - self.y_ball))

                    if d != 0:
                        if self.vy >= 0:

                            if d < (self.h_pad/2):
                                self.degree = int(360+(self.NT-360)*d/(self.h_pad//2))
                            else:
                                self.degree = self.NT
                            
                        else:
                            if d < (self.h_pad/2):
                                self.degree = int((self.NB)*d/(self.h_pad//2))

                            else:
                                self.degree = self.NB
                            
                    else:
                        self.degree = 0

                elif self.x_ball == self.x_pad - self.r_ball:
                    d = int(abs(self.y_pad + (self.h_pad/2) - self.y_ball))


                    if d != 0:
                        if self.vy >= 0:
                            if d < (self.h_pad/2):
                                self.degree = int(180+(self.MT-180)*d/(self.h_pad//2))
                            else:
                                self.degree  = self.MT
                        else:
                            if d < (self.h_pad/2):
                                self.degree = int((self.MB-180)*d/(self.h_pad//2))

                            else:
                                self.degree = self.MT
                            
                    else:
                        self.degree = 180

            if self.degree:
                self.angle = math.radians(self.degree)
                self.trig_multiplier()
    
    def update(self, x_pad: float):

        past_pad = self.x_pad

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

            # Paddle Collsion
            if self.ball_in_horbounds_of_paddle(self.x_ball) and self.y_ball ==self.start_yloc:
                print(1)
                #at the top of paddle
                self.x_ball = new_x_ball
                self.y_ball = new_y_ball
                self.vy += (self.acc_y + self.G)

            elif self.x_ball == past_pad  - self.r_ball or self.x_ball == past_pad +self.w_pad + self.r_ball:
                self.x_ball = new_x_ball
                self.y_ball = new_y_ball
                self.vy += (self.acc_y + self.G)


            elif self.ball_in_horbounds_of_paddle(self.x_ball) and (
                self.y_ball < self.start_yloc < new_y_ball  and 
                self.ball_in_horbounds_of_paddle(new_x_ball)
            ): # above the paddle and it surpassed the paddle
                print(2)
                self.y_ball = self.start_yloc
                self.x_ball = new_x_ball
                self.update_angle()
                self.acc_y = -self.G
                self.vx = -self.start_acc*self.cos_angle
                self.vy = self.start_acc*self.sin_angle

            elif self.vx != 0:
                print(3)
                if self.y_ball >= self.h_pad + self.y_pad + self.r_ball:
                    top =self.intersection((self.x_ball,self.y_ball), (new_x_ball,new_y_ball), (self.x_pad - self.r_ball,
                        self.y_pad- self.r_ball),(self.x_pad +self.w_pad +self.r_ball,self.y_pad- self.r_ball))
                    
                    if top: # will go through the top of the paddle
                        self.y_ball = self.start_yloc
                        self.x_ball = top[0]
                        self.update_angle()
                        self.acc_y = -self.G
                        self.vx = -self.start_acc*self.cos_angle
                        self.vy = self.start_acc*self.sin_angle
                        return
                
                if self.vx > 0:
                    side = self.intersection((self.x_ball,self.y_ball), (new_x_ball,new_y_ball), (self.x_pad - self.r_ball,
                    self.y_pad- self.r_ball),(self.x_pad - self.r_ball,self.y_pad+self.r_ball+ self.h_pad))
                else:
                    print("line_interpolation")
                    side = self.intersection((self.x_ball,self.y_ball), (new_x_ball,new_y_ball), (self.x_pad +self.w_pad +self.r_ball,
                    self.y_pad- self.r_ball),(self.x_pad +self.w_pad +self.r_ball,self.y_pad+self.r_ball+ self.h_pad))

                if side:
                    if self.vx >0:
                        print("yes")
                        self.x_ball = self.x_pad - self.r_ball
                    else:
                        print("no")
                        self.x_ball = self.x_pad +self.w_pad +self.r_ball

                    self.y_ball = side[1]
                    self.update_angle()
                    self.vx = (-1)*self.vx -self.start_acc*self.cos_angle
                    self.vy = self.start_acc*self.sin_angle

                    return
                # will go through the side of the paddle
                self.x_ball = new_x_ball
                self.y_ball = new_y_ball
                self.vy += (self.acc_y + self.G)

            else:
                print(4)
                if self.ball_in_horbounds_of_paddle(new_x_ball) and (
                    self.start_yloc <= new_y_ball <= self.y_pad + self.h_pad + self.r_ball):

                    if self.x_ball < self.x_pad + self.w_pad // 2:
                        self.x_ball = self.x_pad - self.r_ball
                    else:
                        self.x_ball = self.x_pad + self.r_ball + self.w_pad

                    self.y_ball = new_y_ball
                    self.update_angle()
                    self.vx = -self.start_acc*self.cos_angle
                    self.vy = self.start_acc*self.sin_angle

                else:
                    self.x_ball = new_x_ball
                    self.y_ball = new_y_ball
                    self.vy  += (self.acc_y + self.G)


            #Wall Collision

            if self.x_ball -self.r_ball <= 0:
                self.x_ball = self.r_ball 
                self.vy += (self.acc_y + self.G)
                self.vx *= -1

            elif self.x_ball + 2> self.w_layout:
                self.x_ball_ball = self.w_layout - self.r_ball
                self.vy += (self.acc_y + self.G)
                self.vx *= -1

            if (self.y_ball - self.r_ball) <=0:
                #new calculated y is out of frame
                self.y_ball = self.r_ball
                self.acc_y = 0    #tentative
                self.vy = (-1)*self.vy + (self.acc_y + self.G)
                
            elif new_y_ball- self.r_ball >= self.h_layout:
                    self.y_ball = self.h_layout - self.r_ball
                    self.vy = 0
                    self.acc_y = -self.G
                    self.vx = 0

        else:
            self.update_angle()

    def draw(self):

        ball = pyxel.blt(self.x_ball, self.y_ball, 0, 8, 0, 8, 8, 0)

        if (not self.launch) and self.degree != None:

            if self.x_ball <= self.x_pad + self.w_pad/2:
                angle_cyc = pyxel.text(self.x_pad + self.w_pad -10,self.y_pad -2, f"{self.degree}", pyxel.COLOR_BLACK, None)
                # angle_cyc = pyxel.text(self.x_pad + self.w_pad -10,self.y_pad -2, f"{self.degree}", pyxel.COLOR_WHITE, None)
            else:
                angle_cyc = pyxel.text(self.x_pad,self.y_pad -2, f"{self.degree}", pyxel.COLOR_BLACK, None)
                # angle_cyc = pyxel.text(self.x_pad,self.y_pad -2, f"{self.degree}", pyxel.COLOR_WHITE, None)
            length = 15
            x2 = self.x_ball + length * math.cos(self.angle)
            y2 = self.y_ball - length * math.sin(self.angle)

            angled_line = pyxel.line(self.x_ball,self.y_ball,x2,y2, pyxel.COLOR_BLACK)
            # angled_line = pyxel.line(self.x_ball,self.y_ball,x2,y2, pyxel.COLOR_WHITE)

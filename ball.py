
import math
import pyxel
from bricks import Bricks
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
        self.r_ball = 3.5
        self.start_yloc = y
        self.ball_diameter = 7

        #paddle properties
        self.w_pad = w_pad
        self.h_pad = h_pad
        self.x_pad = 0
        self.y_pad = y + self.r_ball
        self.start_acc = -240
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
        self.trail : list[tuple[float,float]] = []

        #Angles
        self.MR = 10
        self.ML = 170
        self.NT = 280
        self.NB = 80
        self.MT = 260
        self.MB = 100
        self.NR = 350
        self.NL = 190

        #component multiplier

        self.sin_angle = 1
        self.cos_angle = 1

        #bricks
        """stage 1"""
        self.bricks = [
                        Bricks(25 + 5, 40, '1', '1', 5, 21),
                        Bricks(50 + 5, 45, '1', '1', 5, 21),
                        Bricks(75 + 5, 40, '1', '1', 5, 21),
                        Bricks(95 + 5, 25, '1', '1', 5, 21),
                        Bricks(5 + 5, 25, '1', '1', 5, 21),  # 2 hits
                        Bricks(50 + 5, 10, '1', '1', 5, 21),
                        Bricks(75 + 5, 15, '1', '1', 5, 21),  # op hits
                        Bricks(25 + 5, 15, '1', '1', 5, 21),
                        #Bricks(10 + 1, 75, '1', '1', 14, 15), #brown spider
                        #Bricks(96 + 1, 65, '1', '1', 15, 16) # spider with ball

                    ]
        
        """stage 2
        self.bricks =[
                        Bricks(10, 20, '1', '1', 15, 15),
                        Bricks(30, 25, '1', '1', 15, 15),
                        Bricks(55, 25, '1', '1', 15, 15),
                        Bricks(75, 25, '1', '1', 15, 15),  # ball maker
                        Bricks(100, 25, '1', '1', 15, 15),
                        Bricks(18, 115, '1', '1', 15, 15),  # 3 hits
                        Bricks(65, 85, '1', '1', 15, 15),
                        Bricks(45, 90, '1', '1', 15, 15),
                        Bricks(25, 75, '1', '1', 15, 15),
                        Bricks(95, 90, '1', '1', 15, 15)
                    ]"""
        
        """stage 3
        self.bricks = [
                        Bricks(11, 30, '1', '1', 6, 12),
                        Bricks(21, 65, '1', '1', 6, 12),  # 2 hits
                        Bricks(91, 65, '1', '1', 6, 12),  # ball maker
                        Bricks(101, 30, '1', '1', 6, 12)  # op hits
                    ]"""


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

            return self.x_pad <= x <= (self.x_pad+ self.w_pad
            ) or  self.x_pad <= x + self.ball_diameter <= (self.x_pad+ self.w_pad)

    def get_line_intersection(self, p1:tuple[float,float], p2:tuple[float,float], p3:tuple[float,float], p4:tuple[float,float]):
    # Using the line segment intersection formula
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4

        # Denominator of the intersection formula
        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:  # Parallel lines
            return None

        # Numerators for the intersection point
        t1 = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        t2 = (x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)

        # Intersection points
        t1 /= denom
        t2 /= denom

        # If the intersection point lies on both line segments, return it
        if 0 <= t1 <= 1 and 0 <= t2 <= 1:
            ix = x1 + t1 * (x2 - x1)
            iy = y1 + t1 * (y2 - y1)
            return (ix, iy)
    
        return None
    def update_angle(self,pos: str,x: float, y:float, w: float, h: float):

        center_x_ball = self.x_ball + self.r_ball
        center_y_ball = self.y_ball + self.r_ball

        d = 0
        if not self.launch:
            
            x1, y1 = pyxel.mouse_x, pyxel.mouse_y
            x2, y2 = self.x_pad + self.w_pad//2, self.y_pad
            
            # Vector difference
            dx = x1 - x2
            dy = y2 - y1
            
            # Calculate angle in radians and convert to degrees
            self.angle = math.atan2(dy, dx)
            self.degree = int(math.degrees(self.angle))

            if self.degree < 0:
                if pyxel.mouse_x >= self.w_layout//2:
                    self.degree = 0

                else:
                    self.degree = 180
            self.angle = math.radians(self.degree)
            self.trig_multiplier()

        else:
            if pos == "top":
                if self.vx == 0:
                    center_pad = x + (w/2)

                    if center_x_ball == center_pad:
                        self.degree = 90

                    elif center_x_ball <= x:
                        self.degree = self.ML
                    elif center_x_ball >= x + w:
                        self.degree = self.MR
                    else:
                        self.degree = int(90 -(((90 -self.MR)/(w/2))*(center_x_ball - center_pad)))

                elif self.vx > 0:
                    d = int(abs(x + (w/2) - center_x_ball))
                    if d != 0:
                        if d < (w/2):
                            self.degree = int(90 +(self.MR-90)*d/(w//2))

                        else:
                            self.degree = self.MR
                    else:
                        self.degree = 90

                else:
                    d = int(abs(x + (w/2) - center_x_ball))
                    if d != 0:
                        if d < (w/2):
                            self.degree = int(90 +(self.ML-90)*d/(w//2)) 
                        else:
                            self.degree = self.ML
                    else:
                        self.degree = 90


            elif pos == "right":
                d = int(abs(y + (h/2) - center_y_ball))

                if d != 0:
                    if self.vy >= 0:

                        if d < (h/2):
                            self.degree = int(360+(self.NT-360)*d/(h//2))
                        else:
                            self.degree = self.NT
                        
                    else:
                        if d < (h/2):
                            self.degree = int((self.NB)*d/(h//2))

                        else:
                            self.degree = self.NB
                        
                else:
                    self.degree = 0

            elif pos == "left":
                d = int(abs(y + (h/2) - center_y_ball))


                if d != 0:
                    if self.vy >= 0:
                        if d < (self.h_pad/2):
                            self.degree = int(180+(self.MT-180)*d/(h/2))
                        else:
                            self.degree  = self.MT
                    else:
                        if d < (h/2):
                            self.degree = int((self.MB-180)*d/(h//2))

                        else:
                            self.degree = self.MT
                        
                else:
                    self.degree = 180

            else:
                if self.vx == 0:
                    center_pad = x + (w/2)

                    if center_x_ball == center_pad:
                        self.degree = 270
                    elif center_x_ball <= self.x_pad:
                        self.degree = self.NL
                    elif center_x_ball >= self.x_pad + self.w_pad:
                        self.degree = self.NR

                    else:
                        self.degree = int(270 -(((270 -self.NR)/(w/2))*(center_x_ball - center_pad)))

                elif self.vx > 0:
                    d = int(abs(x + (w/2) - center_x_ball))
                    if d != 0:
                        if d < (w/2):
                            self.degree = int(270 +(self.NR-270)*d/(w//2))

                        else:
                            self.degree = self.NR
                    else:
                        self.degree = 270

                else:
                    d = int(abs(x + (w/2) - center_x_ball))
                    if d != 0:
                        if d < (w/2):
                            self.degree = int(270 +(self.NL-270)*d/(w//2)) 
                        else:
                            self.degree = self.NL
                    else:
                        self.degree = 270

        
        self.angle = math.radians(self.degree)
        self.trig_multiplier()
        if self.degree == 180 or self.degree == 360 or self.degree == 0:
            self.acc_y = 0

    def brick_collision(self, new_x_ball: float, new_y_ball: float, brick : Bricks) ->  None | tuple[float,float,float,str, Bricks]:
        center_ball = (self.x_ball,self.y_ball)
        new_ball_center =(new_x_ball,new_y_ball)
        top_left = (brick.x - self.ball_diameter,brick.y - self.ball_diameter)
        top_right = (brick.x + brick.w, brick.y - self.ball_diameter)
        bottom_left= (brick.x -self.ball_diameter, brick.y + brick.h)
        bottom_right = (brick.x + brick.w, brick.y+brick.h)
        interesections: list[tuple[float,float,float, str, Bricks]] = []
        if self.vy > 0:
            extremes = self.get_line_intersection(center_ball, new_ball_center, top_left, top_right)
            if extremes:
                interesections.append((extremes[0], extremes[1], (extremes[0]-center_ball[0])**2 + (extremes[1]-center_ball[1])**2, "top", brick))
        else:
            extremes = self.get_line_intersection(center_ball, new_ball_center, bottom_left, bottom_right)
            if extremes:
                interesections.append((extremes[0], extremes[1], (extremes[0]-center_ball[0])**2 + (extremes[1]-center_ball[1])**2, "bottom", brick))
            
        if self.vx <= 0:
            
            side = self.get_line_intersection(center_ball, new_ball_center, top_right, bottom_right)
            if side:
                interesections.append((side[0], side[1], (side[0]-center_ball[0])**2 + (side[1]-center_ball[1])**2, "right", brick))
        elif self.vx>0:
            side = self.get_line_intersection(center_ball, new_ball_center, top_left, bottom_left)
            if side:
                interesections.append((side[0], side[1], (side[0]-center_ball[0])**2 + (side[1]-center_ball[1])**2, "left", brick))
            
        return None if len(interesections) <= 0 else sorted(interesections, key = lambda b: b[2])[0]

    def update(self, x_pad: float):

        past_pad = self.x_pad

        self.x_pad = x_pad

        self.trail.append((self.x_ball + self.r_ball, self.y_ball + self.r_ball))

        if len(self.trail) > 5:
            self.trail.pop(0)

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if not self.launch and self.ball_in_horbounds_of_paddle(self.x_ball):
                self.trig_multiplier ()
                self.vy = self.start_acc*self.sin_angle
                if self.degree != 180 or self.degree !=0:
                    self.acc_y = self.G*(-1)
                self.vx = -self.start_acc*self.cos_angle

            self.launch = True

        if self.launch:
            new_y_ball = self.y_ball + self.vy*(1/60) + 0.5*(self.acc_y + self.G)*(1/60)
            new_x_ball = self.x_ball + self.vx*(1/60) + 0.5*(self.acc_x)*(1/60)

            if self.degree == 0:
                print(f"vx: {self.vx},  vy: {self.vy}, newx : {new_x_ball}, newy: {new_y_ball}")


            #Bricks collision

            ball_bricks_collide = min((pt for b in self.bricks if (pt := self.brick_collision(new_x_ball, new_y_ball, b))),
                            default=None, key=lambda x: x[2])
            
            if ball_bricks_collide:
                print(1)

                if ball_bricks_collide[3] == "top":
                    self.x_ball = ball_bricks_collide[0] 
                    self.y_ball = ball_bricks_collide[1]
                    self.update_angle("top", ball_bricks_collide[4].x,ball_bricks_collide[4].y, ball_bricks_collide[4].w, ball_bricks_collide[4].h)
                    self.vy = self.start_acc*self.sin_angle
                    self.vx = -self.start_acc*self.cos_angle
                    self.acc_y = 0

                elif ball_bricks_collide[3] == "bottom":
                    self.x_ball = ball_bricks_collide[0]
                    self.y_ball = ball_bricks_collide[1]
                    self.update_angle("bottom", ball_bricks_collide[4].x,ball_bricks_collide[4].y, ball_bricks_collide[4].w, ball_bricks_collide[4].h)
                    self.vy = self.start_acc*self.sin_angle
                    self.vx = -self.start_acc*self.cos_angle
                    self.acc_y = -self.G

                elif ball_bricks_collide[3] == "right":
                    self.x_ball = ball_bricks_collide[0]
                    self.y_ball = ball_bricks_collide[1]
                    self.update_angle("right", ball_bricks_collide[4].x,ball_bricks_collide[4].y, ball_bricks_collide[4].w, ball_bricks_collide[4].h)
                    self.vy = self.start_acc*self.sin_angle
                    self.vx = -self.start_acc*self.cos_angle
                    if self.degree == 0:
                        print(self. cos_angle, self.acc_y, self.vx, f"new_y_ball {self.y_ball + self.vy*(1/60) + 0.5*(self.acc_y + self.G)*(1/60)} ew_x_ball:{self.x_ball + self.vx*(1/60) + 0.5*(self.acc_x)*(1/60)} brickx {ball_bricks_collide[4].x} bricky {ball_bricks_collide[4].y}")

                else:
                    self.x_ball = ball_bricks_collide[0]
                    self.y_ball = ball_bricks_collide[1] 
                    self.update_angle("left", ball_bricks_collide[4].x,ball_bricks_collide[4].y, ball_bricks_collide[4].w, ball_bricks_collide[4].h)
                    self.vy = self.start_acc*self.sin_angle
                    self.vx = -self.start_acc*self.cos_angle
                return
                
            
            # Paddle Collsion

            else:
                if self.ball_in_horbounds_of_paddle(self.x_ball) and self.y_ball == self.start_yloc:
                    
                    #at the top of paddle
                    self.x_ball = new_x_ball
                    self.y_ball = new_y_ball
                    self.vy += (self.acc_y + self.G)

                elif self.x_ball == past_pad - self.ball_diameter or self.x_ball == past_pad +self.w_pad:
                    self.x_ball = new_x_ball
                    self.y_ball = new_y_ball
                    self.vy += (self.acc_y + self.G)

                elif self.ball_in_horbounds_of_paddle(self.x_ball) and (
                    self.y_ball < self.start_yloc < new_y_ball  and 
                    self.ball_in_horbounds_of_paddle(new_x_ball)
                ): # above the paddle and it surpassed the paddle
                
                    self.y_ball = self.start_yloc
                    self.x_ball = new_x_ball
                    self.update_angle("top", self.x_pad,self.y_pad,self.w_pad,self.h_pad)
                    self.acc_y = -self.G
                    self.vx = -self.start_acc*self.cos_angle
                    self.vy = self.start_acc*self.sin_angle

                elif self.vx != 0:
                    
                    if self.y_ball <= self.start_yloc and self.vy >0:
                        top =self.get_line_intersection((self.x_ball,self.y_ball), (new_x_ball,new_y_ball), (self.x_pad - self.ball_diameter,
                            self.y_pad-self.ball_diameter),(self.x_pad +self.w_pad,self.y_pad-self.ball_diameter))
                        
                        if top: # will go through the top of the paddle
                            self.y_ball = self.start_yloc
                            self.x_ball = top[0]
                            self.update_angle("top", self.x_pad,self.y_pad,self.w_pad,self.h_pad)
                            self.acc_y = -self.G
                            self.vx = -self.start_acc*self.cos_angle
                            self.vy = self.start_acc*self.sin_angle
                            return
                    
                    if self.vx > 0:
                        side = self.get_line_intersection((self.x_ball,self.y_ball), (new_x_ball,new_y_ball), (self.x_pad -self.ball_diameter,
                        self.y_pad- self.ball_diameter),(self.x_pad - self.ball_diameter,self.y_pad+self.h_pad))
                    else:
                        side = self.get_line_intersection((self.x_ball,self.y_ball), (new_x_ball,new_y_ball), (self.x_pad +self.w_pad,
                        self.y_pad- self.ball_diameter),(self.x_pad +self.w_pad,self.y_pad+self.h_pad))

                    if side:
                        self.y_ball = side[1]
                        if self.vx >0:
                            
                            self.x_ball = self.x_pad - self.ball_diameter
                            self.update_angle("left", self.x_pad,self.y_pad,self.w_pad,self.h_pad)
                        else:
                            self.x_ball = self.x_pad +self.w_pad
                            self.update_angle("right", self.x_pad,self.y_pad,self.w_pad,self.h_pad)
                        self.vx = -self.start_acc*self.cos_angle
                        self.vy = self.start_acc*self.sin_angle

                        return
                          

                    self.x_ball = new_x_ball
                    self.y_ball = new_y_ball
                    self.vy += (self.acc_y + self.G)

                else:
            
                    if self.ball_in_horbounds_of_paddle(new_x_ball) and (
                        self.start_yloc <= self.y_ball <= self.y_pad + self.h_pad):

                        if self.x_ball < self.x_pad + self.w_pad // 2:
                            self.x_ball = self.x_pad - self.ball_diameter
                            self.update_angle("left", self.x_pad,self.y_pad,self.w_pad,self.h_pad)
                        else:
                            self.x_ball = self.x_pad + self.w_pad
                            self.update_angle("right", self.x_pad,self.y_pad,self.w_pad,self.h_pad)

                        self.vx = -self.start_acc*self.cos_angle
                        self.vy = self.start_acc*self.sin_angle

                    else:
                        self.x_ball = new_x_ball
                        self.y_ball = new_y_ball
                        self.vy  += (self.acc_y + self.G)


            #Wall Collision

            if self.x_ball <= 0:
                self.x_ball = 0 
                self.vy += (self.acc_y + self.G)
                self.vx *= -1

            elif self.x_ball  +self.ball_diameter> self.w_layout:
                self.x_ball = self.w_layout - self.ball_diameter
                self.vy += (self.acc_y + self.G)
                self.vx *= -1

            if self.y_ball <=0:
                #new calculated y is out of frame
                self.y_ball = 0
                self.acc_y = 0    #tentative
                self.vy = (-1)*self.vy + (self.acc_y + self.G)
                
            elif new_y_ball + self.ball_diameter >= self.h_layout:
                    self.y_ball = self.h_layout - self.ball_diameter
                    self.vy = 0
                    self.acc_y = -self.G
                    self.vx = 0

        else:
            self.update_angle("top", self.x_pad,self.y_pad,self.w_pad,self.h_pad)

    def draw(self):

        print(self.x_ball,self.y_ball, self.degree)

        # In the draw method:
        for  (tx, ty) in self.trail:
            pyxel.rect(tx+ self.r_ball, ty, 3.5//2, 3.5//2, pyxel.COLOR_WHITE)

        ball = pyxel.blt(self.x_ball, self.y_ball, 0, 8, 0, 8, 8, 0)

        if not self.launch and self.degree != None:

            if self.x_ball <= self.x_pad + self.w_pad/2:
                angle_cyc = pyxel.text(self.x_pad + self.w_pad -10,self.y_pad -2, f"{self.degree}", pyxel.COLOR_BLACK, None)
                # angle_cyc = pyxel.text(self.x_pad + self.w_pad -10,self.y_pad -2, f"{self.degree}", pyxel.COLOR_WHITE, None)
            else:
                angle_cyc = pyxel.text(self.x_pad,self.y_pad -2, f"{self.degree}", pyxel.COLOR_BLACK, None)
                # angle_cyc = pyxel.text(self.x_pad,self.y_pad -2, f"{self.degree}", pyxel.COLOR_WHITE, None)
            length = 15
            x2 =  self.w_layout //2+ length * math.cos(self.angle)
            y2 = self.y_pad - length * math.sin(self.angle)

            angled_line = pyxel.line(self.w_layout//2,self.y_pad,x2,y2, pyxel.COLOR_BLACK)
            # angled_line = pyxel.line(self.x_ball,self.y_ball,x2,y2, pyxel.COLOR_WHITE)

    

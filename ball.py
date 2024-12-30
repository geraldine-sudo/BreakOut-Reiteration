
import math
import pyxel
from paddle import Paddle
from bricks import Bricks
from typing import Literal

Sides = Literal["top", "bottom", "left" , "right"]
class Ball:
    def __init__(self, main: object, x: float, y: float, paddle: Paddle, bricks: None, life: int, launch: bool) -> None:
        #layout
        self.w_layout = 120
        self.h_layout = 200
        self.G = 5
        self.launch = launch
        self.lives = life

        # Main Ball Properties
        self.x_ball: float = x
        self.y_ball: float= y
        self.ball_diameter = 7
        self.r_ball = self.ball_diameter /2
        self.start_yloc = paddle.y_paddle - self.ball_diameter

        #paddle properties
        self.paddle = paddle
        self.past_paddle = self.paddle.x_paddle
        self.start_acc = -240

        #ball properties
        self.acc_y = 0
        self.acc_x = 0
        self.vx = 0
        self.vy = 0
        self.v = 0
        self.t = 0
        self.trail : list[tuple[float,float]] = []

        #Angles
        self.cycle_speed = 4
        self.degree: int = 0 #angle in degrees
        self.angle = 0 # angle in radians
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
        self.bricks = bricks

        self.is_colliding_with_brick = False
    
    def update_lives(self):
        return self.lives


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

            return self.paddle.x_paddle <= x <= ( self.paddle.x_paddle + self.paddle.w_paddle
            ) or  self.paddle.x_paddle <= x + self.ball_diameter <= (self.paddle.x_paddle+ self.paddle.w_paddle)

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

            self.degree +=self.cycle_speed

            if self. degree == 0 or self.degree == 180:
                self.cycle_speed *= -1
            

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
                        if d < (self.paddle.h_paddle/2):
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
                    elif center_x_ball <= self.paddle.x_paddle:
                        self.degree = self.NL
                    elif center_x_ball >= self.paddle.x_paddle + self.paddle.w_paddle:
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


    def paddle_collision(self, new_x_ball: float, new_y_ball: float) -> None | tuple[float, float, Sides]:
        center_ball = (self.x_ball,self.y_ball)
        new_ball_center =(new_x_ball,new_y_ball)
        top_left = (self.paddle.x_paddle- self.ball_diameter,self.paddle.y_paddle - self.ball_diameter)
        top_right = (self.paddle.x_paddle + self.paddle.w_paddle, self.paddle.y_paddle - self.ball_diameter)
        bottom_left= (self.paddle.x_paddle -self.ball_diameter, self.paddle.y_paddle + self.paddle.h_paddle )
        bottom_right = (self.paddle.x_paddle + self.paddle.w_paddle, self.paddle.y_paddle + self.paddle.h_paddle)

        if self.vy > 0:
            extremes = self.get_line_intersection(center_ball, new_ball_center, top_left, top_right)
            if extremes:
                return (extremes[0], extremes[1], "top")
        else:
            extremes = self.get_line_intersection(center_ball, new_ball_center, bottom_left, bottom_right)
            if extremes:
                return (extremes[0], extremes[1], "bottom")
            
        if self.vx <= 0:
            side = self.get_line_intersection(center_ball, new_ball_center, top_right, bottom_right)
            if side:
               return (side[0], side[1], "right")
        elif self.vx>0:
            side = self.get_line_intersection(center_ball, new_ball_center, top_left, bottom_left)
            if side:
                return (side[0], side[1], "left")
            
        return None

    def brick_collision(self, new_x_ball: float, new_y_ball: float, brick : Bricks, 
                        brick_num: int) ->  None | tuple[float,float,float,str, Bricks, int]:
        
        interesections: list[tuple[float,float,float, str, Bricks, int]] = []

        center_ball = (self.x_ball,self.y_ball)
        new_ball_center =(new_x_ball,new_y_ball)
        top_left = (brick.x - self.ball_diameter,brick.y - self.ball_diameter)
        top_right = (brick.x + brick.w, brick.y - self.ball_diameter)
        bottom_left= (brick.x -self.ball_diameter, brick.y + brick.h)
        bottom_right = (brick.x + brick.w, brick.y+brick.h)
        if self.vy > 0:
            extremes = self.get_line_intersection(center_ball, new_ball_center, top_left, top_right)
            if extremes:
                interesections.append((extremes[0], extremes[1], (extremes[0]-center_ball[0])**2 + (extremes[1]-center_ball[1])**2, "top", brick,brick_num))
        else:
            extremes = self.get_line_intersection(center_ball, new_ball_center, bottom_left, bottom_right)
            if extremes:
                interesections.append((extremes[0], extremes[1], (extremes[0]-center_ball[0])**2 + (extremes[1]-center_ball[1])**2, "bottom",brick, brick_num))
            
        if self.vx <= 0:
            
            side = self.get_line_intersection(center_ball, new_ball_center, top_right, bottom_right)
            if side:
                interesections.append((side[0], side[1], (side[0]-center_ball[0])**2 + (side[1]-center_ball[1])**2, "right", brick, brick_num))
        elif self.vx>0:
            side = self.get_line_intersection(center_ball, new_ball_center, top_left, bottom_left)
            if side:
                interesections.append((side[0], side[1], (side[0]-center_ball[0])**2 + (side[1]-center_ball[1])**2, "left", brick, brick_num))
            
        return None if len(interesections) <= 0 else sorted(interesections, key = lambda b: b[2])[0]


    def update(self):

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
            self.paddle.launch = True

        if self.launch:
            new_y_ball = self.y_ball + self.vy*(1/60) + 0.5*(self.acc_y + self.G)*(1/60)
            new_x_ball = self.x_ball + self.vx*(1/60) + 0.5*(self.acc_x)*(1/60)


            #Bricks collision

            ball_bricks_collide= min((pt for n, b in enumerate(self.bricks) if b.alive and (
                                                    pt := self.brick_collision(new_x_ball, new_y_ball, b, n))),
                                                    default=None,key=lambda x: x[2])

            if ball_bricks_collide:
                self.is_colliding_with_brick = True

                self.bricks[ball_bricks_collide[5]].brick_level = str(int(self.bricks[ball_bricks_collide[5]].brick_level) -1)


                self.x_ball = ball_bricks_collide[0] 
                self.y_ball = ball_bricks_collide[1]
                self.update_angle(ball_bricks_collide[3], ball_bricks_collide[4].x,ball_bricks_collide[4].y, ball_bricks_collide[4].w, ball_bricks_collide[4].h)
                self.vy = self.start_acc*self.sin_angle
                self.vx = -self.start_acc*self.cos_angle
                
                if ball_bricks_collide[3] == "top":
                    self.acc_y = -self.G

                elif ball_bricks_collide[3] == "bottom":
                    self.acc_y = 0

                self.past_paddle = self.paddle.x_paddle
                return
                
            
            # Paddle Collsion

            else:
                if self.ball_in_horbounds_of_paddle(self.x_ball) and self.y_ball == self.start_yloc:
                    
                    #at the top of paddle
                    self.x_ball = new_x_ball
                    self.y_ball = new_y_ball
                    self.vy += (self.acc_y + self.G)

                elif self.x_ball == self.past_paddle - self.ball_diameter or self.x_ball == self.past_paddle +self.paddle.w_paddle:
                    self.x_ball = new_x_ball
                    self.y_ball = new_y_ball
                    self.vy += (self.acc_y + self.G)

                elif self.ball_in_horbounds_of_paddle(self.x_ball) and (
                    self.y_ball < self.start_yloc < new_y_ball  and 
                    self.ball_in_horbounds_of_paddle(new_x_ball)
                ): # above the paddle and it surpassed the paddle
                
                    self.y_ball = self.start_yloc
                    self.x_ball = new_x_ball
                    self.update_angle("top", self.paddle.x_paddle,self.paddle.y_paddle,self.paddle.w_paddle,self.paddle.h_paddle)
                    self.acc_y = -self.G
                    self.vx = -self.start_acc*self.cos_angle
                    self.vy = self.start_acc*self.sin_angle

                else:
                    ball_paddle_collide = self.paddle_collision(new_x_ball,new_y_ball)


                    if ball_paddle_collide:

                        self.x_ball = ball_paddle_collide[0] 
                        self.y_ball = ball_paddle_collide[1]
                        self.update_angle(ball_paddle_collide[2], self.paddle.x_paddle,self.paddle.y_paddle, self.paddle.w_paddle,self.paddle.h_paddle)
                        self.vy = self.start_acc*self.sin_angle
                        self.vx = -self.start_acc*self.cos_angle

                        if ball_paddle_collide[2] == "top":
                            self.acc_y = -self.G
                        elif ball_paddle_collide[2] == "bottom":
                            self.acc_y = 0

                    else:
                        self.y_ball = new_y_ball
                        self.x_ball = new_x_ball
                        self.vy += (self.acc_y + self.G)
                
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
                    self.y_ball = self.start_yloc
                    self.x_ball = self.paddle.x_paddle +self.paddle.w_paddle /2 - self.r_ball
                    self.lives -=1
                    self.update_lives()
                    self.degree = 0
                    self.cycle_speed = abs(self.cycle_speed)
                    self.paddle.x_paddle = self.w_layout// 2 - self.paddle.w_paddle//2
                    self.x_ball = self.paddle.x_paddle +self.paddle.w_paddle /2 - self.r_ball
                    self.launch = False
                    self.paddle.launch = False

            self.past_paddle = self.paddle.x_paddle

        else:
            self.past_paddle = self.paddle.x_paddle
            self.update_angle("top", self.paddle.x_paddle,self.paddle.y_paddle,self.paddle.w_paddle,self.paddle.h_paddle)

    
    def is_brick_colliding(self):
        return self.is_colliding_with_brick

    def draw(self):


        for  (tx, ty) in self.trail:
            pyxel.rect(tx+ self.r_ball, ty, 3.5//2, 3.5//2, pyxel.COLOR_RED)

        ball = pyxel.blt(self.x_ball, self.y_ball, 0, 8, 0, 8, 8, 0)

        if not self.launch and self.degree != None:

            #angle_cyc = pyxel.text(self.paddle.x_paddle + self.paddle.w_paddle -10,self.paddle.y_paddle -2, f"{self.degree}", pyxel.COLOR_BLACK, None)
                # angle_cyc = pyxel.text(self.paddle.x_paddle + self.paddle.w_paddle -10,self.paddle.y_paddle -2, f"{self.degree}", pyxel.COLOR_WHITE, None)
            length = 15
            x2 =  self.paddle.x_paddle +self.paddle.w_paddle /2 + length * math.cos(self.angle)
            y2 = self.paddle.y_paddle - length * math.sin(self.angle)

            angled_line = pyxel.line(self.paddle.x_paddle +self.paddle.w_paddle //2,self.paddle.y_paddle,x2,y2, pyxel.COLOR_BLACK)
            # angled_line = pyxel.line(self.x_ball,self.y_ball,x2,y2, pyxel.COLOR_WHITE)

    

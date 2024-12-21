import pyxel

class Ball:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200

        self.x_ball = 60
        self.y_ball = 145

        self.r_ball = 2
    
    def update(self):
        ...

    def draw(self):
        ball = pyxel.circ(self.x_ball, self.y_ball, self.r_ball, pyxel.COLOR_DARK_BLUE)

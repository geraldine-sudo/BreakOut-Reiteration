import pyxel

class Paddle:
    def __init__(self, main) -> None:

        self.main = main

        self.orig_w_paddle = 22
        self.extend_w_paddle = 40

        self.w_layout = 120
        self.h_layout = 200

        self.w_paddle = 22
        self.h_paddle = 14

        self.x_paddle = self.w_layout//2 -self.w_paddle//2
        self.y_paddle = 160

        self.dx = 3
        self.launch = False

    def update(self):

        if self.main.extend_paddle:
            self.w_paddle = self.extend_w_paddle

        else:
            self.w_paddle = self.orig_w_paddle



        if self.launch:

            # always ensure that the mouse is within layout before moving
            if pyxel.mouse_x > self.w_paddle / 2 + self.x_paddle and (0 < pyxel.mouse_y <= self.h_layout):
                self.x_paddle += self.dx
    
            if pyxel.mouse_x < self.w_paddle / 2 + self.x_paddle and (0 < pyxel.mouse_y <= self.h_layout):
                self.x_paddle -= self.dx

            # horizontal border
            self.x_paddle = max(0, min(self.x_paddle, pyxel.width - self.w_paddle))

    def draw(self):
        if self.main.extend_paddle:
            pyxel.blt(self.x_paddle, self.y_paddle, 0, 127, 95, self.w_paddle, self.h_paddle, 0)

        else:
            pyxel.blt(self.x_paddle, self.y_paddle, 0, 0, 135, self.w_paddle, self.h_paddle, 0)
        # pyxel.blt(self.x_paddle, self.y_paddle, 0, 24, 136, self.w_paddle, self.h_paddle, 0)
        if (0 < pyxel.mouse_x <= self.w_layout) and (0 < pyxel.mouse_y <= self.h_layout):
            pyxel.text(5, 190, f'x: {pyxel.mouse_x}', pyxel.COLOR_BLACK, None)

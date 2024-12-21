import pyxel

class Paddle:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200

        self.x_paddle = 45
        self.y_paddle = 165

        self.w_paddle = 30
        self.h_paddle = 5
    
    def update(self):
        self.x_paddle = min(self.w_layout - self.w_paddle, max(0, pyxel.mouse_x))

    def draw(self):
        paddle = pyxel.rect(self.x_paddle, self.y_paddle, self.w_paddle, self.h_paddle, pyxel.COLOR_GREEN)
        cur_x = pyxel.text(5, 190, f'x: {self.x_paddle}', pyxel.COLOR_WHITE, None)

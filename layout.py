import pyxel

class Breakout:
    def __init__(self):
        pyxel.init(120, 180)
        pyxel.run(self.update, self.draw)

    def update(self):
        ...

    def draw(self):
        pyxel.cls(0)
        ball = pyxel.circ(60, 110, 3, pyxel.COLOR_DARK_BLUE)
        paddle = pyxel.rect(45, 130, 30, 6, pyxel.COLOR_GREEN)

Breakout()
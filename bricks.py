import pyxel

class Bricks:
    def __init__(self) -> None:
        ...

    def update(self):
        ...

    def draw(self):

        # for final stage
        for i in range(0, 160, 15):
            pyxel.line(0, 0, pyxel.width, i, pyxel.COLOR_WHITE)
        for i in range(0, 160, 15):
            pyxel.line(pyxel.width, 0, 0, i, pyxel.COLOR_WHITE)

        # bricks
        


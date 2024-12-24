import pyxel

class Stage3Map:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        pyxel.rect(0, 0, self.w_layout, self.h_layout, pyxel.COLOR_WHITE)

        # cosmetics
        for i in range(0, 160, 15):
            pyxel.line(0, 0, pyxel.width, i, pyxel.COLOR_BLACK)
        for i in range(0, 160, 15):
            pyxel.line(pyxel.width, 0, 0, i, pyxel.COLOR_BLACK)

        
        pyxel.ellib(-30, -75, 55, 200, pyxel.COLOR_BLACK)

        pyxel.ellib(-20, -100, 55, 200, pyxel.COLOR_BLACK)

        pyxel.ellib(90, -100, 55, 200, pyxel.COLOR_BLACK)

        pyxel.ellib(100, -75, 55, 200, pyxel.COLOR_BLACK)

        pyxel.blt(30, 25, 0, 0, 152, 100, 65, 0)

        
        pyxel.blt(5, 12, 0, 0, 224, 50, 16, 0)

        for x in range(12, 80, 12):
            pyxel.blt(x, 12, 0, 0, 224, 50, 16, 0)


        # pyxel.blt(12, 12, 0, 0, 224, 50, 16, 0)

        # pyxel.blt(24, 12, 0, 0, 224, 50, 16, 0)

        # pyxel.blt(36, 12, 0, 0, 224, 50, 16, 0)

        # pyxel.blt(48, 12, 0, 0, 224, 50, 16, 0)

        pyxel.text(10, 15, 'Other Mother craves flesh.', pyxel.COLOR_RED)


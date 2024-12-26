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





        
        # cocoons 
        pyxel.line(14, 0, 14, 40, pyxel.COLOR_BLACK)
        pyxel.blt(10, 30, 0, 72, 0, 8, 16, 0)

        pyxel.line(24, 0, 24, 70, pyxel.COLOR_BLACK)
        pyxel.blt(20, 65, 0, 24, 0, 8, 16, 0)

        pyxel.line(94, 0, 94, 66, pyxel.COLOR_BLACK)
        pyxel.blt(90, 65, 0, 64, 0, 8, 16, 0)

        pyxel.line(104, 0, 104, 40, pyxel.COLOR_BLACK)
        pyxel.blt(100, 30, 0, 32, 0, 8, 16, 0)

        # text bg
        pyxel.blt(30, 25, 0, 0, 152, 60, 65, 0)
        pyxel.blt(5, 12, 0, 0, 224, 50, 16, 0)

        for x in range(12, 80, 12):
            pyxel.blt(x, 12, 0, 0, 224, 50, 16, 0)


        pyxel.text(10, 15, 'Other Mother craves flesh.', pyxel.COLOR_RED)




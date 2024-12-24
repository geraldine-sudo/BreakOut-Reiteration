import pyxel

class Stage2Map:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        pyxel.rect(0, 0, self.w_layout, self.h_layout, pyxel.COLOR_NAVY)

        pyxel.elli(0, -60, 100, 350, pyxel.COLOR_PURPLE)

        pyxel.elli(10, -40, 100, 250, pyxel.COLOR_DARK_BLUE)

        pyxel.ellib(10, -40, 105, 250, pyxel.COLOR_BLACK)

        pyxel.elli(35, 25, 75, 150, pyxel.COLOR_PURPLE)

        pyxel.elli(23, 0, 75, 150, pyxel.COLOR_NAVY)

        pyxel.ellib(23, 0, 85, 150, pyxel.COLOR_BLACK)

        pyxel.ellib(15, 0, 95, 150, pyxel.COLOR_PURPLE)

        pyxel.elli(32, 15, 55, 120, pyxel.COLOR_PURPLE)

        pyxel.elli(35, 40, 55, 75, pyxel.COLOR_NAVY)

        pyxel.ellib(30, 40, 55, 75, pyxel.COLOR_BLACK)

        pyxel.elli(43, 43, 35, 65, pyxel.COLOR_DARK_BLUE)

        # door

        pyxel.rect(50, 55, 25, 35, pyxel.COLOR_NAVY)
        pyxel.rectb(50, 55, 25, 35, pyxel.COLOR_PURPLE)

        pyxel.circ(69, 72, 2, pyxel.COLOR_WHITE)

        # string

        pyxel.ellib(-10, -20, 200, 55, pyxel.COLOR_GRAY)

        pyxel.ellib(80, -100, 55, 200, pyxel.COLOR_GRAY)

        pyxel.ellib(-20, -50, 55, 200, pyxel.COLOR_GRAY)

        pyxel.ellib(15, -100, 85, 200, pyxel.COLOR_GRAY)

        # bricks

        pyxel.blt(10, 20, 0, 16, 104, 16, 16, 0)

        pyxel.blt(30, 25, 0, 48, 80, 16, 16, 0)

        pyxel.blt(55, 25, 0, 48, 104, 16, 16, 0)

        pyxel.blt(75, 25, 0, 32, 104, 16, 16, 0)

        pyxel.blt(100, 25, 0, 16, 120, 16, 16, 0)

        pyxel.blt(18, 115, 0, 32, 120, 16, 16, 0)

        pyxel.blt(65, 85, 0, 48, 120, 16, 16, 0)

        pyxel.blt(45, 90, 0, 32, 104, 16, 16, 0)

        pyxel.blt(25, 75, 0, 16, 120, 16, 16, 0)

        pyxel.blt(95, 90, 0, 48, 80, 16, 16, 0)






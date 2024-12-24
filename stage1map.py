import pyxel

class Stage1Map:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        # back
        pyxel.rect(0, 0, 120, 108, pyxel.COLOR_NAVY)
        pyxel.rect(0, 108, 120, 108, pyxel.COLOR_LIME)

        # ominous shadow
        pyxel.elli(50, -50, 50, 150, pyxel.COLOR_BLACK)

        # plate
        pyxel.elli(0, 85, 120, 50, pyxel.COLOR_WHITE)
        pyxel.ellib(8, 75, 100, 52, pyxel.COLOR_NAVY)

        # cake
        pyxel.rect(5, 50, 110, 45, pyxel.COLOR_PEACH)
        pyxel.elli(5, 68, 110, 52, pyxel.COLOR_PEACH)
        pyxel.elli(5, 25, 110, 50, pyxel.COLOR_PINK)
        
        # bottom frosting
        for x in range(20, 90, 16):
            pyxel.blt(x, 108, 0, 16, 16, 16, 16, 0)
                
        pyxel.blt(0, 95, 0, 32, 16, 16, 16, 0)
        pyxel.blt(10, 105, 0, 32, 16, 16, 16, 0)

        pyxel.blt(98, 102, 0, 48, 16, 16, 16, 0)
        pyxel.blt(105, 95, 0, 48, 16, 16, 16, 0)

        # welcome home
        pyxel.blt(25, 35, 0, 24, 32, 45, 16, 0)
        pyxel.blt(60, 35, 0, 24, 64, 45, 16, 0)
        
        pyxel.blt(45, 45, 0, 24, 48, 35, 16, 0)

        # brick
        pyxel.blt(25, 40, 0, 0, 32, 20, 35, 0)

        pyxel.blt(50, 45, 0, 0, 32, 20, 35, 0)

        pyxel.blt(75, 40, 0, 0, 32, 20, 35, 0)

        pyxel.blt(95, 25, 0, 0, 32, 20, 35, 0)

        pyxel.blt(5, 25, 0, 0, 32, 20, 35, 0)

        pyxel.blt(50, 10, 0, 0, 32, 20, 35, 0)

        pyxel.blt(75, 15, 0, 0, 32, 20, 35, 0)

        pyxel.blt(25, 15, 0, 0, 32, 20, 35, 0)
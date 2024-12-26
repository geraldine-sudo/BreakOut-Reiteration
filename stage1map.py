import pyxel

class Stage1Map:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        # back
        pyxel.rect(0, 0, 120, 108, pyxel.COLOR_NAVY)
        pyxel.rect(0, 108, 120, 108, pyxel.COLOR_YELLOW)

        # ominous shadow
        pyxel.elli(50, -50, 50, 150, pyxel.COLOR_BLACK)

        # plate
        pyxel.elli(2, 87, 120, 50, pyxel.COLOR_NAVY)
        pyxel.elli(0, 85, 120, 50, pyxel.COLOR_WHITE)
        pyxel.ellib(8, 75, 100, 52, pyxel.COLOR_NAVY)


        # cake
        pyxel.rect(5, 50, 110, 45, pyxel.COLOR_PEACH)
        pyxel.elli(5, 68, 110, 52, pyxel.COLOR_PEACH)
        pyxel.elli(5, 25, 110, 50, pyxel.COLOR_PINK)
        
        # cake drip
        pyxel.blt(50, 75, 0, 80, 0, 16, 16, 0)
        pyxel.blt(35, 65, 0, 80, 16, 16, 16, 0)
        pyxel.blt(15, 65, 0, 80, 0, 16, 16, 0)
        pyxel.blt(5, 55, 0, 80, 16, 16, 16, 0)

        pyxel.blt(65, 65, 0, 80, 0, 16, 16, 0)
        pyxel.blt(85, 65, 0, 80, 16, 16, 16, 0)
        pyxel.blt(100, 55, 0, 80, 16, 16, 16, 0)

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

        # candles brick
        pyxel.blt(25, 40, 0, 0, 32, 20, 35, 0)

        pyxel.blt(50, 45, 0, 0, 32, 20, 35, 0)

        pyxel.blt(75, 40, 0, 0, 32, 20, 35, 0)

        pyxel.blt(95, 25, 0, 0, 32, 20, 35, 0)

        pyxel.blt(5, 25, 0, 0, 32, 20, 35, 0)

        pyxel.blt(50, 10, 0, 0, 32, 20, 35, 0)

        pyxel.blt(75, 15, 0, 0, 32, 20, 35, 0)

        pyxel.blt(25, 15, 0, 0, 32, 20, 35, 0)

        # fork
        pyxel.blt(5, 150, 0, 64, 48, 16, 64, 0)

        # plate facing player
        pyxel.circ(60, 210, 50, pyxel.COLOR_WHITE)
        pyxel.circb(60, 210, 35, pyxel.COLOR_NAVY)
        
        # spider
        pyxel.line(103, 0, 103, 70, pyxel.COLOR_GRAY)
        pyxel.blt(95, 65, 0, 80, 48, 16, 25, 0)

        pyxel.line(18, 0, 18, 80, pyxel.COLOR_GRAY)
        pyxel.blt(10, 75, 0, 96, 48, 16, 16, 0)

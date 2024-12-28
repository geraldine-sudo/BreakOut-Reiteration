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
        pyxel.blt(25, 40, 0, 0, 32, 20, 25, 0)

        pyxel.blt(50, 45, 0, 0, 32, 20, 25, 0)

        pyxel.blt(75, 40, 0, 0, 32, 20, 25, 0)

        pyxel.blt(95, 25, 0, 0, 32, 20, 25, 0)

        # 2 hits
        pyxel.blt(5, 25, 0, 112, 0, 20, 25, 0)

        pyxel.blt(50, 10, 0, 0, 32, 20, 25, 0)

        # op hits
        pyxel.blt(75, 15, 0, 136, 0, 20, 25, 0)

        pyxel.blt(25, 15, 0, 0, 32, 20, 25, 0)

        # fork
        pyxel.blt(5, 150, 0, 64, 48, 16, 64, 0)

        # plate facing player
        pyxel.circ(60, 210, 50, pyxel.COLOR_WHITE)
        pyxel.circb(60, 210, 35, pyxel.COLOR_NAVY)
        
        # # spider
        # pyxel.line(103, 0, 103, 70, pyxel.COLOR_GRAY)
        # # ball maker
        # pyxel.blt(95, 65, 0, 80, 48, 16, 25, 0)

        # pyxel.line(18, 0, 18, 80, pyxel.COLOR_GRAY)
        # # 3 hits
        # pyxel.blt(10, 75, 0, 96, 48, 16, 16, 0)


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
        # pyxel.blt(18, 115, 0, 32, 120, 16, 16, 0)
        # pyxel.blt(65, 85, 0, 48, 120, 16, 16, 0)
        # pyxel.blt(45, 90, 0, 32, 104, 16, 16, 0)
        # pyxel.blt(25, 75, 0, 16, 120, 16, 16, 0)
        # pyxel.blt(95, 90, 0, 48, 80, 16, 16, 0)


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

        # # 3 hits
        # pyxel.line(14, 0, 14, 40, pyxel.COLOR_BLACK)
        # pyxel.blt(10, 30, 0, 72, 0, 8, 16, 0)

        # # 2 hits
        # pyxel.line(24, 0, 24, 70, pyxel.COLOR_BLACK)
        # pyxel.blt(20, 65, 0, 24, 0, 8, 16, 0)

        # # ball maker
        # pyxel.line(94, 0, 94, 66, pyxel.COLOR_BLACK)
        # pyxel.blt(90, 65, 0, 64, 0, 8, 16, 0)

        # # op hits
        # pyxel.line(104, 0, 104, 40, pyxel.COLOR_BLACK)
        # pyxel.blt(100, 30, 0, 32, 0, 8, 16, 0)

        # other mother
        pyxel.blt(30, 25, 0, 0, 152, 60, 65, 0)

        # text bg
        pyxel.blt(5, 12, 0, 0, 224, 50, 16, 0)

        for x in range(12, 80, 12):
            pyxel.blt(x, 12, 0, 0, 224, 50, 16, 0)

        pyxel.text(10, 15, 'Other Mother craves flesh.', pyxel.COLOR_RED)







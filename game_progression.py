import pyxel
import random

class Start:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):

        random.seed(0)  
        for _ in range(50):
            x = random.randint(0, self.w_layout)
            y = random.randint(0, self.h_layout)
            pyxel.circ(x, y, 1, pyxel.COLOR_WHITE)

        pyxel.circ(60, 65, 50, pyxel.COLOR_LIGHT_BLUE)
        
        pyxel.circ(45, 55, 5, pyxel.COLOR_DARK_BLUE)
        pyxel.circ(80, 55, 5, pyxel.COLOR_DARK_BLUE)

        pyxel.circ(45, 85, 5, pyxel.COLOR_DARK_BLUE)
        pyxel.circ(80, 85, 5, pyxel.COLOR_DARK_BLUE)

        pyxel.elli(-25, 155, 200, 90, pyxel.COLOR_NAVY)

        pyxel.blt(55, 125, 0, 152, 152, 64, 64, 0)
        pyxel.blt(75, 115, 0, 208, 176, 64, 64, 0, None, 2)

        pyxel.text(30, 185, "Press A to Play", pyxel.COLOR_WHITE)

class Pregame:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        pyxel.rect(0, 0, 120, 200, pyxel.COLOR_PEACH)
        pyxel.elli(25, 100, 75, 35, pyxel.COLOR_NAVY)
        pyxel.blt(45, 115, 0, 160, 32, 64, 64, 0, None, 2)
        pyxel.text(15, 30, '"A small price to pay."', pyxel.COLOR_NAVY)
        pyxel.text(35, 40, "Loading Stage...", pyxel.COLOR_NAVY)

class Win:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        pyxel.rect(0, 0, 120, 200, pyxel.COLOR_NAVY)
        pyxel.text(25, 30, '"Veni, vidi, vici"', pyxel.COLOR_WHITE)
        pyxel.text(18, 40, "Press Space to Restart", pyxel.COLOR_WHITE)
        pyxel.circ(60, 110, 50, pyxel.COLOR_YELLOW)
        pyxel.blt(45, 95, 0, 88, 152, 64, 64, 0, None, 2)
        
class GameOver:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        pyxel.rect(0, 0, 120, 200, pyxel.COLOR_BLACK)
        pyxel.text(45, 50, "You Lose", pyxel.COLOR_WHITE)
        pyxel.text(18, 60, "Press Space to Restart", pyxel.COLOR_WHITE)
        pyxel.elli(12, 90, 100, 50, pyxel.COLOR_DARK_BLUE)
        pyxel.blt(53, 100, 0, 160, 0, 16, 16, 0)


class NextStage1_2:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        pyxel.rect(0, 0, 120, 200, pyxel.COLOR_NAVY)
        pyxel.ellib(15, -150, 90, 300, pyxel.COLOR_BROWN)
        pyxel.text(25, 30, '"Out of many, one."', pyxel.COLOR_WHITE)
        pyxel.text(20, 40, "Loading Next Stage...", pyxel.COLOR_WHITE)
        pyxel.blt(45, 145, 0, 128, 224, 32, 32, 0, None, 2)
    

class NextStage2_3:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        pyxel.rect(0, 0, 120, 200, pyxel.COLOR_WHITE)
        pyxel.text(30, 30, 'acjasbcjiebakn', pyxel.COLOR_RED)
        pyxel.text(25, 40, "Loading Next Stage...", pyxel.COLOR_RED)
        pyxel.circ(60, 125, 50, pyxel.COLOR_GRAY)
        pyxel.blt(45, 115, 0, 104, 112, 32, 32, 0, None, 2)

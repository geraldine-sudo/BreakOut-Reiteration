import pyxel

class GameOver:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        pyxel.rect(0, 0, 120, 200, pyxel.COLOR_WHITE)
        pyxel.text(40, 100, "Game Over", pyxel.COLOR_BLACK)
        pyxel.text(20, 107, "Press space to restart", pyxel.COLOR_BLACK)

class NextStage1_2:
    def __init__(self) -> None:
        self.w_layout = 120
        self.h_layout = 200
        
    def draw(self):
        pyxel.rect(0, 0, 120, 200, pyxel.COLOR_WHITE)
        pyxel.text(40, 100, "Next Level", pyxel.COLOR_BLACK)
        pyxel.text(20, 107, "GyatGyatGyatGyatGyatGyat", pyxel.COLOR_BLACK)
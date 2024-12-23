import pyxel
import json

# dict to json file
# stages = {
#     1: {
#         'hits' : 1,
#         'score': 50,
#         'img': 0,
#         'u' : 32, 
#         'v': 0,
#         'w': 8, 
#         'h': 16
#     }
# }

# pyxel.blt(15, 55, 0, 32, 0, 8, 16)


# store stages in json file
# with open('stages.json', 'w') as f:
#     json.dump(stages, f)

# accessing data from json file
stage = {}

with open('stages.json', 'r') as f:
    stage = json.load(f)

# print(stage['1']['u'])

class Bricks:
    def __init__(self, x: int, y: int, brick_level: str) -> None:
        self.x = x
        self.y = y
        self.brick_level = brick_level

        self.img: int = stage[brick_level]['img']
        self.w: int = stage[brick_level]['w']
        self.h:int = stage[brick_level]['h']

        self.u: int = stage[brick_level]['u']
        self.v: int = stage[brick_level]['v']

    def update(self):
        ...

    def draw(self):
        # print(stage[self.brick_level]['u'])
 
        pyxel.blt(self.x, 
                  self.y, 
                  0, 
                  self.u,
                  self.v,
                  self.w,
                  self.h)

import pyxel
import json

# stages = {1: { 'Stage1': {
#                         "score": 50,
#                         "hits": 1,
#                         "img": 0,
#                         "u": 0,
#                         "v": 32,
#                         "w": 20,
#                         "h": 25
#                         },
#                 'Stage2': {"score": 50,
#                         "hits": 1,
#                         "img": 0,
#                         "u": 48,
#                         "v": 120,
#                         "w": 16,
#                         "h": 16
#                 },
#         2: { 'Stage1': {"score": 100,
#                         "hits": 2,
#                         "img": 0,
#                         "u": 112,
#                         "v": 0,
#                         "w": 20,
#                         "h": 25
#                 },
#             'Stage2': {"score": 100,
#                         "hits": 2,
#                         "img": 0,
#                         "u": 112,
#                         "v": 32,
#                         "w": 16,
#                         "h": 16},
#             'Stage3': {"score": 100,
#                         "hits": 2,
#                         "img": 0,
#                         "u": 24,
#                         "v": 0,
#                         "w": 8,
#                         "h": 16}
#                 },
#         3: { 'Stage1': {"score": 150,
#                             "hits": 3,
#                             "img": 0,
#                             "u": 96,
#                             "v": 48,
#                             "w": 16,
#                             "h": 16
#                     },
#             'Stage2': {"score": 150,
#                         "hits": 3,
#                         "img": 0,
#                         "u": 80,
#                         "v": 104,
#                         "w": 16,
#                         "h": 16},
#             'Stage3': {"score": 150,
#                         "hits": 3,
#                         "img": 0,
#                         "u": 72,
#                         "v": 0,
#                         "w": 8,
#                         "h": 16}
#                     },
#         4: { 'Stage1': {"score": 0,
#                             "hits": -1,
#                             "img": 0,
#                             "u": 136,
#                             "v": 0,
#                             "w": 20,
#                             "h": 25
#                     },
#             'Stage2': {"score": 0,
#                         "hits": -1,
#                         "img": 0,
#                         "u": 128,
#                         "v": 32,
#                         "w": 16,
#                         "h": 16
#                         },
#             'Stage3': {"score": 0,
#                         "hits": -1,
#                         "img": 0,
#                         "u": 32,
#                         "v": 0,
#                         "w": 8,
#                         "h": 16}
#                     },
#         5: { 'Stage1': {"score": 50,
#                             "hits": 1,
#                             "img": 0,
#                             "u": 80,
#                             "v": 48,
#                             "w": 16,
#                             "h": 25
#                     },
#             'Stage2': {"score": 0,
#                         "hits": 1,
#                         "img": 0,
#                         "u": 64,
#                         "v": 104,
#                         "w": 16,
#                         "h": 16
#                         },
#             'Stage3': {"score": 0,
#                         "hits": 1,
#                         "img": 0,
#                         "u": 64,
#                         "v": 0,
#                         "w": 8,
#                         "h": 16}
#                     }

# }}

# store stages in json file
# with open('stages.json', 'w') as f:
#     json.dump(stages, f)
stage = {}

with open('stages.json', 'r') as f:
    stage = json.load(f)

# reach into data
# print(stage['1']['Stage1']['u'])

class Bricks:
    def __init__(self, x: int, y: int, brick_level: str) -> None:
        self.x = x
        self.y = y
        self.brick_level = brick_level

        # self.img: int = stage[brick_level]['img']
        # self.w: int = stage[brick_level]['w']
        # self.h:int = stage[brick_level]['h']

        # self.u: int = stage[brick_level]['u']
        # self.v: int = stage[brick_level]['v']

    def update(self):
        ...

    def draw(self):
        # print(stage[self.brick_level]['u'])
 
        # pyxel.blt(self.x, 
        #           self.y, 
        #           0, 
        #           self.u,
        #           self.v,
        #           self.w,
        #           self.h, 
        #           0)
        ...

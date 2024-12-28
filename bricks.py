import pyxel
import json
from pprint import pprint

# brick_specs = {1: {
#                     "score": 50,
#                     "hits": 1,
#                     "img": 0,
#                     "u": 80,
#                     "v": 64,
#                     "w": 16,
#                     "h": 16
#                     },
#         2: {        "score": 100,
#                     "hits": 2,
#                     "img": 0,
#                     "u": 112,
#                     "v": 64,
#                     "w": 16,
#                     "h": 16
#                },
#         3: {        "score": 150,
#                     "hits": 3,
#                     "img": 0,
#                     "u": 96,
#                     "v": 48,
#                     "w": 16,
#                     "h": 16
#                     },
#         4: {        "score": 0,
#                     "hits": -1,
#                     "img": 0,
#                     "u": 80,
#                     "v": 80,
#                     "w": 16,
#                     "h": 16
#                     },
#         5: {        "score": 0,
#                     "hits": 1,
#                     "img": 0,
#                     "u": 80,
#                     "v": 48,
#                     "w": 16,
#                     "h": 16
#                     }
# }

#store brick specifications in json file
# with open('bricks.json', 'w') as f:
#     json.dump(brick_specs, f)

def access_json(file: str):
    brick = {}

    with open(file+'.json', 'r') as f:
        brick = json.load(f)

    return brick

class Bricks:
    def __init__(self, x: int, y: int,  brick_level: str) -> None:
        brick = access_json('bricks')

        self.x = x 
        self.y = y
        self.brick_level = brick_level

        self.img: int = brick[brick_level]['img'] 
        self.w: int = brick[brick_level]['w'] 
        self.h:int = brick[brick_level]['h'] 

        self.u: int = brick[brick_level]['u']
        self.v: int = brick[brick_level]['v']

    def draw(self):
        pyxel.blt(self.x, 
                  self.y, 
                  self.img, 
                  self.u,
                  self.v,
                  self.w,
                  self.h,
                  0)
        
# stages = {'Stage1': {'brick_placement': 'stage1.json',
#                     'background': ('stages', 'Stage1Map'),
#                     'tile1': ['1', '2', '4']
#                     # make separate condition for ball maker and 3 hits
#                     },
#            'Stage2': {'brick_placement': 'stage2.json',
#                     'background': ('stages', 'Stage2Map'),
#                     'tile1': ['1', '2', '3', '4', '5']
#                     },
#            'Stage3': {'brick_placement': 'stage3.json',
#                     'background': ('stages', 'Stage3Map'),
#                     'tile1': ['1', '2', '3', '4', '5']
#                     # make separate condition for other mother
#                     }}

# store stages in json file
# with open('stages.json', 'w') as f:
#     json.dump(stages, f)

# test

# with open('stage1.json', 'r') as f:
#     for i in f:
#         for j in i:
#             print(j)

# pprint(stage)

def check_levels():
    stage = {}
    with open('stages.json', 'r') as f:
        stage = json.load(f)
    return stage

def load_level(level: str):
    this_level = []
    possible_bricks = ["1", "2", "3", "4", "5"]
    # Load the level file, and read through it, adding bricks to this_level
    with open(level+'.json', 'r') as f:
        y = 0
        for i in f:
            x = 0
            for j in i:
                if j in possible_bricks:
                    this_level.append(Bricks(x, y, j))
                x += 16
            y += 16
    return this_level

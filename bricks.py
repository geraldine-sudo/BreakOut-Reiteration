import pyxel
import json
from pprint import pprint

brick_specs = {1: {
                    "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 80,
                    "v": 64,
                    "w": 16,
                    "h": 16
                    },
        2: {        "score": 100,
                    "hits": 2,
                    "img": 0,
                    "u": 112,
                    "v": 64,
                    "w": 16,
                    "h": 16
               },
        3: {        "score": 150,
                    "hits": 3,
                    "img": 0,
                    "u": 96,
                    "v": 48,
                    "w": 16,
                    "h": 16
                    },
        4: {        "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 80,
                    "v": 80,
                    "w": 16,
                    "h": 16
                    },
        5: {        "score": 0,
                    "hits": 1,
                    "img": 0,
                    "u": 80,
                    "v": 48,
                    "w": 16,
                    "h": 16
                    },
        6: {     "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 96,
                    "v": 80,
                    "w": 16,
                    "h": 16
                    },
        7: {        "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 0,
                    "v": 120,
                    "w": 16,
                    "h": 16
                    }
}

#store brick specifications in json file
with open('bricks.json', 'w') as f:
    json.dump(brick_specs, f)

def access_json(file: str):
    brick = {}

    with open(file+'.json', 'r') as f:
        brick = json.load(f)

    return brick

class Bricks:
    def __init__(self, x: int, y: int, brick_level: str) -> None:
        self.x = x
        self.y = y
        self.brick_level = brick_level
        self.alive = True

        # Load brick data once
        self.brick_data = access_json('bricks')
        self.update_attributes()

    def update_attributes(self):
        """Updates attributes based on the current brick level."""
        brick = self.brick_data.get(self.brick_level, None)

        if brick:
            self.img = brick['img']
            self.w = brick['w']
            self.h = brick['h']
            self.u = brick['u']
            self.v = brick['v']
        else:
            # Handle case where brick_level is invalid
            self.alive = False

    def update(self):
        if self.brick_level == "0":
            self.alive = False
        else:
            self.update_attributes()
            
    def draw(self):
        pyxel.blt(self.x, 
                self.y, 
                self.img, 
                self.u,
                self.v,
                self.w,
                self.h,
                0)
       
stages = {'stage1': {'brick_placement':[['', '1', '1', '', '1', '1', '', '', ''],
                                        ['1', '', '', '5', '', '', '1', '', ''],
                                        ['1', '', '', '', '', '', '1', '', ''],
                                        ['', '1', '', '', '', '1', '', '', ''],
                                        ['', '', '1', '', '1', '', '', '', ''],
                                        ['', '', '', '1', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '6', '6', '6', '', '']]},

            'stage2': {'brick_placement':[['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '3', '', '3', '', '', '', ''],
                                        ['', '1', '', '5', '', '1', '', '', ''],
                                        ['', '', '2', '', '2', '', '2', '', ''],
                                        ['', '2', '', '2', '', '2', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '6', '6', '6', '', '']]},

            'stage3': {'brick_placement':[['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['3', '', '', '', '', '', '3', '', ''],
                                        ['', '', '', '3', '', '', '', '', ''],
                                        ['', '3', '', '', '', '5', '', '', ''],
                                        ['1', '', '1', '', '1', '', '1', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '7', '7', '7', '', '']]}
          }

# store stages in json file
with open('stages.json', 'w') as f:
    json.dump(stages, f)

# test

# with open('stages.json', 'r') as f:
#     stage = json.load(f)
#     for i in stage['stage1']['brick_placement']:
#         for j in i:
#             print(j)

# pprint(stage)

# def check_levels():
#     stage = {}
#     with open('stages.json', 'r') as f:
#         stage = json.load(f)
#     return stage

def load_level(level: str, lives: int):
    this_level = []
    lives_display = []

    possible_bricks = ["1", "2", "3", "4", "5"]

    with open('stages.json', 'r') as f:
        stage = json.load(f)
        y = 0
        for i in stage[level]['brick_placement']:
            x = 0
            for j in i:
                if j in possible_bricks:
                    this_level.append(Bricks(x, y, j))
                elif (j == '6' or j == '7') and len(lives_display) < lives:
                    lives_display.append(Bricks(x, y, j))
                x += 16
            y += 16
    return this_level, lives_display


def load_lives(level: str, lives: int):
    this_level_lives = []

    possible_bricks = ["6", "7"]

    with open('stages.json', 'r') as f:
        stage = json.load(f)
        y = 0
        for i in stage[level]['brick_placement']:
            x = 0
            for j in i:
                if j in possible_bricks:
                    this_level_lives.append(Bricks(x, y, j))
                
                x += 16
            y += 16
    return this_level_lives

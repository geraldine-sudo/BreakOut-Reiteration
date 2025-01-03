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
        2.1: {      "score": 100,
                    "hits": 2,
                    "img": 0,
                    "u": 112,
                    "v": 80,
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
        3.1: {        "score": 150,
                    "hits": 3,
                    "img": 0,
                    "u": 96,
                    "v": 64,
                    "w": 16,
                    "h": 16
                    },
        3.2: {        "score": 150,
                    "hits": 3,
                    "img": 0,
                    "u": 112,
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
        5: {        "score": 50,
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
        6.1: {     "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 112,
                    "v": 96,
                    "w": 16,
                    "h": 16
                    },
        6.2: {     "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 152,
                    "v": 80,
                    "w": 7,
                    "h": 7
                    },
        7: {        "score": 0,
                    "hits": -1,
                    "img": 0,
                    "u": 0,
                    "v": 120,
                    "w": 16,
                    "h": 16
                    },
        8: {        "score": 0,
                    "hits": 1,
                    "img": 0,
                    "u": 144,
                    "v": 32,
                    "w": 7,
                    "h": 7
                    },
        8.1: {        "score": 0,
                    "hits": 1,
                    "img": 0,
                    "u": 152,
                    "v": 32,
                    "w": 7,
                    "h": 7
                    },
        8.2: {        "score": 0,
                    "hits": 1,
                    "img": 0,
                    "u": 144,
                    "v": 40,
                    "w": 7,
                    "h": 7
                    },
        8.3: {        "score": 0,
                    "hits": 1,
                    "img": 0,
                    "u": 152,
                    "v": 40,
                    "w": 7,
                    "h": 7
                    },
        9: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 128,
                    "v": 80,
                    "w": 7,
                    "h": 7
                    },
        9.1: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 136,
                    "v": 80,
                    "w": 7,
                    "h": 7
                    },
        9.2: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 128,
                    "v": 88,
                    "w": 7,
                    "h": 7
                    },
        9.3: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 136,
                    "v": 88,
                    "w": 7,
                    "h": 7
                    },
        9.4: {        "score": 50,
                    "hits": 1,
                    "img": 0,
                    "u": 144,
                    "v": 80,
                    "w": 7,
                    "h": 7
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
        self.image = brick_level
        self.hit  = False
        self.alive = True
        self.counted = False

        # Load brick data once
        self.brick_data = access_json('bricks')
        brick = self.brick_data.get(self.image, None)

        if brick:
            self.img = brick['img']
            self.w = brick['w']
            self.h = brick['h']
            self.u = brick['u']
            self.v = brick['v']
            self.hits = brick['hits']


    def update_attributes(self):
        """Updates attributes based on the current brick level."""
        brick = self.brick_data.get(self.image, None)

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
        if self.hit == True and self.brick_level != "4":
            self.hits -= 1
            if self.hits == 0:
                self.alive = False

            if self.alive:
                self.image = str(float(self.image) + 0.1)
                self.update_attributes()

            self.hit = False

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
                                        ['', '4', '', '', '', '4', '', '', ''],
                                        ['1', '', '', '', '', '', '1', '', ''],
                                        ['', '2', '', '', '', '2', '', '', ''],
                                        ['', '3', '', '', '', '5', '', '', ''],
                                        ['3', '', '3', '', '3', '', '3', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '', '', '', '', ''],
                                        ['', '', '', '', '6', '6', '6', '', '']]},
            
            'P': 50,
            'G': 3,
            'X': 20,
            'Q': 5
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


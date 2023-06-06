import pygame
import environment as env


UNIT = 25
SPACE = UNIT/2
NOTALLOW = (3,4,5,6,7,8,9)


class Agent():
    def __init__(self):
        pass
    

def check_collision(x, y, dx, dy, level):
    """
    :param x: center x of the object (ghosts/Pacman)
    :param y: center y of the object (ghosts/Pacman)
    :return move: (bool) True, if next step won't collide; False, if collide
    """
    bd = 0
    if level == 1:
        bd = env.board_1()
    elif level == 2:
        bd = env.board_2()
    elif level == 3:
        bd = env.board_3()
    
    # check if the object is on the screen
    detect = 0
    if dx != 0:
        if dx == 2:  # move right -> detect right edge of the object
            detect = bd[int(y//UNIT)][int((x+SPACE+dx)//UNIT)]
        elif dx == -2:  # move left
            detect = bd[int(y//UNIT)][int((x-SPACE+dx)//UNIT)]
    elif dy != 0:
        if dy == -2:  # move up -> detect upper bound
            detect = bd[int((y+dy-SPACE)//UNIT)][int(x//UNIT)]
        elif dy == 2:  # move down -> detect lower bound
            detect = bd[int((y+dy+SPACE)//UNIT)][int(x//UNIT)]
    
    if detect in NOTALLOW:
        return False
    return True
    # for i in range(-22, 44, 22):
    #     for j in range(-22, 44, 22):
    #         coord = bd[(y+dy+i)//UNIT][(x+dx+j)//UNIT]
    #         if coord in NOTALLOW:
    #             return False
    # return True
    
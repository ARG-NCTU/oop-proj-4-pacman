import pygame
# from environment import Board


UNIT = 25
SPACE = UNIT/2
NOTALLOW = (3,4,5,6,7,8,9)


class Agent():
    def __init__(self):
        pass

    
def current_coord(x, y):
    """return current coordinate"""
    return (int(y//UNIT), int(x//UNIT))


def current_coord_content(x, y, cur_board):
    """
    return the object current coordinate content
    :param x: center x of the detecting object
    :param y: center y of the detecting object
    :return: (int) map object of the current coord
    """
    return cur_board[int(y//UNIT)][int(x//UNIT)][0]


def check_collision(x, y, dx, dy):
    """
    :param x: center x of the object (ghosts/Pacman)
    :param y: center y of the object (ghosts/Pacman)
    :return move: (bool) True, if next step won't collide; False, if collide
    """
    # check if the object moving direction is movable
    detect = 0
    if dx != 0:
        if dx == 2:  # move right -> detect right edge of the object
            detect = bd[int(y//UNIT)][int((x+SPACE+dx)//UNIT)][0]
        elif dx == -2:  # move left
            detect = bd[int(y//UNIT)][int((x-SPACE+dx)//UNIT)][0]
    elif dy != 0:
        if dy == -2:  # move up -> detect upper bound
            detect = bd[int((y+dy-SPACE)//UNIT)][int(x//UNIT)][0]
        elif dy == 2:  # move down -> detect lower bound
            detect = bd[int((y+dy+SPACE)//UNIT)][int(x//UNIT)][0]
    
    if detect in NOTALLOW:
        return False
    return True

def find_best_route(board, depart, dest):
    """
    :param board:
    :param depart: the departure board index, in the form of [x, y]
    :param dest: destination (target) board index
    :return bestmove: a list contain the best route for next move
    """
    # if destination and deaprture have a same soord, return a blank list
    # if depart[0] == dest[0] and 
    pass

def can_move(x, y):
    """

    """
    # choose the board according to level
    bd = board.get_board()
    
    # check if the object moving direction is movable
    canMove = []
    if bd[int((y-2-SPACE)//UNIT)][int(x//UNIT)] in NOTALLOW:
        canMove.append(0)
    else:
        canMove.append(1)
    if bd[int((y+2+SPACE)//UNIT)][int(x//UNIT)] in NOTALLOW:
        canMove.append(0)
    else:
        canMove.append(1)
    if bd[int(y//UNIT)][int((x-SPACE-2)//UNIT)] in NOTALLOW:
        canMove.append(0)
    else:
        canMove.append(1)
    if bd[int(y//UNIT)][int((x+SPACE+2)//UNIT)] in NOTALLOW:
        canMove.append(0)
    else:
        canMove.append(1)
    return canMove
    
    """
    # detect the direction(s) that can turn and save in a list
    can_move = []  # [U, D, L, R]
    coord = (int(centery//UNIT), int(centerx//UNIT))  # the coord which the object middle at (y,x)
    for i in range(-1, 3, 2):
        if coord[0]+i < (len(bd)-1):
            if bd[coord[0]+i][coord[1]] not in NOTALLOW:
                can_move.append(0)
            else:
                can_move.append(1)
        else:
            can_move.append(0)
        
    for i in range(-1, 3, 2):
        if coord[1]+i < len(bd[0])-1: 
            if bd[coord[0]][coord[1]+i] not in NOTALLOW:
                can_move.append(0)
            else:
                can_move.append(1)
        else:
            can_move.append(0)
    print(can_move)
    return can_move
    """

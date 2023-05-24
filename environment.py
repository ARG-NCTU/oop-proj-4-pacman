import pygame


BLUE = (0,0,255)
"""
0: space inside the block
1: horizontal line
2: vertical line
3: intersection
"""

def board_1():
    board = ((0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0))
    return board


def board_2():
    pass


def board_3():
    """setup of level 3 environment"""
    pass


def draw_environment(screen, width, height, level):
    # choose the correct board correlation with the level
    if level == 1:
        board  = board_1()
    elif level == 2:
        board = board_2()
    else:
        board = board_3()

    coeff_x = (width//len(board[0]))
    coeff_y = ((height)//len(board[0])+2)
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == 1:  #horizontal line
                pygame.draw.line(screen, BLUE , [j*coeff_x, i*coeff_y], [j*coeff_x+coeff_x,i*coeff_y], 3)
                pygame.draw.line(screen, BLUE, [j*coeff_x, i*coeff_y+coeff_y], [j*coeff_x+coeff_x, i*coeff_y+coeff_y], 3)
            elif item == 2:  #vertical line
                pygame.draw.line(screen, BLUE , [j*coeff_x, i*coeff_y], [j*coeff_x,i*coeff_y+coeff_y], 3)
                pygame.draw.line(screen, BLUE , [j*coeff_x+coeff_x, i*coeff_y], [j*coeff_x+coeff_x,i*coeff_y+coeff_y], 3) 

            
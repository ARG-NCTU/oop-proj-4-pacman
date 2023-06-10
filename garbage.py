"""
0: space inside the block
1: horizontal line
2: vertical line
3: intersection
"""

def board_1():
    """
    setup of 1st level environment
    18 rows, 25 columns
    """
    board = [[0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1,1,1],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1,1,1],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1,1,1],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1,1,1],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0],
            [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0]]
    return board


def board_2():
    """setup of level 2 environment"""
    board = [[0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0],
            [0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0]]


def board_3():
    """setup of level 3 environment"""
    """
    0: empty space, 1: dot, 2: big dot, 3: vertical line, 4: horizontal line
    5: top right, 6: top left, 7: bot_left corner, 8 = bot_right corner
    9: gate
    """
    boards = [
        [6,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5],
        [3,6,4,4,4,4,4,4,4,4,4,4,4,4,5,6,4,4,4,4,4,4,4,4,4,4,4,4,5,3],
        [3,3,1,1,1,1,1,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,3,3],
        [3,3,1,6,4,4,5,1,6,4,4,4,5,1,3,3,1,6,4,4,4,5,1,6,4,4,5,1,3,3],
        [3,3,2,3,0,0,3,1,3,0,0,0,3,1,3,3,1,3,0,0,0,3,1,3,0,0,3,2,3,3],
        [3,3,1,7,4,4,8,1,7,4,4,4,8,1,7,8,1,7,4,4,4,8,1,7,4,4,8,1,3,3],
        [3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],
        [3,3,1,6,4,4,5,1,6,5,1,6,4,4,4,4,4,4,5,1,6,5,1,6,4,4,5,1,3,3],
        [3,3,1,7,4,4,8,1,3,3,1,7,4,4,5,6,4,4,8,1,3,3,1,7,4,4,8,1,3,3],
        [3,3,1,1,1,1,1,1,3,3,1,1,1,1,3,3,1,1,1,1,3,3,1,1,1,1,1,1,3,3],
        [3,7,4,4,4,4,5,1,3,7,4,4,5,0,3,3,0,6,4,4,8,3,1,6,4,4,4,4,8,3],
        [3,0,0,0,0,0,3,1,3,6,4,4,8,0,7,8,0,7,4,4,5,3,1,3,0,0,0,0,0,3],
        [3,0,0,0,0,0,3,1,3,3,0,0,0,0,0,0,0,0,0,0,3,3,1,3,0,0,0,0,0,3],
        [8,0,0,0,0,0,3,1,3,3,0,6,4,4,9,9,4,4,5,0,3,3,1,3,0,0,0,0,0,7],
        [4,4,4,4,4,4,8,1,7,8,0,3,0,0,0,0,0,0,3,0,7,8,1,7,4,4,4,4,4,4],
        [0,0,0,0,0,0,0,1,0,0,0,3,0,0,0,0,0,0,3,0,0,0,1,0,0,0,0,0,0,0],
        [4,4,4,4,4,4,5,1,6,5,0,3,0,0,0,0,0,0,3,0,6,5,1,6,4,4,4,4,4,4],
        [5,0,0,0,0,0,3,1,3,3,0,7,4,4,4,4,4,4,8,0,3,3,1,3,0,0,0,0,0,6],
        [3,0,0,0,0,0,3,1,3,3,0,0,0,0,0,0,0,0,0,0,3,3,1,3,0,0,0,0,0,3],
        [3,0,0,0,0,0,3,1,3,3,0,6,4,4,4,4,4,4,5,0,3,3,1,3,0,0,0,0,0,3],
        [3,6,4,4,4,4,8,1,7,8,0,7,4,4,5,6,4,4,8,0,7,8,1,7,4,4,4,4,5,3],
        [3,3,1,1,1,1,1,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,3,3],
        [3,3,1,6,4,4,5,1,6,4,4,4,5,1,3,3,1,6,4,4,4,5,1,6,4,4,5,1,3,3],
        [3,3,1,7,4,5,3,1,7,4,4,4,8,1,7,8,1,7,4,4,4,8,1,3,6,4,8,1,3,3],
        [3,3,2,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,1,1,2,3,3],
        [3,7,4,5,1,3,3,1,6,5,1,6,4,4,4,4,4,4,5,1,6,5,1,3,3,1,6,4,8,3],
        [3,6,4,8,1,7,8,1,3,3,1,7,4,4,5,6,4,4,8,1,3,3,1,7,8,1,7,4,5,3],
        [3,3,1,1,1,1,1,1,3,3,1,1,1,1,3,3,1,1,1,1,3,3,1,1,1,1,1,1,3,3],
        [3,3,1,6,4,4,4,4,8,7,4,4,5,1,3,3,1,6,4,4,8,7,4,4,4,4,5,1,3,3],
        [3,3,1,7,4,4,4,4,4,4,4,4,8,1,7,8,1,7,4,4,4,4,4,4,4,4,8,1,3,3],
        [3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3],
        [3,7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8,3],
        [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,8]
         ]
    # bdWithIntersect = ifIntersect(boards)   
    return boards


# def draw_environment(screen, level):
#     # choose the correct board correlation with the level
#     board = 0
#     if level == 1:
#         board  = board_1()
#     elif level == 2:
#         board = board_2()
#     else:
#         bd = Board()
#         board = bd.get_board()
#     coeff_x = 25
#     coeff_y = 25
#     # coeff_x = width//len(board[0])
#     # coeff_y = (height-50)//len(board)
#     # for i, row in enumerate(board):
#     #     for j, item in enumerate(row):
#     #         if item == 1:  #horizontal line
#     #             pygame.draw.line(screen, BLUE , [j*coeff_x, i*coeff_y], [j*coeff_x+coeff_x,i*coeff_y], 3)
#     #             pygame.draw.line(screen, BLUE, [j*coeff_x, i*coeff_y+coeff_y], [j*coeff_x+coeff_x, i*coeff_y+coeff_y], 3)
#     #         elif item == 2:  #vertical line
#     #             pygame.draw.line(screen, BLUE , [j*coeff_x, i*coeff_y], [j*coeff_x,i*coeff_y+coeff_y], 3)
#     #             pygame.draw.line(screen, BLUE , [j*coeff_x+coeff_x, i*coeff_y], [j*coeff_x+coeff_x,i*coeff_y+coeff_y], 3)        
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             coord = board[i][j][0]  # if coord == 0: blank space
#             if coord == 1:  # the small dot
#                 pygame.draw.circle(screen, WHITE, (j*coeff_x+coeff_x//2, i*coeff_y+coeff_y//2), 4)
#             elif coord == 2:  # the bog dot
#                 pygame.draw.circle(screen, WHITE, (j*coeff_x+coeff_x//2, i*coeff_y+coeff_y//2), 10)
#             elif coord == 3:  # verticle line
#                 pygame.draw.line(screen, BLUE, (j*coeff_x+coeff_x//2, i*coeff_y), 
#                                  (j*coeff_x+coeff_x//2, (i+1)*coeff_y), 3)
#             elif coord == 4:  # horizontal line
#                 pygame.draw.line(screen, BLUE, (j*coeff_x, (i+0.5)*coeff_y), 
#                                  ((j+1)*coeff_x, (i+0.5)*coeff_y), 3)
#             elif coord == 5:  # the top right arc of a block  (x, y, width, height)
#                 pygame.draw.arc(screen, BLUE, (j*coeff_x-(coeff_x*0.4)-2, i*coeff_y+coeff_x//2-2, coeff_x, coeff_y),
#                                 0, PI/2, 3)
#             elif coord == 6:  # the top left arc of a block
#                 pygame.draw.arc(screen, BLUE, (j*coeff_x+(coeff_x*0.5), i*coeff_y+(coeff_x//2)-2, coeff_x, coeff_y),
#                                 PI/2, PI, 3)
#             elif coord == 7:  # the bottom left
#                 pygame.draw.arc(screen, BLUE, (j*coeff_x+coeff_x//2, i*coeff_y-0.4*coeff_y, coeff_x, coeff_y), 
#                                 PI, 3*PI/2, 3)
#             elif coord == 8:  # the bottom right
#                 pygame.draw.arc(screen, BLUE, 
#                                 (j*coeff_x-(coeff_x*0.4)-2, i*coeff_y-0.4*coeff_y, coeff_x, coeff_y),
#                                 3*PI/2, 2*PI, 3)
#             elif coord == 9:  # the gate
#                 pygame.draw.line(screen, WHITE, (j*coeff_x, (i+0.5)*coeff_y), ((j+1)*coeff_x, (i+0.5)*coeff_y), 3)

# # check if it is at an intersrction
        # canMove = agent.can_move(self.rect.centerx, self.rect.centery, 3)
        # if (canMove[0]+canMove[1]) * (canMove[2]+canMove[3]) and \
        #     agent.current_coord(self.rect.centery, self.rect.centerx) != self.bd_coord:
        #     self.bd_coord = agent.current_coord(self.rect.centery, self.rect.centerx)
        #     turn = random.randrange(0, 4)
        #     # random choose the direction when encounter a hinder
        #     direction = random.randrange(0, 4)
        #     if direction == 0 and canMove[0]:
        #         self.dx = 0
        #         self.dy = -2
        #     elif direction == 1 and canMove[1]:
        #         self.dx = 0
        #         self.dy = 2
        #     elif direction == 2 and canMove[2]:
        #         self.dx = -2
        #         self.dy = 0
        #     elif direction == 3 and canMove[3]:
        #         self.dx = 2
        #         self.dy = 0
        # else:  # simply moving toward the same direction
        #     self.rect.x += self.dx
        #     self.rect.y += self.dy


# # check collision first
# move = agent.check_collision(
#     self.rect.centerx, self.rect.centery, self.dx, self.dy, 3)

# # if return True -> update position
# if move:
#     self.rect.x += self.dx
#     self.rect.y += self.dy
# else:  # change moving direction or stop
#     # random choose the direction when encounter a hinder
#     direction = random.choice(("left","right","up","down"))
#     if direction == "left" and self.dx == 0:
#         self.dx = -2
#         self.dy = 0
#     elif direction == "right" and self.dx == 0:
#         self.dx = 2
#         self.dy = 0
#     elif direction == "up" and self.dy == 0:
#         self.dx = 0
#         self.dy = -2
#     elif direction == "down" and self.dy == 0:
#         self.dx = 0
#         self.dy = 2



# if intersected:
    #     if direction == 0 and turns_allowed[0]:
    #         self.dy = -self.player_speed
    #         self.dx = 0
    #     elif direction == 1 and turns_allowed[1]:
    #         self.dy = self.player_speed
    #         self.dx = 0
    #     if direction == 2 and turns_allowed[2]:
    #         self.dx = -self.player_speed
    #         self.dy = 0
    #     elif direction == 3 and turns_allowed[3]:
    #         self.dx = self.player_speed
    #         self.dy = 0
    # else:
    #     if self.dx:
    #         if direction == 2 and turns_allowed[2]:
    #             self.dx = -self.player_speed
    #             self.dy = 0
    #         elif direction == 3 and turns_allowed[3]:
    #             self.dx = self.player_speed
    #             self.dy = 0
    #     elif self.dy:
    #         if direction == 0 and turns_allowed[0]:
    #             self.dy = -self.player_speed
    #             self.dx = 0
    #         elif direction == 1 and turns_allowed[1]:
    #             self.dy = self.player_speed
    #             self.dx = 0
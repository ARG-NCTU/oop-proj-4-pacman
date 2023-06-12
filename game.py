import pygame
# from player import Player
from ghost import *
from player import *
import environment as env
import time
UNIT = 30
SPACE = UNIT//2

FPS = 30
UNIT_SQUARE = 25
BOARD = env.originalBoard
SCREEN_WIDTH = UNIT_SQUARE*len(BOARD[0])
SCREEN_HEIGHT = UNIT_SQUARE*len(BOARD)+50
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

# global variable
counter = 0 #數讓pacman張嘴巴


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PACMAN')
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)

# create ghosts
pinky = Ghost("pink",UNIT_SQUARE*2.5,30.5*UNIT_SQUARE,0,-2, "bfs")
blue = Ghost("blue",UNIT_SQUARE*14.5,15.5*UNIT_SQUARE,2,0, "bfs")
red = Ghost("red",UNIT_SQUARE*27.5,2.5*UNIT_SQUARE,-2,0, "ud_prior")
orange = Ghost("orange", UNIT_SQUARE*15.5, 15.5*UNIT_SQUARE, 0, -2, "random")
ghosts = [pinky, blue, red, orange]

# create player
player = Player(UNIT_SQUARE*15,24*UNIT_SQUARE, 2, 0) #傳左上角畫
#turns_allowed = player.check_position(player.player_x, player.player_y, player.direction)
player.direction = 2

# game loop
direction_command = 0
is_running = False
moving = True

board = env.Board()
# print(len(board.board))

if is_running == False: 
#draw ini 畫初始圖 
    for i in range(len(ghosts)): 
        ghost = ghosts[i]
        ghost.draw(screen) 
    canMove = [0,0,0,0] 
    player.draw(counter, screen, canMove) 
    board = env.Board() 
    board.draw_score_and_lives(screen, font) 
    board.draw_environment(screen) 
    board.draw_game_over_or_won(screen, font) 
    pygame.display.flip()
    
while is_running == False:
    time.sleep(1) # 停1秒
    is_running = True 


while is_running:
    screen.fill(BLACK)
    counter += 1
    
    # update environment
    counter_for_quit = 0
    ate = board.detect_eat(player.player_x + SPACE, player.player_y + SPACE)
    board.draw_score_and_lives(screen, font)
    board.draw_environment(screen)
    board.draw_game_over_or_won(screen, font)
    moving = board.draw_game_over_or_won(screen, font) 
    

    if moving:
        # update ghosts
        for i in range(len(ghosts)):
            ghost = ghosts[i]
            if ate == 2:
                ghost.set_attacked()
            # check if pacman touch ghost
            touched = board.ifTouched(player.player_x, player.player_y, ghost.rect.centerx, ghost.rect.centery, ghost._attacked)
            #如果pcaman碰到鬼 座標重設（重頭開始）
            if touched == True: 
                pinky = Ghost("pink",UNIT_SQUARE*2.5,30.5*UNIT_SQUARE,0,-2, "bfs")
                blue = Ghost("blue",UNIT_SQUARE*14.5,15.5*UNIT_SQUARE,2,0, "bfs")
                red = Ghost("red",UNIT_SQUARE*27.5,2.5*UNIT_SQUARE,-2,0, "ud_prior")
                orange = Ghost("orange", UNIT_SQUARE*15.5, 15.5*UNIT_SQUARE, 0, -2, "random")
                ghosts = [pinky, blue, red, orange]
                player = Player(UNIT_SQUARE*14.5,23.5*UNIT_SQUARE, 1, 0)
                player.direction = 2
                for i in range(len(ghosts)):
                    ghost = ghosts[i]
                    ghost.draw(screen)
                canMove = [0,0,0,0]
                player.draw(counter, screen, canMove)
                pygame.display.flip()
                time.sleep(1)  #停1秒


            # determine whether the object need to makes turn, it must in the area of the unit square center
            intersect = board.ifIntersect(ghost.rect.centerx, ghost.rect.centery)
            collision = board.ifCollision(ghost.rect.centerx, ghost.rect.centery, ghost.dx, ghost.dy)
            if intersect or collision:
                ghost_coord = board.current_coord(ghost.rect.centerx, ghost.rect.centery)  # (y, x)
                player_coord = board.current_coord(player.player_x+SPACE, player.player_y+SPACE, player.dx, player.dy)
                if not ghost._attacked:
                    next_step = board.bfs_setdir(ghost_coord, player_coord)
                    canMove = board.canMove(ghost.rect.centerx, ghost.rect.centery)
                    ghost.set_dir(next_step, canMove)
                else:
                    next_step = board.bfs_setdir(ghost_coord, (16, 15))  # target is the gate (mid of the board)
                    ghost.set_dir(next_step, canMove)
                    # canMove = board.canMove(ghost.rect.centerx, ghost.rect.centery)
                    # ghost.random_set_dir(canMove)
            ghost.update()
            ghost.draw(screen)
        
        # update players
        player_middle = board.ifMiddle(player.player_x+SPACE, player.player_y + SPACE)
        player_collide = board.ifCollision(player.player_x+SPACE, player.player_y + SPACE, player.dx, player.dy)
        canMove = board.canMove(player.player_x + SPACE, player.player_y + SPACE)  #用中間去測可不可轉
        player.draw(counter, screen, canMove)
        player.update(player.direction, canMove, player_middle, player_collide)  #傳左上角畫

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            is_runnung = False
        #鍵盤控制pacman
        # if player_intersect:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.control = 0
            elif event.key == pygame.K_DOWN:
                player.control = 1
            elif event.key == pygame.K_LEFT:
                player.control = 2
            elif event.key == pygame.K_RIGHT:
                player.control = 3
            
        else:
            player.control = 4
    
   
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

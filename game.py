import pygame
# from player import Player
from ghost import *
from player import *
import environment as env
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
pinky = Ghost("pink",UNIT_SQUARE*2.5,30.5*UNIT_SQUARE,0,-2)
blue = Ghost("blue",UNIT_SQUARE*2.5,2.5*UNIT_SQUARE,2,0)
red = Ghost("red",UNIT_SQUARE*27.5,2.5*UNIT_SQUARE,-2,0)
orange = Ghost("orange", UNIT_SQUARE*27.5, 30.5*UNIT_SQUARE, 0, -2)
ghosts = [pinky, blue, red, orange]

# create player
player = Player(UNIT_SQUARE*14.5,23.5*UNIT_SQUARE, 2, 0) #傳左上角畫
#turns_allowed = player.check_position(player.player_x, player.player_y, player.direction)
player.direction = 2

# game loop
direction_command = 0
is_running = True

board = env.Board()

while is_running:
    screen.fill(BLACK)
    counter += 1
    
    # update environment
    ate = board.detect_eat(player.player_x + SPACE, player.player_y + SPACE)
    board.draw_score_and_lives(screen, font)
    board.draw_environment(screen)
    
    # update ghosts
    for i in range(len(ghosts)):
        ghost = ghosts[i]
        if ate == 2:
            ghost.set_attacked()
        # check if pacman touch ghost
        touched = board.ifTouched(player.player_x, player.player_y, ghost.rect.centerx, ghost.rect.centery)
        intersect = board.ifIntersect(ghost.rect.centerx, ghost.rect.centery)
        collision = board.ifCollision(ghost.rect.centerx, ghost.rect.centery, ghost.dx, ghost.dy)
        # determine whether the object need to makes turn, it must in the area of the unit square center
        if intersect or collision:
            canMove = board.canMove(ghost.rect.centerx, ghost.rect.centery)
            ghost.set_dir(canMove)
        ghost.update()
        ghost.draw(screen)
    
    # update players
    player_intersect = board.ifIntersect(player.player_x+SPACE, player.player_y + SPACE)
    player_collide = board.ifCollision(player.player_x+SPACE, player.player_y + SPACE, player.dx, player.dy)
    canMove = board.canMove(player.player_x + SPACE, player.player_y + SPACE) #用中間去測可不可轉
    player.draw(counter, screen, canMove)
    player.update(player.direction, canMove, player_intersect, player_collide) #傳左上角畫

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
            elif event.key == pygame.K_SPACE and (game_over or game_won):
                powerup = False
        else:
            player.control = 4
    
   
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

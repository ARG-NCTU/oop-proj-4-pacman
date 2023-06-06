import pygame
# from player import Player
from ghost import *
from player import *
import environment as env


FPS = 30
UNIT_SQUARE = 25
BOARD = env.board_3()
SCREEN_WIDTH = UNIT_SQUARE*len(BOARD[0])
SCREEN_HEIGHT = UNIT_SQUARE*len(BOARD)
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PACMAN')
clock = pygame.time.Clock()

# create ghosts
ghosts = pygame.sprite.Group()
pinky = Ghost("pink",UNIT_SQUARE*2.5,30.5*UNIT_SQUARE,0,2)
blue = Ghost("blue",UNIT_SQUARE*2.5,2.5*UNIT_SQUARE,-2,0)
red = Ghost("red",UNIT_SQUARE*27.5,2.5*UNIT_SQUARE,2,0)
orange = Ghost("orange", UNIT_SQUARE*27.5, 30.5*UNIT_SQUARE, 2, 0)
ghosts.add(pinky, blue, red, orange)


# create player
player = Player(450, 663, 2, 2)
turns_allowed = player.check_position(player.player_x, player.player_y, player.direction)

player.direction = 2
# game loop
direction_command = 0
is_running = True
while is_running:
    screen.fill(BLACK)

    # setup environment
    env.draw_environment(screen, WIDTH, HEIGHT, 3)
    
    # update ghosts
    ghosts.update()
    ghosts.draw(screen)
    
    # update players
    player.draw(screen)
    player.move(player.player_x, player.player_y, player.direction)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            is_runnung = False
        #控制鍵盤
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
            if event.key == pygame.K_SPACE and (game_over or game_won):
                powerup = False
        #當放開按鍵之後(按錯了)direction_command就變回原本的方向    
        '''if event.type == pygame.KEYUP:             
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = player.direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = player.direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = player.direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = player.direction '''
    for i in range(4): #######這邊給出direction (下一次的方向) 要在event外
        if direction_command == i and turns_allowed[i]:
            player.direction = i               
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

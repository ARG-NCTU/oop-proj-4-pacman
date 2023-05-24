import pygame
# from player import Player
from ghost import *
import environment

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 950
FPS = 30

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
pinky = Ghost("pink",288,320,0,2)
blue = Ghost("blue",850,0,-2,0)
ghosts.add(pinky)
ghosts.add(blue)


# game loop
is_running = True
while is_running:
    screen.fill(BLACK)

    # setup environment
    environment.draw_environment(screen, SCREEN_WIDTH, SCREEN_HEIGHT, 1)
    
    # update ghosts
    Ghost.update(pinky)
    Ghost.update(blue)
    ghosts.draw(screen)
    blue.draw(screen)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            is_runnung = False
    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

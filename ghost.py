import pygame
import random
import environment
import agent
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 950
UNIT = 30
UNIT = 30
SPACE = UNIT//2

# define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)


class Ghost(pygame.sprite.Sprite):
    def __init__(self, name, x, y, dx, dy):
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        # set the direction of the ghost
        self.dx = dx
        self.dy = dy
        # load image
        self.name = name
        self.img = pygame.image.load("assets/ghost_images/"+self.name+".png").convert_alpha()
        self.image = pygame.transform.scale(self.img, (UNIT+SPACE, UNIT+SPACE))  #resize to a block size
        # (x, y) is the center of the ghost
        self.rect = self.image.get_rect()  #defines position and size of ghost object
        self.rect.center = (x, y)

    def update(self):
        # check collision first
        move = agent.check_collision(
            self.rect.centerx, self.rect.centery, self.dx, self.dy, 3)
        # if return True -> update position
        if move:
            self.rect.x += self.dx
            self.rect.y += self.dy
            if self.rect.right < 0:
                self.rect.left = SCREEN_WIDTH
            elif self.rect.left > SCREEN_WIDTH:
                self.rect.right = 0
            if self.rect.bottom < 0:
                self.top = SCREEN_HEIGHT
            elif self.rect.top > SCREEN_HEIGHT:
                self.rect.bottom = 0
        else:  # change move direction or stop
            # random choose the direction when encounter a hinder
            direction = random.choice(("left","right","up","down"))
            if direction == "left" and self.dx == 0:
                self.dx = -2
                self.dy = 0
            elif direction == "right" and self.dx == 0:
                self.dx = 2
                self.dy = 0
            elif direction == "up" and self.dy == 0:
                self.dx = 0
                self.dy = -2
            elif direction == "down" and self.dy == 0:
                self.dx = 0
                self.dy = 2
        
        
    def draw(self, screen):
        pass
        

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,color,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)


class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the ellipse
        pygame.draw.ellipse(self.image,color,[0,0,width,height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

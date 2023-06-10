import pygame
import random
import environment as env
# import agent
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 950
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
        # load dead image
        self.dead = pygame.image.load("assets/ghost_images/dead.png").convert_alpha()
        self.deadImg = pygame.transform.scale(self.dead, (UNIT+SPACE, UNIT+SPACE))
        # (x, y) is the center of the ghost
        self.rect = self.image.get_rect()  #defines position and size of ghost object
        self.rect.center = (x, y)
        # attacked related attribute
        self._attacked = False
        self._attackedCounter = 0
        self.__attackedTime = 10

    def update(self):
        """
        :param states: (str) 
        """
        if self._attacked:
            self._attackedCounter += 1
        if self._attackedCounter//30 == self.__attackedTime and self._attacked:
            self._attackedCounter = 0
            self._attacked = False
            self.set_target()

        self.rect.x += self.dx
        self.rect.y += self.dy

    def set_dir(self, canMove):
        choice = 0
        dir = 4
        while choice == 0:
            dir = random.randrange(0, 4)
            choice = canMove[dir]
            # print(choice)
        if dir == 0 and self.dy == 0:
            self.dx = 0
            self.dy = -2
        elif dir == 1 and self.dy == 0:
            self.dx = 0
            self.dy = 2
        elif dir == 2 and self.dx == 0:
            self.dx = -2
            self.dy = 0
        elif dir == 3 and self.dx == 0:
            self.dx = 2
            self.dy = 0  

    def set_target(self):
        pass

    def set_attacked(self):
        """
        setter of attacked states
        """
        self._attacked = True

    def draw(self, screen):
        if not self._attacked:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.deadImg, self.rect)
        

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

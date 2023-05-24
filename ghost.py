import pygame  ##hihi
import random
import environment

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 950

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
        # set the direaction of the ghost
        self.dx = dx
        self.dy = dy
        # load image
        self.name = name
        self.img = pygame.image.load("assets/ghost_images/"+self.name+".png").convert_alpha()
        self.image = pygame.transform.scale(self.img, (45, 45))  #resize to a block size
        self.rect = self.image.get_rect()  #defines pos and size of ghost object
        self.rect.topleft = (x, y)

    def update(self):
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

        # random choose the direction when encounter an intersection
        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left","right","up","down"))
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2


    def get_intersection_position(self):
        items = []
        for i, row in enumerate(environment.board_1()):
            for j, item in enumerate(row):
                if item == 3:
                    items.append((j*32,i*32))

            return items
        
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

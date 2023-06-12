import pygame
import random
import environment as env
# import agent
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 875
UNIT = 30
SPACE = UNIT//2

# define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

class Ghost(pygame.sprite.Sprite):
    def __init__(self, name, x, y, dx, dy, algorithm):
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
        self.deadRect = self.deadImg.get_rect()
        self.deadRect.center =  (x,y)
        # attacked related attribute
        self._attacked = False
        self._attackedCounter = 0
        self.__attackedTime = 10
        # moving algorithm
        self.algorithm = algorithm

    def update(self):
        """
        :param states: (str) 
        """
        if self._attacked:
            self._attackedCounter += 1
        if self._attackedCounter//30 == self.__attackedTime and self._attacked:
            self._attackedCounter = 0
            self._attacked = False
            if self.name == "orange" or self.name == "blue":
                self.algorithm = "random"
            if self.name == "red":
                self.algorithm = "ud_prior"
        
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.deadRect.x += self.dx
        self.deadRect.y += self.dy
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = UNIT-10
            self.deadRect.x = UNIT-10
        elif self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH-UNIT+10
            self.rect.x = SCREEN_WIDTH-UNIT+10

    def set_dir(self, next_step, canMove):
        """
        :param target: the target coord (x, y); board[y][x]
        """
        if self.algorithm == "bfs":
            if next_step == 0 and self.dy == 0:
                self.dx = 0
                self.dy = -2
            elif next_step == 1 and self.dy == 0:
                self.dx = 0
                self.dy = 2
            elif next_step == 2 and self.dx == 0:
                self.dx = -2
                self.dy = 0
            elif next_step == 3 and self.dx == 0:
                self.dx = 2
                self.dy = 0
        elif self.algorithm == "ud_prior":
            self.ud_set_dir(canMove, next_step)
        else:
            self.random_set_dir(canMove)

    def ud_set_dir(self, canMove, bfs_next):
        """If at an intersection choose up and down first"""
        x_dir = random.randrange(2, 4)
        if canMove[0] and self.dy == 0:
            self.dx = 0
            self.dy = -2 
        elif canMove[1] and self.dy == 0:
            self.dx = 0
            self.dy = 2
        
        elif x_dir == 2 and canMove[2] and self.dx == 0:
            self.dx = -2
            self.dy = 0
        elif x_dir == 3 and canMove[3] and self.dx == 0:
            self.dx = 2
            self.dy = 0

    def random_set_dir(self, canMove):
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
        """
        0: chase Pacman, 1: attacked, moving to the center of the board
        """
        pass

    def set_attacked(self):
        """
        setter of attacked states
        """
        self._attacked = True
        self.algorithm = "bfs"

    def draw(self, screen):
        if not self._attacked:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.deadImg, self.deadRect)
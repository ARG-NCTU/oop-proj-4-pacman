import pygame
import environment as env

BOARD = env.board_3()

WIDTH = 900
HEIGHT = 950
direction = 0


class Player:
    def __init__(self, player_x, player_y, direction, player_speed):
        self.player_x = player_x
        self.player_y = player_y
        self.direction = 0
        self.player_speed = 2
    
    def draw(self, screen):   #####################################還沒懂
    # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        player_images = []
        for i in range(1, 5):
            player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))
        if self.direction == 0:
            screen.blit(player_images[0], (self.player_x, self.player_y))
        elif self.direction == 1:
            screen.blit(pygame.transform.flip(player_images[0], True, False), (self.player_x, self.player_y))
        elif self.direction == 2:
            screen.blit(pygame.transform.rotate(player_images[0], 90), (self.player_x, self.player_y))
        elif self.direction == 3:
            screen.blit(pygame.transform.rotate(player_images[0], 270), (self.player_x, self.player_y))
        
    def check_position(self, player_x, player_y, direction): #會回傳turn allow[] ：可不可以轉 右 左 上 下
        centerx = self.player_x + 23  # check collisions based on center x and center y of player +/- fudge number
        centery = self.player_y + 24
        turns = [False, False, False, False] 
        num1 = (HEIGHT - 50) // 32
        num2 = (WIDTH // 30)
        num3 = 15
        if centerx // 30 < 29:
            if self.direction == 0:
                if BOARD[centery // num1][(centerx - num3) // num2] < 3:
                    turns[1] = True
            if self.direction == 1:
                if BOARD[centery // num1][(centerx + num3) // num2] < 3:
                    turns[0] = True
            if self.direction == 2:
                if BOARD[(centery + num3) // num1][centerx // num2] < 3:
                    turns[3] = True
            if self.direction == 3:
                if BOARD[(centery - num3) // num1][centerx // num2] < 3:
                    turns[2] = True

            if self.direction == 2 or self.direction == 3:
                if 12 <= centerx % num2 <= 18:
                    if BOARD[(centery + num3) // num1][centerx // num2] < 3:
                        turns[3] = True
                    if BOARD[(centery - num3) // num1][centerx // num2] < 3:
                        turns[2] = True
                if 12 <= centery % num1 <= 18:
                    if BOARD[centery // num1][(centerx - num2) // num2] < 3:
                        turns[1] = True
                    if BOARD[centery // num1][(centerx + num2) // num2] < 3:
                        turns[0] = True
            if self.direction == 0 or self.direction == 1:
                if 12 <= centerx % num2 <= 18:
                    if BOARD[(centery + num1) // num1][centerx // num2] < 3:
                        turns[3] = True
                    if BOARD[(centery - num1) // num1][centerx // num2] < 3:
                        turns[2] = True
                if 12 <= centery % num1 <= 18:
                    if BOARD[centery // num1][(centerx - num3) // num2] < 3:
                        turns[1] = True
                    if BOARD[centery // num1][(centerx + num3) // num2] < 3:
                        turns[0] = True
        else:  #可左右轉
            turns[0] = True
            turns[1] = True

        return turns  #回傳回去變turn allow[]
    
        

    def move(self, player_x, player_y, direction):
        # r, l, u, d
            turns_allowed = [False, False, False, False]
            turns_allowed = self.check_position(self.player_x, self.player_y, self.direction)  #從前面的函式
            if self.direction == 0 and turns_allowed[0]:
                self.player_x += self.player_speed
            elif direction == 1 and turns_allowed[1]:
                self.player_x -= self.player_speed
            if direction == 2 and turns_allowed[2]:
                self.player_y -= self.player_speed
            elif direction == 3 and turns_allowed[3]:
                self.player_y += self.player_speed

            # return self.player_x, self.player_y

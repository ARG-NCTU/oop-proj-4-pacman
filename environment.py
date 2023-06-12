import pygame
# import agent


BLUE = (0,0,255)
WHITE = (255,255,255)
PI = 3.14159
UNIT = 25
SPACE = UNIT/2
NOTALLOW = (3,4,5,6,7,8)


originalBoard = [
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

class Board():
    def __init__(self):
        self.board = self.intersect_map(originalBoard)
        self.score = 0
        self.lives = 3
        self.gameStart = True
        self.game_over = False
        self.game_won = False
        
    def current_coord(self, x, y, dx=0, dy=0):
        """
        :return: (tuple) current coordinate index in the form of (y, x)
        which equals to the spot board[y][x]
        """
        if dx != 0:
            if dx == 2:  # move right -> detect right edge of the object
                return (int(y//UNIT), int((x+SPACE+dx)//UNIT))
            elif dx == -2:  # move left
                return (int(y//UNIT), int((x-SPACE+dx)//UNIT))
        elif dy != 0:
            if dy == -2:  # move up -> detect upper bound
                return (int((y+dy-SPACE)//UNIT), int(x//UNIT))
            elif dy == 2:  # move down -> detect lower bound
                return (int((y+dy+SPACE)//UNIT),int(x//UNIT))
        return (int(y//UNIT), int(x//UNIT))

    def detect_eat(self, obj_x, obj_y):
        """
        detect whether Pacman eat a food.
        :param obj_x: center x of the object
        :param obj_y: center y of the object
        :return ate: (tuple) thing has ate (1: small dot; 2: big dot)
        """
        cur_y, cur_x = self.current_coord(obj_x, obj_y)
        ate = self.board[cur_y][cur_x][0]
        if ate == 1:
            self.board[cur_y][cur_x][0] = 0
            self.score += 10
        elif ate == 2:
            self.board[cur_y][cur_x][0] = 0
            self.score += 50
            #這邊還要加一個鬼會變白(不能吃pacman)
        return ate

    def intersect_map(self, boards):
        """reutrn a new board map with canMove direction list and if intersection"""
        new_board = [[[] for j in range(len(boards[0]))] for i in range(len(boards))]
        for i in range(len(boards)):
            for j in range(len(boards[0])):
                new_board[i][j].append(boards[i][j])
                # check intersection
                canMove = []
                if i-1 >= 0:  # up
                    if boards[i-1][j] in NOTALLOW:
                        canMove.append(0)
                    else:
                        canMove.append(1)
                else:
                    canMove.append(0)
                if i+1 < len(boards):  # down
                    if boards[i+1][j] in NOTALLOW:
                        canMove.append(0)
                    else:
                        canMove.append(1)
                else:
                    canMove.append(0)
                if j-1 > 0:  # left
                    if boards[i][j-1] in NOTALLOW:
                        canMove.append(0)
                    else:
                        canMove.append(1)
                else:
                    canMove.append(0)
                if j+1 < len(boards[0]):  # right
                    if boards[i][j+1] in NOTALLOW:
                        canMove.append(0)
                    else:
                        canMove.append(1)
                else:
                    canMove.append(0)
                # check if intersect
                intersect = False
                if (canMove[0]+canMove[1]) * (canMove[2]+canMove[3]):
                    intersect = True
                new_board[i][j].append(canMove)
                new_board[i][j].append(intersect)
        return new_board

    def ifMiddle(self, obj_x, obj_y):
        """Check in the obj is at the middle of a unit square"""
        if 5 < obj_x%UNIT < 15 and 5 < obj_y%UNIT < 15:
            return True
        return False
    
    def ifIntersect(self, obj_x, obj_y):
        """
        :return: (bool) if the coord is an intersection
        """
        if 5 < obj_x%UNIT < 15 and 5 < obj_y%UNIT < 15:
            cur_y, cur_x = self.current_coord(obj_x, obj_y)
            if self.board[cur_y][cur_x][2]:
                return True
        return False
        
    def ifCollision(self, obj_x, obj_y, dx, dy):
        """
        :param obj_x: center x of the object (ghosts/Pacman)
        :param obj_y: center y of the object (ghosts/Pacman)
        :return: (bool) True, if next step will collide; False, if will not collide
        """
        # check if the object moving direction is movable
        detect = 0
        if dx != 0:
            if dx > 0:  # move right -> detect right edge of the object
                if originalBoard[int(obj_y//UNIT)][int((obj_x+SPACE+dx)//UNIT)] in NOTALLOW:
                    return True
            elif dx < 0:  # move left
                 if originalBoard[int(obj_y//UNIT)][int((obj_x-SPACE+dx)//UNIT)] in NOTALLOW:
                     return True
        elif dy > 0:
            if dy != 0:
                if dy < 0:  # move up -> detect upper bound
                    if originalBoard[int((obj_y-SPACE*2+dy)//UNIT)][int(obj_x//UNIT)] in NOTALLOW:
                        return True
                elif dy > 0:  # move down -> detect lower bound
                    if originalBoard[int((obj_y+SPACE*2+dy)//UNIT)][int(obj_x//UNIT)] in NOTALLOW:
                        return True
        if 5 < obj_x%UNIT < 16:
            if dx != 0:
                if dx > 0:  # move right -> detect right edge of the object
                    detect = originalBoard[int(obj_y//UNIT)][int((obj_x+SPACE+dx)//UNIT)]
                elif dx < 0:  # move left
                    detect = originalBoard[int(obj_y//UNIT)][int((obj_x-SPACE+dx)//UNIT)]
        elif 5 < obj_y%UNIT < 16:
            if dy != 0:
                if dy < 0:  # move up -> detect upper bound
                    detect = originalBoard[int((obj_y-SPACE*2+dy)//UNIT)][int(obj_x//UNIT)]
                elif dy > 0:  # move down -> detect lower bound
                    detect = originalBoard[int((obj_y+SPACE*2+dy)//UNIT)][int(obj_x//UNIT)]
            # print(detect)
        if detect in NOTALLOW:
            return True
        return False

    def ifTouched(self, player_x, player_y, ghost_x, ghost_y, attacked):
        """
        Check if Pacman have touched ghost
        if touched return True, else return Fasle
        """
        if attacked:
            return False
        if self.gameStart:
            if abs(player_x-ghost_x)<UNIT+SPACE and abs(player_y-ghost_y)<UNIT+SPACE:
                self.lives -= 1
                return True
        return False

    def canMove(self, obj_x, obj_y):
        """
        if the direction can move -> 1; if not -> 0
        :return: (lst) contain [U,D,L,R] can move direction
        """
        y, x = self.current_coord(obj_x, obj_y)
        canMove = self.board[y][x][1]
        return canMove

    def draw_score_and_lives(self, screen, font):
    
        """
        update and add score board on the screen
        update and draw the live pac man left
        """
        player_images_forlives = pygame.image.load(f'assets/player_images/1.png')
        score_text = font.render(f'Score: {self.score}', True, (255,255,255))
        screen.blit(score_text, (50, 830))
        for i in range(self.lives):
            screen.blit(pygame.transform.scale(player_images_forlives, (30, 30)), (600+i*50, 830))

    def draw_game_over_or_won(self, screen, font):
    
        """
        draw game over or won
        """

        if self.lives == 0:
            pygame.draw.rect(screen, (255, 255, 255), [50, 300, 650, 300],0, 10)
            pygame.draw.rect(screen, (100,100,100), [70, 320, 610, 260], 0, 10)
            gameover_text = font.render('Game over! ', True, (255,0,0))
            screen.blit(gameover_text, (300, 420))
            return False

        if self.score == 2620:
            pygame.draw.rect(screen, 'white', [50, 300, 650, 300],0, 10)
            pygame.draw.rect(screen, 'dark gray', [70, 320, 610, 260], 0, 10)
            gameover_text = font.render('Victory! ', True, (0,255,255))
            screen.blit(gameover_text, (300, 420))     
            return False
            
        else:
            return True    

    def draw_environment(self, screen):
        coeff_x = 25
        coeff_y = 25

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                coord = self.board[i][j][0]  # if coord == 0: blank space
                if coord == 1:  # the small dot
                    pygame.draw.circle(screen, WHITE, (j*coeff_x+coeff_x//2, i*coeff_y+coeff_y//2), 4)
                elif coord == 2:  # the bog dot
                    pygame.draw.circle(screen, WHITE, (j*coeff_x+coeff_x//2, i*coeff_y+coeff_y//2), 10)
                elif coord == 3:  # verticle line
                    pygame.draw.line(screen, BLUE, (j*coeff_x+coeff_x//2, i*coeff_y), 
                                    (j*coeff_x+coeff_x//2, (i+1)*coeff_y), 3)
                elif coord == 4:  # horizontal line
                    pygame.draw.line(screen, BLUE, (j*coeff_x, (i+0.5)*coeff_y), 
                                    ((j+1)*coeff_x, (i+0.5)*coeff_y), 3)
                elif coord == 5:  # the top right arc of a block  (x, y, width, height)
                    pygame.draw.arc(screen, BLUE, (j*coeff_x-(coeff_x*0.4)-2, i*coeff_y+coeff_x//2-2, coeff_x, coeff_y),
                                    0, PI/2, 3)
                elif coord == 6:  # the top left arc of a block
                    pygame.draw.arc(screen, BLUE, (j*coeff_x+(coeff_x*0.5), i*coeff_y+(coeff_x//2)-2, coeff_x, coeff_y),
                                    PI/2, PI, 3)
                elif coord == 7:  # the bottom left
                    pygame.draw.arc(screen, BLUE, (j*coeff_x+coeff_x//2, i*coeff_y-0.4*coeff_y, coeff_x, coeff_y), 
                                    PI, 3*PI/2, 3)
                elif coord == 8:  # the bottom right
                    pygame.draw.arc(screen, BLUE, 
                                    (j*coeff_x-(coeff_x*0.4)-2, i*coeff_y-0.4*coeff_y, coeff_x, coeff_y),
                                    3*PI/2, 2*PI, 3)
                elif coord == 9:  # the gate
                    pygame.draw.line(screen, WHITE, (j*coeff_x, (i+0.5)*coeff_y), ((j+1)*coeff_x, (i+0.5)*coeff_y), 3)

    def bfs_setdir(self, ghost, target):
        """
        :param ghost_index: (tup) (i, j) == board[j][i]
        :param target_index: (tup) (i,j) == board[j][i]
        """
        q = []
        dist = [[float("inf") for j in range(len(self.board[0]))] for i in range(len(self.board))]
        parent = [[(-2,-2) for j in range(len(self.board[0]))] for i in range(len(self.board))]
        q.append(ghost)
        dist[ghost[0]][ghost[1]] = 0  # the departure point of ghost, dist == 0
        
        while q and parent[target[0]][target[1]] == (-2,-2):
            curr = q.pop(0)
            for i in range(4):
                if self.board[curr[0]][curr[1]][1][i] == 1:  # check if the direction is available
                    neighbor = 0
                    if i == 0:  #up
                        neighbor = (curr[0]-1, curr[1])
                    elif i == 1:  #down
                        neighbor = (curr[0]+1, curr[1])
                    elif i == 2:  # left
                        neighbor = (curr[0], curr[1]-1)
                    elif i == 3:
                        neighbor = (curr[0], curr[1]+1)
                    if parent[neighbor[0]][neighbor[1]] == (-2, -2):  # unvisited
                        dist[neighbor[0]][neighbor[1]] = dist[curr[0]][curr[1]]+1
                        parent[neighbor[0]][neighbor[1]] = curr
                        q.append(neighbor)  # enqueue the front
        if parent[target[0]][target[1]] == (-2,-2):  # if cannot reach
            return False
        else:
            best_route = []
            curr = target
            while curr != ghost:
                best_route.insert(0, curr)
                curr = parent[curr[0]][curr[1]]
            # best_route.insert(0, start)
            if not best_route:
                return False
            next_step = best_route[0]
            direction = 4
            if next_step[1] != ghost[1]:  # x-direction
                if next_step[1] - ghost[1] > 0:
                    direction = 3
                else:
                    direction = 2
            elif next_step[0] != ghost[0]:  # y-direction
                if next_step[0] - ghost[0] > 0:  # down
                    direction = 1
                else:
                    direction = 0
            # print("next step", next_step, "ghost", ghost, "dir", direction)
            return direction

board = Board()
print(board.board)
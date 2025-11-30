import pygame
# import environment as env
import environment
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 950
UNIT = 30
SPACE = UNIT//2
# BOARD = env.board_3()


direction = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y, dx, dy, control=0):
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        self.dx = dx
        self.dy = dy
        self.player_x = player_x
        self.player_y = player_y
        self.direction = 0
        self.player_speed = 2
        self.control = control
        # self.rect = self.image.get_rect()  #defines position and size of ghost object
        # self.rect.center = (player_x, player_y)
    

    def draw(self, counter, screen, canMove):
        if self.control != 4 and canMove[self.control]:
            self.direction = self.control
        # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        counter = counter
        player_images = []
        for i in range(1, 5):
            player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (UNIT+SPACE, UNIT+SPACE)))
        if self.direction == 3:
            screen.blit(player_images[counter%4], (self.player_x-SPACE, self.player_y-SPACE))
        elif self.direction == 2:
            screen.blit(pygame.transform.flip(player_images[counter%4], True, False), (self.player_x-SPACE, self.player_y-SPACE))
        elif self.direction == 0:
            screen.blit(pygame.transform.rotate(player_images[counter%4], 90), (self.player_x-SPACE, self.player_y-SPACE))
        elif self.direction == 1:
            screen.blit(pygame.transform.rotate(player_images[counter%4], 270), (self.player_x-SPACE, self.player_y-SPACE))



    def update(self, direction, canMove, intersected, collision):
        
        #turns_allowed = [False, False, False, False]
        if collision:
            self.dy = 0
            self.dx = 0
        else:
            turns_allowed = canMove
            if direction == 0 and turns_allowed[0]:
                self.dy = -self.player_speed
                self.dx = 0
            elif direction == 1 and turns_allowed[1]:
                self.dy = self.player_speed
                self.dx = 0
            if direction == 2 and turns_allowed[2]:
                self.dx = -self.player_speed
                self.dy = 0
            elif direction == 3 and turns_allowed[3]:
                self.dx = self.player_speed
                self.dy = 0 
        
        self.player_x += self.dx
        self.player_y += self.dy
        
        #走到最左（右）邊要從右（左）邊回來
        if self.player_x >= 700:
            self.player_x = -50
        if self.player_x < -50:
            self.player_x = 700


class ScriptedPlayer(Player):
    """A Player that replays a predetermined list of moves."""

    def __init__(self, player_x, player_y, dx, dy, control=0, move_script=None, loop_script=False):
        super().__init__(player_x, player_y, dx, dy, control)
        self._script = self._validate_script(move_script or [])
        self.loop_script = loop_script
        self._script_index = 0

    def draw(self, counter, screen, canMove):
        self.consume_scripted_move(canMove)
        super().draw(counter, screen, canMove)

    def consume_scripted_move(self, canMove):
        """
        Apply the next scripted move when it is currently allowed.
        :return: bool indicating whether a move from the script was consumed.
        """
        if len(canMove) != 4:
            raise ValueError("canMove must describe exactly four directions.")

        if not self._script:
            self.control = 4
            return False

        if self._script_index >= len(self._script):
            if self.loop_script:
                self._script_index = 0
            else:
                self.control = 4
                return False

        desired_direction = self._script[self._script_index]

        if not canMove[desired_direction]:
            self.control = 4
            return False

        self.control = desired_direction
        self.direction = desired_direction
        self._script_index += 1
        return True

    @staticmethod
    def _validate_script(script):
        for move in script:
            if move not in (0, 1, 2, 3):
                raise ValueError("Scripted moves must be integers between 0 and 3.")
        return list(script)
    
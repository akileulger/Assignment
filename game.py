import pygame,sys,random
from pygame.math import Vector2

# ATTENTION PLEASE !!This .py file includes pixel!! 8 pixel equals to 1 ch !! It will be change !

class Board:
    def __init__(self):
        self.cell_size = 5 # its for 5x5 cell
        self.board_width = 150 
        self.board_height = 150
        self.screen = pygame.display.set_mode((self.cell_size * self.board_width, self.cell_size * self.board_height))
        #self.clock = pygame.time.Clock()
    def print_board(self):
        self.screen.fill(pygame.Color('white'))


class Player:
    def __init__(self, board_width, board_height):
        self.cell_size = 24
        self.x = random.randint(1, board_width - 2)
        self.y = random.randint(1, board_height - 2)
        self.body = [Vector2(self.x,self.y)]
        self.health = 1000
        self.pixel_move = 2 # 2 pixel per one second
        self.wait_time = 500 # 500 ms
        self.last_move_time = pygame.time.get_ticks() # this function find from internet! SORRY :( its from stackoverflow..

    def move(self, dir_x, dir_y):
        now = pygame.time.get_ticks() #this function gets last move time in milliseconds.
        print(now)
        if now - self.last_move_time >= self.wait_time:
            new_x = self.x + dir_x * self.pixel_move # new position for  up, down, left, right.
            new_y = self.y + dir_y * self.pixel_move # new position for  up, down, left, right.
            if 0 <= new_x < board.board_width - 1 and 0 <= new_y < board.board_height - 1: # control for screen border.
                self.x = new_x
                self.y = new_y
                self.last_move_time = now

    def draw_player(self, screen):
        player_rect = pygame.Rect(int(self.x * board.cell_size),int(self.y * board.cell_size),self.cell_size,self.cell_size)
        pygame.draw.rect(screen, pygame.Color('pink'), player_rect)
        board.screen.blit(screen, (0, 0))  

class Enemy :
    def __init__(self,board_width, board_height): 
        #self.cell_size = random.randint(1,5)
        self.cell_size = 24
        self.x = random.randint(1, board_width -2)
        self.y = random.randint(1, board_height -2)
        self.body = [Vector2(self.x,self.y)]
        self.health = self.cell_size
        self.pixel_move = 2 # 2 pixel per one second
        self.wait_time = 500  # 500 ms
        self.last_move_time = pygame.time.get_ticks()
    
    def move(self):
        move_direction = random.choice(["right", "left", "down", "up"])
        now = pygame.time.get_ticks()
        if move_direction == "right":
            if now - self.last_move_time >= self.wait_time:
                new_x = self.x + 1 * self.pixel_move # new position for  right.
                new_y = self.y + 0 * self.pixel_move # new position for  right.
                if 0 <= new_x < board.board_width - 1 and 0 <= new_y < board.board_height - 1: # control for screen border.
                    self.x = new_x
                    self.y = new_y
                    self.last_move_time = now

        elif move_direction == "left":
            if now - self.last_move_time >= self.wait_time:
                new_x = self.x + -1 * self.pixel_move # new position for  right.
                new_y = self.y + 0 * self.pixel_move # new position for  right.
                if 0 <= new_x < board.board_width - 1 and 0 <= new_y < board.board_height - 1:
                    self.x = new_x
                    self.y = new_y
                    self.last_move_time = now
        
        elif move_direction == "down":
            if now - self.last_move_time >= self.wait_time:
                new_x = self.x + 0 * self.pixel_move
                new_y = self.y + 1 * self.pixel_move
                if 0 <= new_x < board.board_width - 1 and 0 <= new_y < board.board_height - 1:
                    self.x = new_x
                    self.y = new_y
                    self.last_move_time = now

        elif move_direction == "up":
            if now - self.last_move_time >= self.wait_time:
                new_x = self.x + 0 * self.pixel_move
                new_y = self.y + -1 * self.pixel_move
                if 0 <= new_x < board.board_width - 1 and 0 <= new_y < board.board_height - 1:
                    self.x = new_x
                    self.y = new_y
                    self.last_move_time = now

    def draw_enemy(self, screen):
        enemy_rect = pygame.Rect(int(self.x * board.cell_size),int(self.y * board.cell_size),self.cell_size,self.cell_size)
        pygame.draw.rect(screen, pygame.Color('blue'), enemy_rect)
        board.screen.blit(screen, (0, 0))  



pygame.init()
board = Board()
player = Player(board.board_width, board.board_height)
enemies = []
for _ in range(10):
    enemy = Enemy(board.board_width, board.board_height)
    enemies.append(enemy)
score_table = [0,0,0,0]
game_over = False

while not game_over:

    if len(enemies) < 10 :
        enemy = Enemy(board.board_width, board.board_height)
        enemies.append(enemy)
    for enemy in enemies :
        enemy.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(0, -1)
                for enemy in enemies :
                    if enemy.body == player.body and enemy.body == player.body:
                        player.health -= 100
                        score_table[0]= player.health
                        game_over = True
            elif event.key == pygame.K_DOWN:
                player.move(0, 1)
                for enemy in enemies :
                    if enemy.body == player.body and enemy.body == player.body:
                        player.health -= 100
                        score_table[1]= player.health
                        game_over = True
            elif event.key == pygame.K_LEFT:
                player.move(-1, 0)
                for enemy in enemies :
                    if enemy.body == player.body and enemy.body == player.body:
                        player.health -= 100
                        score_table[2]= player.health
                        game_over = True
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0)
                for enemy in enemies :
                    if enemy.body == player.body and enemy.body == player.body:
                        player.health -= 100
                        score_table[3]= player.health
                        game_over = True
    score = 0
    for _ in range(4):
        score += score_table[_]
    print(score)
    board.print_board()
    player.draw_player(board.screen)
    for enemy in enemies:
        enemy.draw_enemy(board.screen)
    pygame.display.update()
    #board.clock.tick(60)
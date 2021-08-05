import pygame, sys
from player import Player
from alien import Alien
import obstacle

class Game:
    def __init__(self):
        # Player
        player_sprite = Player((screen_width/2, screen_height), screen_width, screen_height)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Obstacle
        self.shape = obstacle.block_shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_positions = [ num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount) ]
        self.create_obstacles(*self.obstacle_positions, start_x=screen_width/14, start_y=480)
    
        # Alien
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows=6, cols=8)
    
    def alien_setup(self, rows, cols, offset_x=70, offset_y=100, distance_x=60, distance_y=48):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * distance_x + offset_x
                y = row_index * distance_y + offset_y
                alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)

    def create_obstacle(self, start_x, start_y, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = start_x + col_index * self.block_size + offset_x
                    y = start_y + row_index * self.block_size
                    block = obstacle.Block(self.block_size, x, y)
                    self.blocks.add(block)

    def create_obstacles(self, *offset, start_x, start_y):
        for offset_x in offset:
            self.create_obstacle(start_x, start_y, offset_x)              

    def run(self):
        self.player.update()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.blocks.draw(screen)
        self.aliens.draw(screen)

if __name__ == '__main__':
    pygame.init()
    screen_height = 600
    screen_width = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))
        game.run()

        pygame.display.flip()
        clock.tick(60)
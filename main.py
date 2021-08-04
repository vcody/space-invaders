import pygame, sys

pygame.init()
screen_height = 600
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30,30,30))

    pygame.display.flip()
    clock.tick(60)
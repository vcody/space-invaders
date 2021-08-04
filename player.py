import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen_x, screen_y):
        super().__init__()
        self.image = pygame.image.load('./graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 6
        self.screen_x = screen_x
        self.screen_y = screen_y
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.rect.right >= self.screen_x:
                self.rect.right = self.screen_x
            else: self.rect.x += self.speed

        elif keys[pygame.K_LEFT]:
            if self.rect.left <= 0:
                self.rect.left = 0
            else: self.rect.x -= self.speed
    
    def update(self):
        self.get_input()
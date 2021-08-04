import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen_x, screen_y):
        super().__init__()

        self.image = pygame.image.load('./graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 6

        self.screen_x = screen_x
        self.screen_y = screen_y

        self.ready = True
        self.laser_timer = 0
        self.laser_cooldown = 500

        self.lasers = pygame.sprite.Group()
    
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
        
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_timer = pygame.time.get_ticks()
    
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_timer >= self.laser_cooldown:
                self.ready = True
        
    def shoot_laser(self):
        # print('Pew pew pew!')
        self.lasers.add(Laser(self.rect.center, self.rect.bottom))
    
    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()
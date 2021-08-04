import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, screen_y, speed=-10):
        super().__init__()

        self.image = pygame.Surface((4,20))
        self.image.fill('red')

        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.screen_y = screen_y

    def destroy_laser(self):
        if self.rect.y <= -50 or self.rect.y >= self.screen_y + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy_laser()
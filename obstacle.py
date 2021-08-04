import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()

        self.image = pygame.Surface((size,size))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft=(x,y)) 

block_shape = [ 
    'xxxxxxxxxx',
    'xxxxxxxxxx',
    'xxxxxxxxxx',
    'xxxx  xxxx',
    'xxx    xxx',
    'xx      xx'
]

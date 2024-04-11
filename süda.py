import pygame.sprite

class Süda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("süda.png").convert_alpha(), (10, 10))
        self.rect = self.image.get_rect(up=(300, 100))


import pygame.sprite

class Süda(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("süda.png").convert_alpha(), (50, 50))
        self.rect = self.image.get_rect(center=(x, y))

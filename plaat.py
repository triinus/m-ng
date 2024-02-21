import pygame.sprite

class Plaat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("plaat.png").convert_alpha(), (50,50))
        self.rect = self.image.get_rect(center=(200, 200))

    def kuku(self):
        self.rect.x += 5
        self.rect.y += 5

    def update(self):
        self.kuku()
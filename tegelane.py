import pygame.sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("player.png").convert_alpha(), (150, 150))
        self.rect = self.image.get_rect(bottomleft=(400, 450))

    def liigub(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP6]:
            self.rect.y -= 10
            self.rect.x += 10

        if keys[pygame.K_KP3]:
            self.rect.x += 10

        if keys[pygame.K_KP4]:
            self.rect.x -= 10
            self.rect.y -= 10

        if keys[pygame.K_KP1]:
            self.rect.x -= 10

    def uuendab(self):
        self.liigub()

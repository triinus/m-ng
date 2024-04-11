import pygame.sprite

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("tegelaneOtse.png").convert_alpha(), (100, 125))
        self.rect = self.image.get_rect(bottomleft=(400, 500))

    def liigub(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.image = pygame.transform.scale(pygame.image.load("tegelaneParem.png").convert_alpha(), (125, 125))
            if self.rect.x < 600:
                self.rect.x += 10

        if keys[pygame.K_LEFT]:
            self.image = pygame.transform.scale(pygame.image.load("tegelaneVasak.png").convert_alpha(), (125, 125))
            if self.rect.x > 200:
                self.rect.x -= 10


    def update(self):
        self.liigub()
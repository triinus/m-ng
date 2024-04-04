
import pygame.sprite

class Plaat(pygame.sprite.Sprite):
    def __init__(self,vasaküleval, paremüleval, vasakall, paremall):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("plaat.png").convert_alpha(), (50, 50))

        self.paremall = paremall
        self.vasaküleval = vasaküleval
        self.vasakall = vasakall
        self.paremüleval = paremüleval

        if vasaküleval:
            self.rect = self.image.get_rect(center=(200, 200))
        if paremüleval:
            self.rect = self.image.get_rect(center=(600, 200))
        if vasakall:
            self.rect = self.image.get_rect(center=(200, 300))
        if paremall:
            self.rect = self.image.get_rect(center=(600, 300))

    def kuku(self):

        if self.vasaküleval or self.vasakall:
            self.rect.x += 5
            self.rect.y += 5

        if self.paremüleval or self.paremall:
            self.rect.x -= 5
            self.rect.y += 5

    def update(self):
        self.kuku()
        self.hävine()

    def hävine(self):
        if self.rect.y > 300:
            self.kill()

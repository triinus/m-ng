import pygame.sprite

class Plaat(pygame.sprite.Sprite):
    def __init__(self,screen ,vasaküleval, paremüleval, vasakall, paremall):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("plaat.png").convert_alpha(), (50, 50))
        self.mängläbi = pygame.transform.scale(pygame.image.load("lõpp.jpg").convert_alpha(), (968, 548))
        self.screen = screen

        self.paremall = paremall
        self.vasaküleval = vasaküleval
        self.vasakall = vasakall
        self.paremüleval = paremüleval

        if vasaküleval:
            self.rect = self.image.get_rect(center=(150, 100))
        if paremüleval:
            self.rect = self.image.get_rect(center=(750, 100))
        if vasakall:
            self.rect = self.image.get_rect(center=(150, 200))
        if paremall:
            self.rect = self.image.get_rect(center=(750, 200))

    def kuku(self):

        if self.vasaküleval or self.vasakall:
            self.rect.x += 3
            self.rect.y += 5

        if self.paremüleval or self.paremall:
            self.rect.x -= 3
            self.rect.y += 5

    def update(self, südamed):
        self.kuku()
        self.hävine(südamed)

    def hävine(self, südamed):
        if self.rect.y > 500:
            self.kill()
            if len(südamed) <= 1:
                self.screen.blit(self.mängläbi, (0, 0))
                pygame.display.flip()
                pygame.time.delay(5000)
                pygame.quit()
                sys.exit()
            for süda in südamed:
                süda.kill()
                break

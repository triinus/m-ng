import pygame
pygame.init()
screen = pygame.display.set_mode((968, 548))

suda = pygame.image.load('suda.jpg')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    def suda(x, y):
        gameDisplay.blit(suda, (x, y))
        pygame.display.update()
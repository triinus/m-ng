import pygame
from tegelane import Player
from plaat import Plaat

pygame.init()
screen = pygame.display.set_mode((968, 548))
clock = pygame.time.Clock()

plaat = pygame.sprite.GroupSingle()
plaat.add(Plaat())

player = pygame.sprite.GroupSingle()
player.add(Player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")

    plaat.draw(screen)
    plaat.update()

    player.draw(screen)
    player.update()

    pygame.display.update()
    clock.tick(60)

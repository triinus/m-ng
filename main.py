import pygame
from tegelane import Player
from plaat import Plaat
from random import randint, choice
red = (255, 0, 0)

def plaat_movement(plaat_list):
    if plaat_list:
        for plaat_rect in plaat_list:
            plaat_rect.x -= 5

            if plaat_rect.bottom == 300:
                screen.blit(Plaat.kuku, plaat_rect)
            else:
                screen.blit(Plaat.kuku, plaat_rect)

        plaat_list = [plaat for plaat in plaat_list if plaat.x > -100]

        return plaat_list
    else:
        return []

pygame.init()
screen = pygame.display.set_mode((968, 548))
clock = pygame.time.Clock()

plaat = pygame.sprite.GroupSingle()

player = pygame.sprite.GroupSingle()
player.add(Player())

aeg = randint(500, 3000)

plaat_1 = Plaat(True, False, False, False)
plaat_2 = Plaat(False, True, False, False)
plaat_3 = Plaat(False, False, True, False)
plaat_4 = Plaat(False, False, False, True)
plaadidStartPositsioon= ["v-y", "v-a", "p-y", "p-a"]

plaat_group = pygame.sprite.Group()

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, aeg)

game_active = False

punktid = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == obstacle_timer:
            suvalineAsukoht = choice(plaadidStartPositsioon)
            if suvalineAsukoht == "v-y":
                suvalinePlaat = Plaat(True, False, False, False)
            elif suvalineAsukoht == "v-a":
                suvalinePlaat = Plaat(False, False, True, False)
            elif suvalineAsukoht == "p-y":
                suvalinePlaat = Plaat(False, True, False, False)
            elif suvalineAsukoht == "p-a":
                suvalinePlaat = Plaat(False, False, False, True)

            plaat_group.add(suvalinePlaat)

    plaat_group.draw(screen)
    plaat_group.update()

    if pygame.sprite.spritecollide(player.sprite, plaat_group, True):
        print("Põrge!")
        punktid += 100

    screen.fill((0, 0, 0))
    player.draw(screen)
    player.update()

    font = pygame.font.SysFont("Bold", 50)
    txtsurf = font.render(str(punktid), True, red)
    screen.blit(txtsurf, (300 - txtsurf.get_width() // 2, 50 - txtsurf.get_height() // 2))
    pygame.display.update()

    plaat_group.draw(screen)
    plaat_group.update()

    pygame.display.update()
    clock.tick(60)
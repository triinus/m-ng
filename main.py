
import pygame
from tegelane import Player
from plaat import Plaat
from random import randint, choice


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

aeg = randint(0, 5)  #võtab suvalise nr 1-5, mis on aeg, mis aja tagant plaat kukub


plaat_1 = Plaat(True, False, False, False)
plaat_2 = Plaat(False, True, False, False)
plaat_3 = Plaat(False, False, True, False)
plaat_4 = Plaat(False, False, False, True)
plaadid = (plaat_1, plaat_2, plaat_3, plaat_4)

suvaline_plaat = choice(plaadid)


#kas seda on vaja?
plaat_group = pygame.sprite.Group()
plaat_group.add(plaadid)

#kas seda on vaja?
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


game_active = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    if event.type == obstacle_timer:
        plaat_group.add(suvaline_plaat)

    if suvaline_plaat:  #vaja et kuvaks plaatide listist sobiva plaadi sõltuvalt numbrist



    if pygame.sprite.spritecollide(player, plaadid, False):
        print("Põrge!")

    player.draw(screen)
    player.update()

    plaat_group.draw(screen)
    plaat_group.update()

    pygame.display.update()
    clock.tick(60)


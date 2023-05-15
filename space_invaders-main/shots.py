import pygame
import random
from variables import *


class Shots(pygame.sprite.Sprite):
    def __init__(self, xy, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = shotsimg
        self.rect = shotsimg.get_rect(center=(xy))
        self.shotes_ship = pygame.sprite.Group()
        self.shotes_aliens = pygame.sprite.Group()
        self.ship = pygame.sprite.Group()
        self.speed = speed

    def ship_shot_group(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shotes_ship.add(Shots(ship.sprites()[0].rect.center))


    def ship_shot_movement(self):
        for shut in self.shotes_ship:
            if shut.rect.y > 0:
                shut.rect.y -= 3 + self.speed/2
            if shut.rect.y <= 3:
                shut.kill()
        self.shotes_ship.draw(screen)

    def alien_shot(self):
        self.image = shoting

    def alien_shot_group(self, group):
        if len(group) >= 1:   
            a = random.choices(group.sprites(), k=1)
            sh = Shots(a[0].rect.center, self.speed)
            sh.alien_shot()
            if len(self.shotes_aliens) < self.speed + 5:
                self.shotes_aliens.add(sh)

    def alien_shot_movement(self):
        for shut in self.shotes_aliens:
                if shut.rect.y >= 0:
                    shut.rect.y += 3 + self.speed/2
                if shut.rect.y >= 850:
                    shut.kill()
        self.shotes_aliens.draw(screen)



class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = heartimg
        self.rect = heartimg.get_rect(center=(x, y))


class Gift(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = giftimg
        self.rect = giftimg.get_rect(center=(x,y))




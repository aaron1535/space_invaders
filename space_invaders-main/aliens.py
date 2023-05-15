from variables import *
import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = alienimg
        self.rect = alienimg.get_rect(center=(x,y))
        self.aliens = pygame.sprite.Group()
        self.n = 1
        self.speed = speed

    def creating_alien_group(self):
        p1 = 10
        p2 = 80
        for i in range(3):
            for j in range(10):
                p1 += 110
                self.aliens.add(Alien(p1, p2, self.n))
            p1 = 10
            p2 += 70

    def aliens_move(self):
        for alien in self.aliens:
            alien.rect.x += (self.speed + 1) * self.n
            if alien.rect.x >1500 or alien.rect.x <= 0:
                self.n = self.n*(-1)
                for alien in self.aliens:
                    alien.rect.y += 15
        self.aliens.draw(screen)

    def add_speed(self):
        self.speed += 1

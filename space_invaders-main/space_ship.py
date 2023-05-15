from variables import *
import pygame

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.car = carimg
        self.rect = carimg.get_rect(center=(x,y))
        self.speed = speed
        self.ship = pygame.sprite.Group()
        self.score = 0

    def car_group(self, car):
        self.ship.add(car)

    def car_move(self):
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT] and self.rect.x >0:
            self.rect.x -= 3 + self.speed
        if key_input[pygame.K_RIGHT] and self.rect.x <1540:
            self.rect.x += 3 + self.speed
        if key_input[pygame.K_DOWN] and self.rect.y <820:
            self.rect.y += 3 + self.speed
        if key_input[pygame.K_UP] and self.rect.y >720:
            self.rect.y -= 3 + self.speed



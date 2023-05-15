import pygame
from variables import *
from shots import *
from heart_gift import *
from space_ship import *
from aliens import *
pygame.init()


ship1 = Spaceship(750, 850, speed)
ship1.car_group(ship1)
ship = ship1.ship
alien = Alien(0, 0, speed)
alien.creating_alien_group()
aliens = alien.aliens
alien_shut = Shots(alien.rect.center, speed)
ship_shut = Shots(ship1.rect.center, speed)
heart = Heart(1150, 30, life)
gif = Gift(0, 0, ship1.score)

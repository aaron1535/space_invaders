import pygame
pygame.init()

screen = pygame.display.set_mode((1600, 900))
background_colour = (0, 0, 0)
pygame.display.set_caption('SPACE INVAIDERS by Aaron Sonnenfeld')
screen_img = pygame.image.load('12345.jpg')
screen_img = pygame.transform.scale(screen_img, (1600, 900))
carimg = pygame.image.load('ship.bmp')
alienimg = pygame.image.load('alien.bmp')
shotsimg = pygame.image.load('til.png')
shoting = pygame.image.load('bulit.png')
heartimg = pygame.image.load('heart.png')
giftimg = pygame.image.load('111.png')
shotes_ship = pygame.sprite.Group()
shotes_aliens = pygame.sprite.Group()
ship = pygame.sprite.Group()
hearts = pygame.sprite.Group()
gifts = pygame.sprite.Group()



speed = 1
life = 3
i = -900
















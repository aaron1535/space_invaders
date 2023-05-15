import pygame
from objects import *
pygame.init()



def Text(string, size, font, Location, RGB):
    font = pygame.font.Font(font, size)
    text = font.render(string, True, RGB)
    text_rect = text.get_rect(center = Location)
    return text, text_rect

text, text_rect = Text(' level  '+ str(speed), 48,'Arima-VariableFont_wght.ttf',  (1450, 30), (0, 255, 255))
text1, text_rect1 = Text(' KuLuLuLu', 120,'RubikMoonrocks-Regular.ttf', (800, 400), (0, 240, 0))
text2, text_rect2 = Text(' Press Enter to start the ' + ' level ' + str(speed + 1) , 72,'Anton-Regular.ttf', (800, 520), (0, 210, 0))
text3, text_rect3 = Text(' Maybe few times ;)', 64,'Anton-Regular.ttf', (800, 590), (0, 190, 0))
text4, text_rect4 = Text(' score ' + str(ship1.score), 52,'IndieFlower-Regular.ttf', (100, 20), (0, 255, 255))
text5, text_rect5 = Text(' "Welcome to Aaron games" ', 60,'PressStart2P-Regular.ttf', (800, 70), (255, 0, 0))
text7, text_rect7 = Text(' You lost  Ha Ha Ha..... ', 120,'AlfaSlabOne-Regular.ttf', (750, 550), (0, 0, 0))
text8, text_rect8 = Text(' Your score is ' + str(ship1.score), 100,'IndieFlower-Regular.ttf', (700, 720), (0, 230, 150))
#text9, text_rect9 = Text(' The highest score is ' + str(Results(score)), 120,'IndieFlower-Regular.ttf', (700, 800), (70, 230, 200))
text10, text_rect10 = Text(' Press Enter to start playing ', 53,'PressStart2P-Regular.ttf', (750, 850), (250, 0, 0))

def updating_text():
    global text, text_rect, text1, text_rect1, text2, text_rect2, text3, text_rect3, text4, text_rect4, text5, text_rect5, text7, text_rect7, text8, text_rect8, text10, text_rect10
    text, text_rect = Text(' level  '+ str(ship1.speed), 48,'Arima-VariableFont_wght.ttf',  (1450, 30), (0, 255, 255))
    text1, text_rect1 = Text(' KuLuLuLu', 120,'RubikMoonrocks-Regular.ttf', (800, 400), (0, 240, 0))
    text2, text_rect2 = Text(' Press Enter to start the ' + ' level ' + str(ship1.speed + 1) , 72,'Anton-Regular.ttf', (800, 520), (0, 210, 0))
    text3, text_rect3 = Text(' Maybe few times ;)', 64,'Anton-Regular.ttf', (800, 590), (0, 190, 0))
    text4, text_rect4 = Text(' score ' + str(ship1.score), 52,'IndieFlower-Regular.ttf', (100, 20), (0, 255, 255))
    text5, text_rect5 = Text(' "Welcome to Aaron games" ', 60,'PressStart2P-Regular.ttf', (800, 70), (255, 0, 0))
    text7, text_rect7 = Text(' You lost  Ha Ha Ha..... ', 120,'AlfaSlabOne-Regular.ttf', (750, 550), (0, 0, 0))
    text8, text_rect8 = Text(' Your score is ' + str(ship1.score), 100,'IndieFlower-Regular.ttf', (700, 720), (0, 230, 150))
    #text9, text_rect9 = Text(' The highest score is ' + str(Results(score)), 120,'IndieFlower-Regular.ttf', (700, 800), (70, 230, 200))
    text10, text_rect10 = Text(' Press Enter to start playing ', 53,'PressStart2P-Regular.ttf', (750, 850), (250, 0, 0))    


def start(filename):
    return pygame.image.load(filename)


start_game = True

def open_screen():
    global start_game
    while start_game:
        print('12345678')
        screen.blit(start('start.png'), (-100,-90))
        screen.blit(text5, text_rect5) #5
        screen.blit(text10, text_rect10) #10
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_game = False
                    print(start_game)
        pygame.display.flip()

def starts_playing():
    global i
    screen.blit(screen_img, (0,i))
    screen.blit(screen_img, (0,900 + i))
    if i == 0:
        screen.blit(screen_img, (0,901))
        i = -900
    i += 1
    ship1.car_move()
    screen.blit(ship1.car, ship1.rect)


def ship_shot_group():
    ship_shut.shotes_ship.add(Shots(ship.sprites()[0].rect.center, ship1.speed))


def battlefield_movement():
    ship_shut.ship_shot_movement()
    alien_shut.alien_shot_group(alien.aliens)
    alien_shut.alien_shot_movement()
    alien.aliens_move()
    ship_shut.ship_shot_movement()
    heart.draw_heart()
    #gif.add_gift()
    #gif.gift_draw()

def battlefield_collision_attacks():
    global score
    if pygame.sprite.groupcollide(gifts, ship, False, True):
                ship.add(Spaceship(750, 850, speed))
    if pygame.sprite.groupcollide(ship_shut.shotes_ship, aliens, True, True):
        ship1.score += 2
        print(ship1.score)
    if pygame.sprite.groupcollide(ship_shut.shotes_ship, alien_shut.shotes_aliens, True, True):
        ship1.score += 1
    if pygame.sprite.groupcollide(ship, alien_shut.shotes_aliens, False, True):
        heart.hearts.sprites()[-1].kill()
        heart.life -= 1
    if heart.life == 0:
        alien_shut.shotes_aliens.empty()
        ship_shut.shotes_ship.empty()
        screen.blit(start('1153443.png'), (-150,-420))
        screen.blit(text7, text_rect7) #7
        screen.blit(text8, text_rect8) #8
    if pygame.sprite.groupcollide(ship, aliens, False, True):
                heart.life == 0
    screen.blit(text, text_rect)
    screen.blit(text4, text_rect4)

def win_screen():
    screen.blit(text1, text_rect1) #1
    screen.blit(text2, text_rect2) #2
    ship_shut.shotes_ship.empty()
    alien_shut.shotes_aliens.empty()



def next_level():
    heart.hearts.empty()
    ship1.speed += 1
    alien_shut.speed += 1
    ship_shut.speed += 1
    alien.add_speed()
    alien.creating_alien_group()
    heart.x = 1150
    heart.life += 1





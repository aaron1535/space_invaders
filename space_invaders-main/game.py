from back_play import *
import pygame


def game_loop():
    global run
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_RETURN:
                    if len(alien.aliens) == 0:
                        next_level()
                if event.key == pygame.K_SPACE:
                    ship_shot_group()
        open_screen()
        starts_playing()
        updating_text()
        battlefield_movement()
        battlefield_collision_attacks()
        if len(alien.aliens) == 0:
            win_screen()
        pygame.display.flip()

run = True
def main():
    game_loop()

if __name__ == "__main__":
    main()


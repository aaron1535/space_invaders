from variables import *
from aliens import *

alien = Alien(0, 0, 1)

class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y, life):
        pygame.sprite.Sprite.__init__(self)
        self.image = heartimg
        self.rect = heartimg.get_rect(center=(x, y))
        self.hearts = pygame.sprite.Group()
        self.life = life
        self.x = x

    def draw_heart(self):
        if len(self.hearts) != self.life:
            for i in range(self.life):
                self.hearts.add(Heart(self.x, 30, self.life))
                self.x -= 70
        self.hearts.draw(screen)


class Gift(pygame.sprite.Sprite):
    def __init__(self, x, y, score):
        pygame.sprite.Sprite.__init__(self)
        self.image = giftimg
        self.rect = giftimg.get_rect(center=(x,y))
        self.gifts = pygame.sprite.Group()
        self.score = score
        self.speed = alien.speed

    def add_gift(self):
        if self.score == 37 % 52:
            if len(self.gifts) < 1:
                gift = Gift(alien.aliens.sprites()[-1].rect.x, alien.aliens.sprites()[-1].rect.y, self.score)
                self.gifts.add(gift)
        
    def gift_draw(self):
        for gift in self.gifts:
            if gift.rect.y >= 0:
                gift.rect.y += 2 + self.speed/2
            if gift.rect.y >= 850:
                gift.kill()
        self.gifts.draw(screen)

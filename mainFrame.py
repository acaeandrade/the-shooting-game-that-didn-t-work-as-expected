import pygame
from pygame.locals import *
from sys import *

pygame.init()

win = pygame.display.set_mode((1100, 600))
pygame.display.set_caption('T-Block Beta v0.0.1')

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bullets = []


class Ain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ain_shoot = []
        self.ain_shoot.append(pygame.image.load('red_dot_signal/red_dot2_0.png'))
        self.ain_shoot.append(pygame.image.load('red_dot_signal/red_dot2_1.png'))
        self.ain_shoot.append(pygame.image.load('red_dot_signal/red_dot2_2.png'))
        self.ain_shoot.append(pygame.image.load('red_dot_signal/red_dot2_3.png'))
        self.current = 0

        self.image = self.ain_shoot[self.current]
        self.image = pygame.transform.scale(self.image, (600, 600))
        self.rect = self.image.get_rect()
        self.rect.center = 450, 300

    def update(self):
        self.current = self.current + 0.1
        if self.current >=4:
            self.current = 0
        self.image = self.ain_shoot[int(self.current)]
        self.image = pygame.transform.scale(self.image, (1000, 1000))

        mpos = pygame.mouse.get_pos()

        self.rect = self.image.get_rect()

        #self.rect.topleft = pygame.mouse.get_pos()[0], -400
        self.rect.center = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + 30
        pygame.mouse.set_visible(False)

        #when shooting, the cursor should be moved sme pixels for


'''class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.character = []
        self.character.append(pygame.image.load('character/teb_mode Character1.png'))

    def update(self):
        self.current = self.current + 0.0001
        if self.current >= 4:
            self.current = 0
        self.image = self.ain_shoot[int(self.current)]
        self.image = pygame.transform.scale(self.image, (1000, 1000))

        mpos = pygame.mouse.get_pos()

        self.rect = self.image.get_rect()
        self.rect. = -50, -600
'''

#background
bg = pygame.image.load('red_dot_signal/main_background.jpeg').convert()
bg = pygame.transform.scale(bg, (900, 600))

#ain shoot
all_frames = pygame.sprite.Group()
ain = Ain()
all_frames.add(ain)

sound = pygame.mixer.music.load('red_dot_signal/m1a-suppressed.mp3')


clock = pygame.time.Clock()

while True:
    clock.tick(120)
    win.fill((0, 0, 0))
    win.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.key == [BUTTON_LEFT]:
                print('shooting!')
                sound = pygame.mixer.music.play()
            if event.type == MOUSEMOTION :
                print(event)

    all_frames.draw(win)
    all_frames.update()

    pygame.display.flip()
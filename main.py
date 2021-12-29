import pygame
import os
import sys
import random

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
GRAVITY = 0.001


class Plat:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# def load_image(name, colorkey=None):
#     fullname = os.path.join(name)
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     return image

background = pygame.image.load("eiffel.png")
background = pygame.transform.scale(background, (800, 600))
all_sprites = pygame.sprite.Group()

h = 0


class Game(pygame.sprite.Sprite):
    def __init__(self, *group):
        global h
        self.ch = ["grass_floor.png", "grass1_floor.png"]
        self.grass_image = pygame.image.load(random.choice(self.ch))
        self.grass = pygame.sprite.Sprite(all_sprites)
        self.grass.image = self.grass_image
        self.grass.rect = self.grass.image.get_rect()
        self.mask_of_grass = pygame.mask.from_surface(self.grass_image)
        self.grass.rect.x = random.randint(-100, 700)
        self.grass.rect.y = h
        h += 140


for _ in range(4):
    Game(all_sprites)


class Komar():
    def __init__(self, *group):
        self.komar_image = pygame.image.load("komar.png")
        self.komar_image = pygame.transform.scale(self.komar_image, (104, 136))
        self.komar = pygame.sprite.Sprite(all_sprites)
        self.komar.image = self.komar_image
        self.komar.rect = self.komar.image.get_rect()
        self.mask_of_komar = pygame.mask.from_surface(self.komar_image)
        self.komar.rect.x = 300
        self.komar.rect.y = 500

    # def update(self):
    #     dist = 10
    #     key = pygame.key.get_pressed()
    #     if key[pygame.K_DOWN]:
    #         print(self.komar.rect.top)
    #         self.komar.rect.top += dist
    #     elif key[pygame.K_UP]:
    #         self.komar.rect.top -= dist
    #     if key[pygame.K_RIGHT]:
    #         self.komar.rect.left += dist
    #     elif key[pygame.K_LEFT]:
    #         self.komar.rect.left -= dist
    # def update(self):


Komar(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print('ooo')
    # all_sprites.update()
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()

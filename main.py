import pygame
import os
import sys
import random

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

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

# class Game(pygame.sprite.Sprite):

ch = ["grass_floor.png", "grass1_floor.png"]
h = 0
for i in range(6):
    grass_image = pygame.image.load(random.choice(ch))
    grass = pygame.sprite.Sprite(all_sprites)
    grass.image = grass_image
    grass.rect = grass.image.get_rect()
    grass.rect.x = random.randint(-100, 700)
    grass.rect.y = h
    h += 100


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()

import pygame
import os
import sys
import random


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


intro_image = load_image('intro.png')
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
background = load_image("eiffel.png")
background = pygame.transform.scale(background, (800, 600))
h = 580


class Islands(pygame.sprite.Sprite):
    def __init__(self, x, *group):
        super().__init__(all_sprites)
        global h
        self.length = [190, 160]
        self.num1 = random.choice(self.length)
        # self.image = pygame.Surface((self.num1, 20))
        # self.image.fill((0, 153, 0))
        self.image = load_image('baget.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = h


class Komar(pygame.sprite.Sprite):
    image = load_image("komar.png")

    def __init__(self, *group):
        super().__init__(all_sprites)
        self.image = Komar.image

        self.rect = self.image.get_rect()
        # self.mask = pygame.mask.from_surface(self.image)
        self.velocity = 0
        self.rect.center = (300, 300)
        self.side = False

    def update(self):
        dx = 0
        dy = 0

        userInput = pygame.key.get_pressed()

        if userInput[pygame.K_LEFT]:
            dx = -10
            self.side = True
        elif userInput[pygame.K_RIGHT]:
            dx = 10
            self.side = False
        elif userInput[pygame.K_UP]:
            dy = -10
        elif userInput[pygame.K_DOWN]:
            dy = 10

        self.velocity += 1
        dy += self.velocity

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > 800:
            dx = 800 - self.rect.right

        collision = pygame.sprite.spritecollide(self, platforms, False)
        if collision:
            if self.rect.bottom < collision[0].rect.centery:
                if self.velocity > 0:
                    self.rect.bottom = collision[0].rect.top
                    dy = 0
                    self.velocity = -20

        if self.rect.bottom + dy > 600:
            dy = 0
            self.velocity = -20

        self.rect.x += dx
        self.rect.y += dy


switch = True
komar = Komar()
all_sprites.add(komar)

for _ in range(5):
    for _ in range(2):
        num_x = random.randint(-100, 750)
        if switch:
            island = Islands(num_x)
            switch = False
        else:
            island = Islands(num_x + random.randint(300, 450))
            switch = True
        platforms.add(island)
    h -= 160


class GameStates():
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'

        screen.blit(intro_image, (0, 0))
        pygame.display.flip()

    def main_game(self):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()

    def state_image(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()


game_state = GameStates()

while True:
    game_state.state_image()

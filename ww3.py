import pygame
import random
import os

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# set screen constants
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

pygame.init()

# set window title
pygame.display.set_caption("DellPogie Python Portfolio - World War III Game")

# set screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text_font = pygame.font.SysFont("Arial", 50)

def draw_text(text, font, text_col, x, y):
   img = font.render(text, True, text_col)
   screen.blit(img, (x, y))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("C:/Users/dellp/OneDrive/Desktop/ww3/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("C:/Users/dellp/OneDrive/Desktop/ww3/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("C:/Users/dellp/OneDrive/Desktop/ww3/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
            
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

player = Player()

clock = pygame.time.Clock()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# game loop
running = True
while running:

    clock.tick(10)
   
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                
        elif event.type == QUIT:
            running = False

        # create new enemy
        elif event.type == ADDENEMY:
            # add enemy to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # create new cloud
        elif event.type == ADDCLOUD:
            # add cloud to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    pygame.display.flip()

    # update enemy position
    enemies.update()
    clouds.update()

    # fill the sky with blue
    screen.fill((135, 206, 250))        

    # draw the sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # if enemy have collided with the jet
    if pygame.sprite.spritecollideany(player, enemies):
        # if yes, then remove the player then stop the loop
        player.kill()

        draw_text("Game Over! Thank you for playing! :)", text_font, (0, 0, 0), 220, 150)
        pygame.display.flip()
        
        # stop the loop
        running = False
            
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)    

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    
    player.update(pressed_keys)



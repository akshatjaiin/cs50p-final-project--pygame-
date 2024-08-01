# Import the pygame module, random for random numbers
import random
import pygame

pygame.mixer.init()
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Define constants for screen width, height, and custom events
ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2
ADDCOIN = pygame.USEREVENT + 3
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super(Player, self).__init__()
        self.surf = sprite["jet"]
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys, sounds):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            sounds["move_up"].play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            sounds["move_down"].play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super(Enemy, self).__init__()
        self.surf = sprite["missile"]
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < -5:
            self.kill()

# Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super(Coin, self).__init__()
        self.surf = sprite["coin"]
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 10)

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < -5:
            self.kill()

# Cloud Class
class Cloud(pygame.sprite.Sprite):
    def __init__(self, sprite):
        super(Cloud, self).__init__()
        self.surf = sprite["cloud"]
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < -8:
            self.kill()


# Load all our sound files Sound sources: Jon Fincher
def load_Sound():
    # Load and play our background music
    # Sound source: http://ccmixter.org/files/Apoxode/59262
    # License: https://creativecommons.org/licenses/by/3.0/
    print("sound loaded")
    pygame.mixer.music.load("melody/Apoxode_-_Electric_1.mp3")
    pygame.mixer.music.play(loops=-1)

    move_up_sound = pygame.mixer.Sound("melody/Rising_putter.ogg")
    move_down_sound = pygame.mixer.Sound("melody/Falling_putter.ogg")
    collision_sound = pygame.mixer.Sound("melody/Collision.ogg")
    coin_collect_sound = pygame.mixer.Sound("melody/coin_sound.mp3")

    
    # Return as a dictionary
    return {
        "move_up": move_up_sound,
        "move_down": move_down_sound,
        "collision": collision_sound,
        "collect": coin_collect_sound,
    }

#load sprites
def load_image():
    print("image loaded")
    background = pygame.image.load("image/sample_map.jpg")
    original_width = background.get_width()
    background = pygame.transform.scale(background, (original_width, SCREEN_HEIGHT))
    jet = pygame.image.load("image/jet.png").convert()
    missile = pygame.image.load("image/missile.png").convert()
    cloud = pygame.image.load("image/cloud.png").convert()
    coin = pygame.image.load("image/coin.png").convert()
    heart = pygame.image.load("image/heart.png").convert()
    return {
        "jet": jet,
        "missile": missile,
        "cloud": cloud,
        "background": background,
        "coin": coin,
        "heart": heart,
    }

# game events
def game_events(player, enemies, clouds, all_sprites, sprite, sounds, coins):
    print("event triggered")
    running = True
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy(sprite)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud(sprite)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            
        elif event.type == ADDCOIN:
            new_coin = Coin(sprite)
            coins.add(new_coin)
            all_sprites.add(new_coin)

    return running

def update_sprites(player, enemies, clouds, coins, sounds):
    print("update.x")
    player.update(pygame.key.get_pressed(), sounds)
    enemies.update()
    clouds.update()
    coins.update()

def draw_background(screen, sprite, x, bg_speed):
    # Determine the width of the background image
    bg_width = sprite["background"].get_width()
    
    # Draw the background
    # Draw the visible part of the background
    screen.blit(sprite["background"], (x, 0))
    screen.blit(sprite["background"], (bg_width+x, 0))

    # # Update the position for scrolling
    x -= bg_speed
    if (bg_width+x<0):
        x = 0
    return x

def draw_sprites(screen, all_sprites):
    print("drawing sprite")
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

def check_collisions(player, enemies, coins, sounds, hearts):
    if enemy := pygame.sprite.spritecollideany(player, enemies):
        print("heart loss")
        hearts -= 1
        enemy.kill()
        sounds["collision"].play()
    if coin := pygame.sprite.spritecollideany(player, coins):
        sounds["collect"].play()
        coin.kill()
        return 1, hearts
    return 0, hearts

def update_score_display(screen, coin_count, hearts, sprite):
    print(f"score {hearts}")
    font = pygame.font.SysFont('Arial', 36)
    text_surface = font.render(f'Score: {coin_count}', True, (255, 255, 255))  # White text
    text_rect = text_surface.get_rect(topright=(SCREEN_WIDTH - 10, 10))
    screen.blit(text_surface, text_rect)
    for i in range(hearts):
        screen.blit(sprite["heart"], (i * 40, 3))

def end_game(player, sounds):
    print("game over")
    player.kill()
    sounds["move_up"].stop()
    sounds["move_down"].stop()
    sounds["collision"].play()

def game_loop(player, enemies, clouds, coins, all_sprites, sprite, sounds, screen, clock):
    print("game loop")

    coin_count = 0
    hearts = 3
    pygame.font.init()
    running = True
    x = 0
    bg_speed = 4

    while running:
        print("loop started")
        running = game_events(player, enemies, clouds, all_sprites, sprite, sounds, coins)
        update_sprites(player, enemies, clouds, coins, sounds)
        x = draw_background(screen, sprite, x, bg_speed)
        draw_sprites(screen, all_sprites)
        collected, hearts = check_collisions(player, enemies, coins, sounds, hearts)
        coin_count += collected
        update_score_display(screen, coin_count, hearts, sprite)

        if hearts == 0:
            end_game(player, sounds)
            running = False

        pygame.display.update()
        clock.tick(30)


# from pygame.locals import Trigger(key)
from pygame.locals import (
    K_DOWN,
    K_ESCAPE,
    K_LEFT,
    K_RIGHT,
    K_UP,
    KEYDOWN,
    QUIT,
    RLEACCEL,
)



def main():

    sprite = load_image()
    sounds = load_Sound()
        
    # Access sounds from the dictionary and set the base volume for all
    sounds["move_up"].set_volume(0.5)
    sounds["move_down"].set_volume(0.5)
    sounds["collision"].set_volume(0.5)
    sounds["collect"].set_volume(0.8)

    # Create player and sprite groups
    player = Player(sprite)
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Create the screen object and custom events
    clock = pygame.time.Clock()
    pygame.time.set_timer(ADDENEMY, 250)
    pygame.time.set_timer(ADDCLOUD, 1000)
    pygame.time.set_timer(ADDCOIN, 600)

    # Start the game loop
    game_loop(player, enemies, clouds, coins, all_sprites, sprite, sounds, screen, clock)
 
    # At this point, we're done, so we can stop and quit the mixer
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    # Quit Pygame
    pygame.quit()

main()

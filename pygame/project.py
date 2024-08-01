# Import the pygame module, random for random numbers
import random
import pygame

coin_count = 0 #coins


# Load all our sound files Sound sources: Jon Fincher
def load_Sound():
    # Load and play our background music
    # Sound source: http://ccmixter.org/files/Apoxode/59262
    # License: https://creativecommons.org/licenses/by/3.0/
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
    background = pygame.image.load("image/game_background.jfif")
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
    running = True
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            
        elif event.type == ADDCOIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    return running

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# load sprites into a dictionary
sprite = load_image()
# Load sounds into a dictionary
sounds = load_Sound()

# Access sounds from the dictionary and set the base volume for all
sounds["move_up"].set_volume(0.5)
sounds["move_down"].set_volume(0.5)
sounds["collision"].set_volume(0.5)
sounds["collect"].set_volume(0.8)


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

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = sprite["jet"]
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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


# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create custom events for adding a new enemy and cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
ADDCOIN = pygame.USEREVENT + 3
pygame.time.set_timer(ADDCOIN, 600)

# Create our 'player'
player = Player()

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites isused for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player, coins)

pygame.font.init()  # Initialize the font module
font = pygame.font.SysFont('Arial', 36)
# Variable to keep our main loop running
running = True
x = 0
bg_speed = 5
# Our main loop
heart = 3
while running:
    # Look at every event in the queue check if user presses quit or esc
    running = game_events(player, enemies, clouds, all_sprites, sprite, sounds, coins)
    
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update the position of our enemies and clouds
    enemies.update()
    clouds.update()
    coins.update()
    
    text_surface = font.render(f'Score: {coin_count}', True, (255, 255, 255))  # White text

    # Get the rectangle of the text surface
    text_rect = text_surface.get_rect(topright=(SCREEN_WIDTH-10, 10))
    # Background movement
    screen.blit(sprite["background"], (x, 0))
    screen.blit(sprite["background"], (SCREEN_WIDTH + x, 0))
    screen.blit(text_surface, text_rect)
    for i in range(heart):
        screen.blit(sprite["heart"],(i*40,3))
    
    # Move the background to the left
    x -= bg_speed
    if x <= -SCREEN_WIDTH:
        x = 0

    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player remove enemy 
    if enemy := pygame.sprite.spritecollideany(player, enemies):
        heart-=1
        enemy.kill()

        # Stop any moving sounds and play the collision sound
        sounds["collision"].play()    

        
    if coin := pygame.sprite.spritecollideany(player, coins):
        sounds["collect"].play()
        coin.kill()
        coin_count+=1

    if heart == 0:
        player.kill()
        # Stop any moving sounds and play the collision sound
        sounds["move_up"].stop()
        sounds["move_down"].stop()
        sounds["collision"].play()
        # stop the game
        running = False

    # Updare everything to the display
    pygame.display.update()
    # Ensure we maintain a 30 frames per second rate
    clock.tick(30)


def main():
    # Initialize pygame and Setup for sounds, defaults are good 
    pygame.mixer.init()
    pygame.init()



    # At this point, we're done, so we can stop and quit the mixer
    pygame.mixer.music.stop()
    pygame.mixer.quit()
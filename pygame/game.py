# Import the pygame module
import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
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

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf = pygame. transform. scale(self.surf, (30,20))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # UPDATE THE PLAYER POSITION ON THE SCREEN
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, +5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(+5, 0)

        # KEEP THE SPIRIT  WITHIN THE SCREEN
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf = pygame. transform. scale(self.surf, (20,20))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(3, 8)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right == 0:
            self.kill()

# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()



# Initialize pygamee
pygame.init()



# Create the screen object  
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()

#crezte z event to create the event
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 250)
clock = pygame.time.Clock()
#create a group for sprit
# make enemy
# clear
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Create custom events for adding a new enemy and a cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
# Variable to keep the main loop running
running = True
# Initialize score variable
score = 0
high_score = 0
try:
    with open('high_score.txt', 'r') as file:
        high_score = int(file.read())
except FileNotFoundError:
    with open('high_score.txt', 'w') as file:
        file.write('0')
# Initialize font for score display
font = pygame.font.Font(None, 36)

# Main loop
def start_screen():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    start = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.fill((135, 206, 235))  # Light blue background

        # Load and display the title image
        title_image = pygame.image.load('jet_game_title.png')
        title_image_rect = title_image.get_rect()
        title_image_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100)
        screen.blit(title_image, title_image_rect)

        # Load and display the jet image
        jet_image = pygame.image.load('jet.png')
        jet_image_rect = jet_image.get_rect()
        jet_image_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)
        screen.blit(jet_image, jet_image_rect)

        # Display the instructions
        font = pygame.font.Font(None, 36)
        text = font.render("Press 'P' to play, 'Q' to quit", True, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)
    game()

def game_over_screen(score, high_score):
    global screen
    global font
    clock = pygame.time.Clock()
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    game_over = False
                    restart_game()
                    global running
                    running = True
                    return

        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 64)
        game_over_text = font.render('Game Over', True, (0, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 100))

        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))

        high_score_text = font.render(f'High Score: {high_score}', True, (0, 0, 0))
        screen.blit(high_score_text, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2))

        options_text = font.render('Press Q to quit or P to play again', True, (0, 0, 0))
        screen.blit(options_text, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 + 50))

        pygame.display.flip()
        clock.tick(60)

def restart_game():
    print("restart_game")
    global score, high_score
    score = 0
    player.kill()
    player.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    enemies.empty()
    clouds.empty()
    all_sprites.empty()
    all_sprites.add(player)
    pygame.time.set_timer(ADD_ENEMY, 250)
    pygame.time.set_timer(ADDCLOUD, 1000)
    running = True
    game()
def game():
    
# Initialize pygamee
pygame.init()



# Create the screen object  
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()

#crezte z event to create the event
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 250)
clock = pygame.time.Clock()
#create a group for sprit
# make enemy
# clear
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Create custom events for adding a new enemy and a cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
# Variable to keep the main loop running
running = True
# Initialize score variable
score = 0
high_score = 0
try:
    with open('high_score.txt', 'r') as file:
        high_score = int(file.read())
except FileNotFoundError:
    with open('high_score.txt', 'w') as file:
        file.write('0')
# Initialize font for score display
font = pygame.font.Font(None, 36)

    while running:

        print("running_game")
        # Setup the clock for a decent framerate
        clock = pygame.time.Clock()

        # for loop through the event queue
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False
            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                running = False

            elif event.type == ADD_ENEMY:
               # CREATE A NEW ENEMY AND ADD IT TO THE SPRITE GROUP
                new_enemy = Enemy()
                enemies.add(new_enemy)
                clouds = pygame.sprite.Group()
                all_sprites.add(new_enemy)
                score += 1

            # Add a new cloud?
            elif event.type == ADDCLOUD:
                # Create the new cloud and add it to sprite groups
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)


        #key pressed by the user
        key_pressed = pygame.key.get_pressed()

        # UPDATING THE LOCATION OF SPRITE ON THE SCREEN
        player.update(key_pressed)

        #update enemies position
        enemies.update()
        clouds.update()

        # Fill the screen with sky blue
        screen.fill((135, 206, 250))

        # Draw the player on the screen
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

    # collision detection
        if pygame.sprite.spritecollideany(player, enemies):
            game_over_screen(score, high_score)


        # screen.fill((255, 255, 255))
        # for entity in all_sprites:
        #     screen.blit(entity.surf, entity.rect)


        # Draw the score on the screen
        score_surface = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_surface, (10, 10))
        if score > high_score:
            high_score = score
            with open('high_score.txt', 'w') as file:
                file.write(str(high_score))
        font = pygame.font.Font(None, 36)
        high_score_text = font.render(f'High Score: {high_score}', True, (0, 0, 0))
        screen.blit(high_score_text, (SCREEN_WIDTH - 200, 10))

        # Update the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(60)


if __name__ == "__main__":
    start_screen()
import pygame

# Assume these functions are defined elsewhere and imported here
def load_Sound():
    move_up_sound = pygame.mixer.Sound("melody/Rising_putter.ogg")
    move_down_sound = pygame.mixer.Sound("melody/Falling_putter.ogg")
    collision_sound = pygame.mixer.Sound("melody/Collision.ogg")
    
    return {
        "move_up": move_up_sound,
        "move_down": move_down_sound,
        "collision": collision_sound
    }

def load_image():
    background = pygame.image.load("image/game_background.jfif")
    jet = pygame.image.load("image/jet.png").convert()
    missile = pygame.image.load("image/missile.png").convert()
    cloud = pygame.image.load("image/cloud.png").convert()
    return {
        "jet": jet,
        "missile": missile,
        "cloud": cloud,
        "background": background
    }

def test_load_Sound():
    try:
        sounds = load_Sound()
        assert "move_up" in sounds
        assert "move_down" in sounds
        assert "collision" in sounds
        assert isinstance(sounds["move_up"], pygame.mixer.Sound)
        assert isinstance(sounds["move_down"], pygame.mixer.Sound)
        assert isinstance(sounds["collision"], pygame.mixer.Sound)
        print("load_Sound() passed.")
    except AssertionError as e:
        print("load_Sound() failed:", e)
    except Exception as e:
        print("load_Sound() raised an exception:", e)

def test_load_image():
    try:
        images = load_image()
        assert "jet" in images
        assert "missile" in images
        assert "cloud" in images
        assert "background" in images
        assert isinstance(images["jet"], pygame.Surface)
        assert isinstance(images["missile"], pygame.Surface)
        assert isinstance(images["cloud"], pygame.Surface)
        assert isinstance(images["background"], pygame.Surface)
        print("load_image() passed.")
    except AssertionError as e:
        print("load_image() failed:", e)
    except Exception as e:
        print("load_image() raised an exception:", e)

def main():
    pygame.mixer.init()
    pygame.display.init()
    
    test_load_Sound()
    test_load_image()
    
    pygame.mixer.quit()
    pygame.display.quit()

if __name__ == "__main__":
    main()

from project import load_Sound, load_image, game_events
import pygame

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

def test_game_events():
    pass

def main():
    pygame.mixer.init()
    pygame.display.init()
    
    test_load_Sound()
    test_load_image()
    test_game_events()
    
    pygame.mixer.quit()
    pygame.display.quit()

if __name__ == "__main__":
    main()

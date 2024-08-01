import pygame 
from project import load_Sound, load_image, game_events
import unittest
from unittest.mock import MagicMock, patch

class TestGameFunctions(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.mixer.init()

    def tearDown(self):
        pygame.mixer.quit()
        pygame.quit()

    def test_load_Sound(self):
        try:
            sounds = load_Sound()
            assert isinstance(sounds["move_up"], pygame.mixer.Sound)
            assert isinstance(sounds["move_down"], pygame.mixer.Sound)
            assert isinstance(sounds["collision"], pygame.mixer.Sound)
            assert isinstance(sounds["collect"], pygame.mixer.Sound)
            print("load_Sound() passed.")
        except Exception as e:
            print(f"load_Sound() raised an exception: {e}")

    def test_load_image(self):
        try:
            images = load_image()
            assert isinstance(images["jet"], pygame.Surface)
            assert isinstance(images["missile"], pygame.Surface)
            assert isinstance(images["cloud"], pygame.Surface)
            assert isinstance(images["background"], pygame.Surface)
            assert isinstance(images["coin"], pygame.Surface)
            assert isinstance(images["heart"], pygame.Surface)
            print("load_image() passed.")
        except Exception as e:
            print(f"load_image() raised an exception: {e}")

    @patch('pygame.event.get')
    def test_game_events(self, mock_get):
        # Define custom event types for testing
        ADDENEMY = pygame.USEREVENT + 1
        ADDCLOUD = pygame.USEREVENT + 2
        ADDCOIN = pygame.USEREVENT + 3
        mock_get.return_value = [
            pygame.event.Event(ADDENEMY),
            pygame.event.Event(ADDCLOUD),
            pygame.event.Event(ADDCOIN)
        ]

        player = MagicMock()
        enemies = pygame.sprite.Group()
        clouds = pygame.sprite.Group()
        coins = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()

        running = game_events(player, enemies, clouds, all_sprites, None, None, coins)

        assert running == True
        assert len(enemies) == 1
        assert len(clouds) == 1
        assert len(coins) == 1
        assert len(all_sprites) == 3

        print("game_events() passed.")

if __name__ == "__main__":
    unittest.main()

![image](https://github.com/user-attachments/assets/9799e941-179f-4ab6-bbd2-f8cb91faa264)

# Jet Shoter
#### Video Demo:  <https://www.youtube.com/watch?v=ojbPM6gELck>
#### Description: game using pygame
<its a good game>

finally i m here submitting my python project i completed all the pset months ago but havent submit my project the reason is im not confident about my self and i want to make a best project but here i m submiting my project that i started months ago and completing the cycle.

// but wait you have to run *pip install pygame* before it now we are good to go //

# Pygame Jet Fighter Game

This is a 2D jet fighter game developed using the Pygame library in Python. The objective of the game is to control a jet, avoid incoming missiles, collect coins, and score as many points as possible while avoiding collisions. The game includes sound effects and a moving background to enhance the gameplay experience.

## Features

- **Player Controls**: Control a jet using the arrow keys.
- **Enemies**: Avoid incoming missiles that appear randomly on the screen.
- **Coins**: Collect coins to increase your score.
- **Clouds**: Clouds move across the screen as a part of the background.
- **Score and Health System**: Track your score and remaining hearts (health). The game ends when you lose all hearts.
- **Sound Effects**: Various sound effects for actions like moving, collecting coins, and collisions.
- **Scrolling Background**: A continuous scrolling background to simulate movement.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/akshatjaiin/cs50p-final-project--pygame-
    cd project
    ```

2. **Install Pygame**:
    Ensure you have Python installed. Install the required Pygame module using pip:
    ```sh
    pip install pygame
    ```

3. **Place Assets**:
    - Ensure all image assets (e.g., `jet.png`, `missile.png`, `cloud.png`, etc.) are in an `image` directory within the project folder.
    - Place the sound files (e.g., `Apoxode_-_Electric_1.mp3`, `Rising_putter.ogg`, etc.) in a `melody` directory within the project folder.

## How to Play

1. **Run the Game**:
    Run the main script to start the game.
    ```sh
    python main.py
    ```

2. **Controls**:
    - **Up Arrow**: Move the jet up.
    - **Down Arrow**: Move the jet down.
    - **Left Arrow**: Move the jet left.
    - **Right Arrow**: Move the jet right.
    - **Escape**: Quit the game.

3. **Objective**:
    - Avoid missiles.
    - Collect as many coins as possible.
    - The game ends when you lose all hearts.

## Game Loop Overview

The game consists of several classes:

- **Player**: Handles the player's jet, movement, and boundary conditions.
- **Enemy (Missile)**: Represents the missiles, which move from right to left and are removed once off-screen.
- **Coin**: Represents coins that the player collects for points.
- **Cloud**: Represents clouds moving in the background.
  
The game loop manages events, updates sprites, checks for collisions, and updates the score and screen.

## Known Issues and Future Enhancements

- The game could be enhanced with additional levels, different types of enemies, or power-ups.
- Currently, there's no pause or restart functionality, which could be added in future updates.

## Credits

- **Sound Effects**: Provided by Jon Fincher under Creative Commons license.
- **Background Music**: Sourced from [ccMixter](http://ccmixter.org/files/Apoxode/59262) under a [Creative Commons license](https://creativecommons.org/licenses/by/3.0/).


# Pygame Jet Fighter Game - Code Explanation

This README provides an in-depth explanation of the code structure, classes, functions, and overall game logic for the 2D Jet Fighter Game developed using Pygame.

## Code Structure

The code is organized into several key components:

1. **Constants and Initial Setup**: 
    - The code begins by importing the necessary libraries (`pygame`, `random`) and initializing the Pygame mixer and display.
    - Constants like `SCREEN_WIDTH`, `SCREEN_HEIGHT`, and custom Pygame events (`ADDENEMY`, `ADDCLOUD`, `ADDCOIN`) are defined.

2. **Classes**: 
    - The game utilizes several classes to represent different entities in the game:
        - `Player`: Represents the player-controlled jet.
        - `Enemy`: Represents the enemy missiles.
        - `Coin`: Represents the collectible coins.
        - `Cloud`: Represents the moving clouds in the background.

3. **Function Definitions**:
    - The code is modularized into several functions, each handling specific aspects of the game:
        - `load_Sound()`: Loads and returns a dictionary of sound effects.
        - `load_image()`: Loads and returns a dictionary of image assets.
        - `game_events()`: Handles Pygame events like keypresses and custom events for spawning enemies, clouds, and coins.
        - `update_sprites()`: Updates the position and state of all sprites.
        - `draw_background()`: Draws and scrolls the background image.
        - `draw_sprites()`: Draws all active sprites on the screen.
        - `check_collisions()`: Detects collisions between the player and enemies/coins.
        - `update_score_display()`: Updates the score and displays the player's remaining hearts.
        - `end_game()`: Handles the game-over state, stopping sounds and cleaning up.
        - `game_loop()`: The main game loop that continuously runs until the game ends.

4. **Main Function**:
    - The `main()` function ties everything together:
        - It loads images and sounds, displays the opening screen, and initializes the player and sprite groups.
        - The game loop is then started by calling `game_loop()`.

## Classes Explanation

### `Player` Class
- **Purpose**: Represents the player's jet and handles movement based on keypresses.
- **Key Methods**:
    - `__init__(self, sprite)`: Initializes the player with the provided sprite, setting up the initial position.
    - `update(self, pressed_keys, sounds)`: Updates the player's position based on keypresses and ensures the player remains within screen bounds. Plays movement sounds.

### `Enemy` Class
- **Purpose**: Represents enemy missiles that the player must avoid.
- **Key Methods**:
    - `__init__(self, sprite)`: Initializes the enemy with a random position and speed.
    - `update(self)`: Moves the enemy across the screen and removes it when it goes off-screen.

### `Coin` Class
- **Purpose**: Represents coins that the player can collect to increase their score.
- **Key Methods**:
    - `__init__(self, sprite)`: Initializes the coin with a random position and speed.
    - `update(self)`: Moves the coin across the screen and removes it when it goes off-screen.

### `Cloud` Class
- **Purpose**: Represents clouds moving in the background, adding depth to the game.
- **Key Methods**:
    - `__init__(self, sprite)`: Initializes the cloud with a random position.
    - `update(self)`: Moves the cloud across the screen and removes it when it goes off-screen.

## Function Explanation

### `load_Sound()`
- **Purpose**: Loads the game's sound effects and background music.
- **Details**: Returns a dictionary of sound objects that are used throughout the game for different actions.

### `load_image()`
- **Purpose**: Loads and returns a dictionary of all the image assets used in the game.
- **Details**: This includes sprites for the player, enemies, coins, clouds, and background.

### `game_events()`
- **Purpose**: Handles user inputs and custom game events (like adding enemies, clouds, and coins).
- **Details**: It checks for keypresses (like ESC to quit) and spawns new game objects based on timed events.

### `update_sprites()`
- **Purpose**: Calls the `update()` method on all sprite groups to move and update their states.
- **Details**: This keeps the game objects moving and reacting to player inputs.

### `draw_background()`
- **Purpose**: Draws the scrolling background to give the illusion of movement.
- **Details**: The background image is drawn in a loop to create a continuous scrolling effect.

### `draw_sprites()`
- **Purpose**: Draws all active sprites on the screen.
- **Details**: Iterates through all sprites in `all_sprites` and blits them to the screen.

### `check_collisions()`
- **Purpose**: Detects collisions between the player and enemies/coins.
- **Details**: If a collision with an enemy occurs, the player loses a heart. If a coin is collected, the score increases.

### `update_score_display()`
- **Purpose**: Updates and displays the player's score and remaining hearts on the screen.
- **Details**: Renders text for the score and uses heart sprites to show the player's remaining lives.

### `end_game()`
- **Purpose**: Handles the game-over state by stopping the game, playing a collision sound, and cleaning up.
- **Details**: This function is called when the player loses all hearts.

### `game_loop()`
- **Purpose**: The core loop that runs the game until it ends.
- **Details**: It handles events, updates sprites, checks for collisions, draws the screen, and manages the game's running state.

## Execution Flow

1. The game starts by initializing Pygame and loading all assets.
2. The `main()` function displays the opening screen and waits for user input to start the game.
3. The `game_loop()` function runs continuously, handling game logic, updating sprites, checking for collisions, and rendering the game until the player loses all hearts.
4. The game ends by stopping the music and quitting Pygame.

## Conclusion

This code provides a complete framework for a simple 2D jet fighter game. It demonstrates the use of Pygame's sprite and event systems, sound management, and basic game loop structure. The modular design allows for easy extension and customization of the game.


## License

This project is licensed under the MIT License.

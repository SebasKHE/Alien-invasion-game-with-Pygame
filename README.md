# Alien-invasion-game-with-Pygame

**Alien Invasion** is a game developed in **Python** using the **Pygame** library, where the player controls a spaceship to shoot and defend against waves of invading aliens. This project demonstrates how to structure a basic 2D game and is ideal for anyone looking to learn or practice game development skills.

## Project Structure  

The project is organized as follows:  

- **`alien_invasion.py`**: The main file that initializes the game. It sets up Pygame, creates the main game objects, and runs the main game loop.  

- **`alien.py`**: Defines the **Alien** class, representing the enemies in the game. It includes the logic for alien movement and behavior.  

- **`bullet.py`**: Contains the **Bullet** class, which defines the bullets shot by the player’s spaceship. Handles their creation, position, and removal when they exit the screen or hit an alien.  

- **`button.py`**: Defines the **Button** class, used to create interactive buttons like the start button in the game menus.  

- **`character.py`**: Represents the player’s spaceship. It includes logic for movement and interaction with other game elements.  

- **`game_functions.py`**: A module that centralizes key game functions, such as collision detection, screen updates, and player event handling (e.g., key presses or mouse clicks).  

- **`game_stats.py`**: Manages game statistics such as score, remaining lives, and game state (active, paused, etc.).  

- **`settings.py`**: Contains the **Settings** class, defining global game configurations like screen size, spaceship speed, alien speed, and bullet behavior. This makes it easy to tweak game properties without modifying other files.  

- **`scoreboard.py`**: Handles the logic for displaying player stats on the screen, including scores, levels, and high scores.  

- **Resource Files (Images and Text)**:  
  - **Images (`*.png`)**: Includes graphics for aliens, the player’s spaceship, bullets, stars, and more, bringing the game to life.  
  - **`stats.txt`**: A file used to store persistent data, such as the highest score achieved in previous game sessions.  

---

## Features  

- **Interactive Gameplay**: Control the spaceship using the keyboard to dodge aliens and shoot bullets.  
- **Statistics Tracking**: Displays scores, levels, and remaining lives.  
- **Progressive Difficulty**: Alien speed increases as the player progresses, making the game more challenging.  
- **Persistent Data**: Saves the highest score to `stats.txt`.  
- **Interactive Menu**: Includes buttons to start or restart the game.  

---

## Installation and Running the Game  

### Requirements  
- **Python 3.10 or higher**  
- **Pygame** library  

### Instructions  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/your-username/alien-invasion.git  
   cd alien-invasion  
   ```  

2. Install the required library:  
   ```bash  
   pip install pygame  
   ```  

3. Run the game:  
   ```bash  
   python alien_invasion.py  
   ```  

---

## Contribution  

If you’d like to improve the game or add new features, feel free to fork the project and submit a pull request.  

--- 

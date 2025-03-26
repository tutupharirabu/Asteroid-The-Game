# Asteroid: The Game

A classic arcade-style space shooter game built with Pygame where you control a ship, blast asteroids, and try to achieve the highest score possible.

## Game Overview

In Asteroid: The Game, you pilot a triangular ship through space, avoiding and shooting asteroids that appear from the edges of the screen. As you destroy asteroids, they split into smaller pieces, and your score increases. The game ends when your ship collides with an asteroid.

## Controls

- **W** - Move forward
- **S** - Move backward
- **A** - Rotate counter-clockwise
- **D** - Rotate clockwise
- **SPACE** - Shoot

### If You Die

- **R** - Restart after game over
- **ESC** - Exit after game over

## Installation

### Prerequisites

- Python 3.x
- Pygame 2.6.1

### Setup

1. Clone this repository:
   ```
   https://github.com/tutupharirabu/asteroid-the-game.git
   cd asteroid-the-game
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game

After installation, run the game with:

```
python main.py
```

## Game Features

- Ship with momentum-based movement
- Asteroids that split into smaller pieces when shot
- Score tracking system
- Game over screen with restart option
- Customized with your username

## Project Structure

- `main.py` - Main game loop and initialization
- `constants.py` - Game constants and configuration
- `assets/` - Game objects and classes
  - `player.py` - Player ship implementation
  - `asteroid.py` - Asteroid implementation
  - `asteroidfield.py` - Asteroid spawning system
  - `shot.py` - Player projectiles
  - `circleshape.py` - Base class for circular collision objects

## Future Enhancements

- Add sound effects and background music
- Implement different levels with increasing difficulty
- Add power-ups and special weapons
- Implement a high score system
- Add different enemy types

## Acknowledgements

- Inspired by the classic Asteroids arcade game
- Built with [Pygame](https://www.pygame.org/)

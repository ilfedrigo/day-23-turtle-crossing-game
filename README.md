# Turtle Crossing Game

This project is part of my 100 days of code in Python, and it represents my 23rd day.

The game involves a turtle that moves vertically to cross a busy road while avoiding oncoming cars. The goal is to reach the top of the screen to advance to the next level.

## How to Play

- Use the **"W"** key to move the turtle up.
- Use the **"S"** key to move the turtle down.
- Cross the road without colliding with cars to advance to the next level.
- If the turtle collides with a car, the game ends, and **"GAME OVER"** is displayed.

## Game Rules

- The turtle starts at the bottom center of the screen and must reach the top to advance levels.
- Cars appear randomly on the road, and their speed increases with each level.

## Files

- `main.py`: Contains the main game and setup.
- `car_manager.py`: This module defines the CarManager class, which is responsible for creating, moving, and increasing the speed of cars on the road. Cars are generated randomly, and their speed increases as the player progresses through levels.
- `player.py`: The Player class is defined in this module. It represents the player-controlled turtle that moves vertically to cross the road. The player can move up, move down, and reset its position. The game involves avoiding collisions with oncoming cars.
- `scoreboard.py`: This module contains the Scoreboard class, which manages the game's scoring and displays the current level. The scoreboard updates with each successful crossing, and it shows "GAME OVER" when a collision occurs.

## How to Run

- Ensure that Python is installed on your system.
- Run the main.py script.

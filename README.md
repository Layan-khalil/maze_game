# Maze Runner Game

## Description

**Maze Runner** is a simple game where the player navigates through a randomly generated maze. The goal is to reach the exit of the maze, which is located at the bottom-right corner. The player can move using the arrow keys.

## Features
- **Random Maze Generation**: The maze is generated dynamically using a Depth-First Search (DFS) algorithm.
- **Player Movement**: The player can move using the arrow keys (Up, Down, Left, Right).
- **Exit**: Reach the bottom-right corner of the maze to win.

## Requirements

- **Python 3.x**: This game is built using Python.
- **Pygame**: A library used for game development.

## How to Run the Game

Follow these steps to set up and run the game on your own computer:

### 1. Install Python

Make sure you have Python 3.x installed. If not, download and install it from [python.org](https://www.python.org/downloads/). Ensure that Python is added to your system's PATH.

To check if Python is installed, open a terminal/command prompt and run:

```bash
python --version

2. Install Pygame
The game uses Pygame, a library used for game development. Install Pygame using pip (Python's package installer).

Open your terminal/command prompt and run the following command:

bash
Copy code
pip install pygame

3. Clone the Repository
Clone this repository to your local machine using Git. If you don't have Git installed, you can download it from git-scm.com.

To clone the repository:

Go to the directory where you want to store the project.
Run the following command:
bash
Copy code
git clone https://github.com/your-username/maze-game.git
4. Run the Game
Navigate to the project directory and run the Python script:

bash
Copy code
python maze_game.py
This will launch the game, and you can start playing by using the arrow keys to navigate through the maze.

5. Game Controls
Arrow Keys: Move the player (green square) through the maze.
Goal: Reach the red square at the bottom-right corner to win the game.
6. Exit
To quit the game, close the Pygame window, or press Alt+F4.

How the Maze is Generated
The maze is randomly generated using a Depth-First Search (DFS) algorithm. Starting from the top-left corner, the algorithm recursively carves paths through the maze by choosing random directions. The goal (bottom-right corner) is always open, and the player must navigate from the start to the goal.

License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy code

---

 **Explanation of the Sections in the README**:

1. **Project Description**: Briefly explains what the game is about.
2. **Features**: Lists key features such as random maze generation, player movement, and the goal.
3. **Requirements**: Details the software required to run the game (Python and Pygame).
4. **How to Run the Game**: The step-by-step process that users need to follow to set up and run the game on their own system.
   - **Install Python**: Guides users to install Python if they don’t have it already.
   - **Install Pygame**: Instructions to install Pygame via `pip`.
   - **Clone the Repository**: Instructions to clone the repository from GitHub.
   - **Run the Game**: The command to start the game script.
5. **Game Controls**: Explains how to play the game using the arrow keys and the goal.
6. **Exit Instructions**: Details on how to exit the game.
7. **Maze Generation Explanation**: A brief explanation of how the maze is generated (using DFS).
8. **License**: A note about licensing if you’re using open-source software (MIT license here as an example).

---


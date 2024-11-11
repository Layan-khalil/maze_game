import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40
MAZE_WIDTH = WIDTH // CELL_SIZE
MAZE_HEIGHT = HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maze Runner')

# Player class to handle the player's position
class Player:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.color = GREEN

    def move(self, dx, dy, maze):
        if 0 <= self.x + dx < MAZE_WIDTH and 0 <= self.y + dy < MAZE_HEIGHT:
            if maze[self.y + dy][self.x + dx] == 0:
                self.x += dx
                self.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to generate a random maze using Depth First Search (DFS) algorithm
def generate_maze():
    maze = [[1] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]  # Start with all walls

    def dfs(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        random.shuffle(directions)  # Shuffle directions to make it random
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and maze[ny][nx] == 1:
                maze[ny][nx] = 0  # Remove wall
                maze[y + dy][x + dx] = 0  # Remove wall between current and new cell
                dfs(nx, ny)

    maze[1][1] = 0  # Starting point
    dfs(1, 1)
    maze[MAZE_HEIGHT - 2][MAZE_WIDTH - 2] = 0  # End point
    return maze

# Function to draw the maze on the screen
def draw_maze(maze):
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            color = WHITE if maze[y][x] == 0 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main game loop
def game():
    player = Player()
    maze = generate_maze()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1, 0, maze)
        if keys[pygame.K_RIGHT]:
            player.move(1, 0, maze)
        if keys[pygame.K_UP]:
            player.move(0, -1, maze)
        if keys[pygame.K_DOWN]:
            player.move(0, 1, maze)

        # Check if the player has reached the end
        if player.x == MAZE_WIDTH - 2 and player.y == MAZE_HEIGHT - 2:
            print("Congratulations! You completed the maze!")
            pygame.quit()
            sys.exit()

        screen.fill(BLACK)
        draw_maze(maze)
        player.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(10)

# Start the game
if __name__ == "__main__":
    game()
 
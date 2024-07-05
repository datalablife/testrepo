import pygame
import random

# Define the Tetris grid
GRID_WIDTH, GRID_HEIGHT = 10, 20
CELL_SIZE = 30
GRID_ORIGIN = (100, 50)

# Define the shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1, 0],
     [0, 0, 1]],
    [[1, 1, 1, 0],
     [1]],
    [[1, 1, 0, 0],
     [0, 1, 1]],
    [[0, 1, 1],
     [1, 1]],
    [[1, 1],
     [1, 1]]
]

# Define colors
COLORS = [(0, 255, 255), (255, 165, 0), (0, 0, 255), (255, 255, 0), (255, 0, 0), (0, 255, 0), (160, 32, 240)]

# Initialize Pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tetris')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Draw the Tetris grid
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            rect = (GRID_ORIGIN[0]+j*CELL_SIZE, GRID_ORIGIN[1]+i*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

    # Draw a random shape
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                rect = (GRID_ORIGIN[0]+j*CELL_SIZE, GRID_ORIGIN[1]+i*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect)

    # Update the display
    pygame.display.flip()
    pygame.time.wait(500)  # Wait for half a second

pygame.quit()

import pygame
import time

pygame.init()

CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

BLACK = (0, 0, 0)
PINK = (255, 192, 203)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
pygame.display.set_caption("Enter Effect in pygame")


grid = []

for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)


eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)
running = True

while running:
    screen.fill(PINK)

    for rect in grid:
        pygame.draw.rect(screen, BLACK, rect)
    mouse_x , mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x , mouse_y)

    new_grid = []
    
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)

    grid = new_grid

    pygame.draw.rect(screen, RED, eraser)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()



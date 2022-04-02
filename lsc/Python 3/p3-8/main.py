import pygame
import SnakeGame

display = SnakeGame.Disp((400, 300))
game_over = False
while not game_over:
    SnakeGame.GameLogic.tick()
pygame.quit()


import time

import pygame

pygame.init()
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake')
pygame.draw.rect(dis, blue, [200, 150, 10, 10])
pygame.display.update()
snake_block = 10
font_stlye = pygame.font.SysFont("Arial", 50)
# pygame.time.Clock.__init__()


def massage(msg: str, color: 'tuple(int, int, int)'):
    return font_stlye.render(msg, True, color)


def game_loop():
    game_over = False
    x1 = 200
    y1 = 100
    x1_change = 0
    y1_change = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            if event.type == pygame.event:
                if event.key == pygame.KEYUP:
                    x1_change = -snake_block
                if event.key == pygame.KEYDOWN:
                    x1_change = snake_block
                if event.key == pygame.K_LEFT:
                    y1_change = -snake_block
                if event.key == pygame.K_RIGHT:
                    y1_change = snake_block
        if x1 >= 400 or x1 < 0 or y1 > 300 or y1 < 0:
            dis.blit(massage("You stincc", white), 200, 150)
            time.sleep(2)
            game_over = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [200, 150, 10, 10])
        # pygame.time.Clock.tick(30)


pygame.quit()
quit()

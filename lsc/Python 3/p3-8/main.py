import time
import random
import pygame

pygame.init()
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

height, width = 400, 300
dis = pygame.display.set_mode((height, width))
pygame.display.update()
pygame.display.set_caption('Snake')

pygame.draw.rect(dis, blue, [200, 150, 10, 10])
pygame.display.update()

font_stlye = pygame.font.SysFont("Arial", 50)
clock = pygame.time.Clock()


def massage(msg: str, color: 'tuple(int, int, int)'):
    return font_stlye.render(msg, True, color)


def game_loop():
    snake_block = 22
    game_over = False

    x1 = 200
    y1 = 100

    x1_change = 0
    y1_change = 0

    foody = round(random.randint(0, height-snake_block))
    foodx = round(random.randint(0, 200 - snake_block))

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
        if x1 >= height or x1 < 0 or y1 > width or y1 < 0:
            dis.blit(massage("You stincc", white), 200, 150)
            time.sleep(2)
            game_over = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block])
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        if x1 == foodx and y1 == foody:
            print('yum')
        pygame.display.update()
        clock.tick(30)


game_loop()
pygame.quit()
quit()

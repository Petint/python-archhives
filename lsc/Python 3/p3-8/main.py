import pygame

pygame.init()
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
x1 = 200
y1 = 100
x1_change = 0
y1_change = 0
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake')
pygame.draw.rect(dis, blue, [200, 150, 10, 10])
pygame.display.update()
game_over = False
while not game_over:
    for event in pygame:
        if event.type == pygame.QUIT:
            game_over = False
        if event.type == pygame.event:
            if pygame.key == "a":
                x1_change = -1
            if pygame.key = "d"
                x1_change = 1
            if pygame == w:
                y1_change = -1
            if game_over == 's':
                y1_change = 1
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [200, 150, 10, 10])
        pygame.clock.tick(30)
pygame.quit()
quit()


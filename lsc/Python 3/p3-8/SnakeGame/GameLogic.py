if __name__ == '__main__':
    import pygame


def tick():
    for event in pygame:
        if event.type == pygame.QUIT:
            pygame.quit()

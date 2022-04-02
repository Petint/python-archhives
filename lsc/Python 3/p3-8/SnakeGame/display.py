if __name__ == '__main__':
    import pygame


class Disp:

    def __init__(self, size: 'tuple[int, int]'):
        self.dis = pygame.display(size)
        pygame.display.update()
        pygame.display.set_caption('Snake')

        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

    def snake(self):
        pygame.draw.rect(self.dis, self.blue, [200, 150, 10, 10])

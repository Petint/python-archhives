import pygame

pygame.init()
my_vec = pygame.math.Vector2
HEIGHT = 420
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

framsper = pygame.time.Clock()
disp_srf = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption('Platformer')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 40))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(10, 420))


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((0xff, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))

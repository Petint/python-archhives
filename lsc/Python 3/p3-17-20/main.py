from pygame import *

init()
my_vec = math.Vector2
HEIGHT = 450
WIDTH = 420
ACC = 0.5
FRIC = -0.12
FPS = 60

framsper = time.Clock()
disp_srf = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Platformer')


class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = Surface((30, 40))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(20, 410))
        self.pos = my_vec((10, 385))
        self.vel = my_vec(0, 0)
        self.acc = my_vec(0, 0)

    def move(self):
        self.acc = my_vec(0, 0)
        pressed_keys = key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + ACC * self.acc
        if self.pos.x > WIDTH:
            self.vel.x -= 20    # self.pos.x = 0
        if self.pos.x < 0:
            self.vel.x += 20    # self.pos.x = 0
        self.rect.midbottom = self.pos


class Platform(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = Surface((WIDTH, 20))
        self.surf.fill((0xff, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))


PT1 = Platform()  # Platform
PL1 = Player()    # Player

all_sprites = sprite.Group()
all_sprites.add(PT1)
all_sprites.add(PL1)

platforms = sprite.Group()
platforms.add(PT1)

while True:     # Main loop
    for evnt in event.get():
        if evnt.type == QUIT:
            quit()
    disp_srf.fill((0, 0, 0))

    for entity in all_sprites:
        disp_srf.blit(entity.surf, entity.rect)
    PL1.move()
    PL1.update()
    display.update()
    framsper.tick(FPS)

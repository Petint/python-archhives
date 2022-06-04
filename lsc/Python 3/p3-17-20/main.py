from pygame import *
from random import randint

init()
myVector = math.Vector2
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = time.Clock()
displaySurface = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Platformer")


class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(10, 420))

        self.pos = myVector((10, 385))
        self.vel = myVector(0, 0)
        self.acc = myVector(0, 0)

    def move(self):
        self.acc = myVector(0, 0.5)
        pressed_keys = key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

    def update(self):
        hits = sprite.spritecollide(P1, platforms, False)
        if hits and self.vel.y > 0:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0

        self.rect.midbottom = self.pos
        
    def jump(self):
        hits = sprite.spritecollide(P1, platforms, False)
        if hits:
            self.vel.y -= 15


class Platform(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT-10))


PT1 = Platform()
P1 = Player()

all_sprites = sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = sprite.Group()
platforms.add(PT1)

for _ in range(randint(4, 6)):
    pl = Platform()
    platforms.add(pl)
    all_sprites.add(pl)

while True:
    for evnt in event.get():
        if evnt.type == QUIT:
            quit()
        if evnt.type == KEYDOWN:
            if evnt.key == K_SPACE:
                P1.jump()
    displaySurface.fill((0, 0, 0))

    for entity in all_sprites:
        displaySurface.blit(entity.surf, entity.rect)
    P1.move()
    P1.update()
    display.update()
    FramePerSec.tick(FPS)

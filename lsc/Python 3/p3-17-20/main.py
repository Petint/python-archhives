from pygame import *
from random import randint, randrange
import sys
import time as tm


init()
myVector = math.Vector2
HEIGHT = 440
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
FramePerSec = time.Clock()
displaySurface = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Platformer")
background = image.load("assets/background.png")
background = transform.scale(background, (860, 480))


class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = transform.scale(image.load("assets/player.png"), (40, 40))
        self.rect = self.surf.get_rect(center=(10, 420))
        self.pos = myVector((10, 385))
        self.vel = myVector(0, 0)
        self.acc = myVector(0, 0)
        self.jumping = False
        self.score = 0

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
        self.rect.midbottom = self.pos

    def update(self):
        hits = sprite.spritecollide(P1, platforms, False)
        if hits and P1.vel.y > 0:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0
            self.jumping = False

    def jump(self):
        hits = sprite.spritecollide(P1, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3


class Platform(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = transform.scale(image.load("assets/platform.png"), (randint(50, 120), 18))
        self.rect = self.surf.get_rect(center=(randint(0, WIDTH - 10),
                                               randint(0, HEIGHT - 10)))
        self.speed = randint(-1, 1)
        self.moving = False

    def move(self):
        hits = self.rect.colliderect(P1.rect)
        if self.moving:
            self.rect.move_ip(self.speed, 0)
            if hits:
                P1.pos += (self.speed, 0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.left < 0:
                self.rect.left = WIDTH


def platform_generator():
    while len(platforms) < 7:
        width = randrange(50, 100)
        c = True
        while c:
            p = Platform()
            p.rect.center = (randrange(0, WIDTH - width), randrange(-50, 0))
            c = check(p, platforms)
            p.add(platforms, all_sprites)


def check(platform: Platform, groupies: sprite.Group):
    if sprite.spritecollideany(platform, groupies):
        return True
    else:
        for new_plat in groupies:
            if new_plat == platform:
                continue
            if (abs(platform.rect.top - new_plat.rect.bottom) < 40)\
                    and (abs(platform.rect.bottom - new_plat.rect.top) < 40):
                return True


platforms = sprite.Group()
all_sprites = sprite.Group()
PT1 = Platform()
PT1.surf = Surface((WIDTH, 20))
PT1.surf.fill((255, 0, 0))
PT1.rect = PT1.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))
PT1.moving = False
P1 = Player()
all_sprites.add(PT1)
all_sprites.add(P1)
platforms.add(PT1)

for x in range(randint(5, 6)):
    C = True
    pl = Platform()
    while C:
        pl = Platform()
        C = check(pl, platforms)
    platforms.add(pl)
    all_sprites.add(pl)

while True:
    for evnt in event.get():
        if evnt.type == QUIT:
            quit()
            sys.exit(0)
        if evnt.type == KEYDOWN:
            if evnt.key == K_SPACE:
                P1.jump()
        if evnt.type == KEYUP:
            if evnt.key == K_SPACE:
                P1.cancel_jump()
    displaySurface.blit(background, (-50, 0))
    f = font.SysFont("Verdana", 20)
    g = f.render(str(P1.score), True, (0, 0, 0))
    displaySurface.blit(g, (WIDTH/2, 10))
    if P1.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
            tm.sleep(0.1)
            displaySurface.fill((255, 0, 0))
            display.update()
            tm.sleep(0.1)
            quit()
            sys.exit(0)
    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                P1.score += 1
                plat.kill()
    P1.update()
    platform_generator()
    for entity in all_sprites:
        displaySurface.blit(entity.surf, entity.rect)
        entity.move()
    display.update()
    FramePerSec.tick(FPS)

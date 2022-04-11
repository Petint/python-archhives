# Import stuff
import os.path
import random
import pygame
import math


# Defining global vars
pygame.font.init()
WIDTH = 900     # Screen size
HEIGHT = 600
BRDR = pygame.Rect((WIDTH // 2) - 5, 0, 10, HEIGHT,)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space fight")
SSS = (80, 60)  # SpaceShipSize
REDHIT = pygame.USEREVENT + 1
YELHIT = pygame.USEREVENT + 2
WHITE = (0xff, 0xff, 0xff)
YEE = (0xff, 0xff, 0)
RED = (0xff, 0, 0)
BLACC = (0, 0, 0)
SHOOTSPEED = 7
MAX_BLTS = 3
YHLT = 10
RHLT = 10
FPS = 60
VEL = 10


# Loading assets
YSSS = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RSSS = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
PICTURE = pygame.image.load(os.path.join('Assets', 'space.png'))
METPIC = pygame.image.load(os.path.join('Assets', 'meteor.png'))
HPFONT = pygame.font.SysFont('Arial', 40)  #  Font(os.path.join('Assets', 'ds-digitb'), 40)
WNRFNT = pygame.font.SysFont('Arial', 80)

# Creating objects
SPACESHIP_YE = pygame.transform.rotate(pygame.transform.scale(YSSS, SSS), 90)
SPACESHIP_RE = pygame.transform.rotate(pygame.transform.scale(RSSS, SSS), -90)
SPACE_BG = pygame.transform.scale(PICTURE, (WIDTH, HEIGHT))
METTY = pygame.transform.rotate(METPIC, random.randint(0, 360))



def draw(red, yel, _by, _br, _rh, _yh):
    """GaphX subsystem"""

    # Draw game
    WINDOW.blit(SPACE_BG, (0, 0))
    _rht = HPFONT.render(f"Health: {_rh}", True, WHITE)
    _yht = HPFONT.render(f"Health: {_yh}", True, WHITE)
    pygame.draw.rect(WINDOW, BLACC, BRDR)
    WINDOW.blit(_rht, (WIDTH - _rht.get_width() - 10, 10))
    WINDOW.blit(_yht, (10, 10))
    WINDOW.blit(SPACESHIP_YE, (yel.x, yel.y))
    WINDOW.blit(SPACESHIP_RE, (red.x, red.y))
    # Draw bullets
    for y in _by:  # Yellow
        pygame.draw.rect(WINDOW, YEE, y)
    for r in _br:  # Red
        pygame.draw.rect(WINDOW, RED, r)
    pygame.display.update()


def ycon(keys_pressed, yel):
    """Yellow's controlls"""
    if keys_pressed[pygame.K_a] and yel.x - VEL > 0:
        yel.x -= VEL
    if keys_pressed[pygame.K_w] and yel.y + VEL > 0:
        yel.y -= VEL
    if keys_pressed[pygame.K_s] and yel.y - VEL + yel.height < HEIGHT:
        yel.y += VEL
    if keys_pressed[pygame.K_d] and yel.x + VEL + yel.width < HEIGHT:
        yel.x += VEL


def rcon(keys_pressed, red):
    """Red's controlls"""
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BRDR.x:
        red.x -= VEL
    if keys_pressed[pygame.K_UP] and red.y + VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y - VEL + red.height < HEIGHT:
        red.y += VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width + 10 < WIDTH:
        red.x += VEL


def bullethandler(_rblt: list, _yblt: list, _yel, _red):
    """"Bullet handeler for players --Make bullets work--"""

    # Yellow's bullets
    for bullet in _yblt:
        bullet.x += SHOOTSPEED
        if _red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(REDHIT))
            _yblt.remove(bullet)
        if bullet.x > WIDTH:
            _yblt.remove(bullet)

    # Red's bullets
    for bullet in _rblt:
        bullet.x -= SHOOTSPEED
        if _yel.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELHIT))
            _rblt.remove(bullet)
        if bullet.x < 0:
            _rblt.remove(bullet)


def drawwinner(_wtxt):
    _dtxt = WNRFNT.render(_wtxt, True, WHITE)
    WINDOW.blit(_dtxt, (WIDTH // 2 - _dtxt.get_width() // 2, HEIGHT // 2 - _dtxt.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(50000)


def keyhandler(event, yelcart, yellow, red, redcart):
    if event.key == pygame.K_LCTRL and len(yelcart) < 3:
        blt = pygame.Rect(yellow.x + yellow.height, yellow.centery, 10, 5)  # Make bullet
        yelcart.append(blt)
    if event.key == pygame.K_RCTRL and len(redcart) < 3:
        blt = pygame.Rect(red.x - 5, red.centery, 10, 5)  # Make bullet
        redcart.append(blt)


def main():
    """Maintilope"""

    # Players
    red = pygame.Rect((WIDTH / 2 + WIDTH / 4) - 60, HEIGHT / 2 - 60, SSS[0], SSS[1])
    yellow = pygame.Rect((WIDTH / 2 - WIDTH / 4) - 60, HEIGHT / 2 - 60, SSS[0], SSS[1])
    redlife = 10
    yellife = 10
    # Bullets
    yelcart = []
    redcart = []
    clock = pygame.time.Clock
    winner_txt = ""
    run = True
    while run:
        # clock.tick(clock, FPS)
        for event in pygame.event.get():  # Turn to method
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:  # Code for bullet
                keyhandler(event, yelcart, yellow, red, redcart)
            if event.type == REDHIT:
                redlife -= 1
            if event.type == YELHIT:
                yellife -= 1
        if yellife <= 0:
            winner_txt = "RED WON!"
        if redlife <= 0:
            winner_txt = "YELLOW WON!"
        if winner_txt != "":
            drawwinner(winner_txt)
            break
        keys_pressed = pygame.key.get_pressed()
        ycon(keys_pressed, yellow)
        rcon(keys_pressed, red)
        bullethandler(redcart, yelcart, yellow, red)
        draw(red, yellow, yelcart, redcart, redlife, yellife)
    pygame.font.quit()
    pygame.quit()


# Python s#!t
if __name__ == "__main__":
    main()

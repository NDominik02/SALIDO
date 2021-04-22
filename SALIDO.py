import pygame
import random
# Kijelző

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
done = False
#x/y a piros kocka helyzete, a t/z a kék kockáé, x_2 / y_2 pedig a szürke kocka amit el kell kapni
x = 480
y = 270
t = 1440
z = 810
x_2 = random.randint(50, 1870)
y_2 = random.randint(50, 1030)
#háttérkép + fullscreen
background = pygame.image.load("unnamed.jpg")
# DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#Textek
font = pygame.font.SysFont("comicsansms", 36)
pontszam_text = font.render("R: ", True, (204, 0, 0))
pontszamB_text = font.render("B: ", True, (0, 0, 250))
ujra_text = font.render("ÚJRAKEZDÉS", True, (0, 0, 0))
exitfont = pygame.font.SysFont("comicsansms", 36)
exit_text = exitfont.render("X", True, (255, 0, 0))
piros_text = font.render("PIROS NYERT", True, (204, 0, 0))
kek_text = font.render("KÉK NYERT", True, (0, 0, 250))

ido = 0
pontszam = 0
pontszamB = 0

while not done:
#irányítás NYILAK RED, WASD KÉK
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 15
    if pressed[pygame.K_DOWN]:
        y += 15
    if pressed[pygame.K_LEFT]:
        x -= 15
    if pressed[pygame.K_RIGHT]:
        x += 15

    if y < 0:
        y += 1080
    if y > 1020:
        y -= 1080
    if x < 0:
        x += 1920
    if x > 1890:
        x -= 1920


    if pressed[pygame.K_w]:
        z -= 15
    if pressed[pygame.K_s]:
        z += 15
    if pressed[pygame.K_a]:
        t -= 15
    if pressed[pygame.K_d]:
        t += 15

    if z < 0:
        z += 1080
    if z > 1020:
        z -= 1080
    if t < 0:
        t += 1920
    if t > 1890:
        t -= 1920
#háttér
    screen.blit(background, [0, 0])
#Kilépés BAL KLIKKEL
    exit = screen.blit(exit_text, (1880 , 0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and exit.collidepoint(pygame.mouse.get_pos()):
            done = True

    if pontszam < 2 and pontszamB < 2:
        a = pygame.draw.rect(screen, ( 204, 0, 0),(x, y, 30, 30))
        b = pygame.draw.circle(screen, (128, 128, 128), (x_2, y_2), 10)

        c = pygame.draw.rect(screen, (0, 0, 250), (t, z, 30, 30))

        if a.colliderect(b):
            pontszam += 1
            x_2 = random.randint(50, 1870)
            y_2 = random.randint(50, 1030)
            pygame.display.update(b)

        if c.colliderect(b):
            pontszamB += 1
            x_2 = random.randint(50, 1870)
            y_2 = random.randint(50, 1030)
            pygame.display.update(b)

#pontszám szöveg + szám helye + pontSZÁM színe
        screen.blit(pontszam_text, (16, 1020))
        screen.blit(pontszamB_text, (1840, 1020))
        pontszamB_text2 = font.render(str(pontszamB), True, (0, 0, 250))
        screen.blit(pontszamB_text2, (pontszam_text.get_width() + 1835, 1020))

        pontszam_text2 = font.render(str(pontszam), True, (222, 30, 30))
        screen.blit(pontszam_text2, (pontszam_text.get_width() + 10, 1020))
    else: #újrakezdés helye
# KI NYERT? FELIRAT
        if pontszam > pontszamB:
            p = screen.blit(piros_text, (840, 300))
        else:
            p = screen.blit(kek_text, (840, 300))

        u = screen.blit(ujra_text, (840, 370))
#ÚJRAKEZDÉS KATTINTÁSSAL
        if u.collidepoint(pygame.mouse.get_pos()):
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                pontszam = 0
                pontszamB = 0


    pygame.display.flip()
    pygame.time.Clock().tick(60)

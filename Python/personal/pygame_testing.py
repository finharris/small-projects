import pygame
pygame.init()
import time

win_width = 500
win_height = 400

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pygame Testing")

clock = pygame.time.Clock()



x = 50
y = 325
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < win_width - width:
        x += vel

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1

            y -= (jumpCount ** 2) / 2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    
    clock.tick(60)


pygame.quit()

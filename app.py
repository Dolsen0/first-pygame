import pygame

pygame.init()

background = (0,100,200)
player = (255,255,255)

canvas = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Ready?")
exit = False

while not exit:
    canvas.fill(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()
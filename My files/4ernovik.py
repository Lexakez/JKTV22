import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((1900, 1000))

font = pygame.font.SysFont('arial', 100)

test = True

pygame.display.set_caption("")

vector = [1, 1]


color = 255

x = 1
y = 50



while test:
    a, b, c = randint(0, 255), randint(0, 255), randint(0, 255)
    window.fill((a, b, c))

    cord = [1, 50]

    pygame.draw.rect(window, (a, b, c), (x, y, 200, 60))

    x += vector[0]
    y += vector[1]
    a, b, c = randint(0, 255), randint(0, 255), randint(0, 255) 
    if y + 60 >= 1000 or y <= 0:
        vector[1] *= -1
        # a = randint(0, 255)
        # b = randint(0, 255)
        # c = randint(0, 255)
    
    if x + 200 >= 1900 or x <= 0:
        vector[0] *= -1
        # a = randint(0, 255)
        # b = randint(0, 255)
        # c = randint(0, 255)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test = False

    text = font.render("DVD", True, (c, a, b))
    window.blit(text, (x, y))

    pygame.display.update()
pygame.quit()

import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((1900, 1000))

test = True

pygame.display.set_caption("")

vector = [1, 1]

platform_cord = [950, 900]
platform_razmer = [100, 10]
color = 255
razmer = [150, 110, 5]
kvadrat = True

while test:
    window.fill((0, 0, 0))
    pygame.draw.circle(window, (0, 255, 0), (razmer[0], razmer[1]), razmer[2])
    razmer[0] += vector[0]
    razmer[1] += vector[1]

    if razmer[1] - razmer[2] <= 0 or (razmer[1] + razmer[2]) >= 1000:
        vector[1] *= -1      
    if razmer[0] - razmer[2] <= 0 or (razmer[0] + razmer[2]) >= 1900:
        vector[0] *= -1

    if razmer[1] + razmer[2] >= 900 and (razmer[0] + razmer[2] >= platform_cord[0] and razmer[0] - razmer[2] <= platform_cord[0] + platform_razmer[0]):
        vector[1] *= -1
    


    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        platform_cord[0] += 8
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        platform_cord[0] -= 8
    pygame.draw.rect(window, (255, 0, 0), (platform_cord, platform_razmer))

    if kvadrat:
        pygame.draw.rect(window, (0, 0, 255), (0, 0, 470, 100))
    # pygame.draw.rect(window, (0, 0, color), (475, 0, 470, 100))
    # pygame.draw.rect(window, (0, 0, color), (950, 0, 470, 100))
    # pygame.draw.rect(window, (0, 0, color), (1425, 0, 470, 100))
    
    if razmer[1] - razmer[2] <= 100 and razmer[0] <= 470 and kvadrat:
        
        vector[1] *= -1

        kvadrat = False



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test = False
    pygame.time.delay(5)
    pygame.display.update()
pygame.quit()

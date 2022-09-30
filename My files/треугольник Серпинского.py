import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((1900, 1000))

iterations = 0
font = pygame.font.SysFont('arial', 20)

test = True
A, B, C = (900, 100), (300, 900), (1500, 900)
top_list = [A, B, C]
start_point = A
point_list = []
pygame.display.set_caption("Serpinsky triangle")
while test:
    window.fill((0, 0, 0))
    for top in top_list:
        pygame.draw.circle(window, (0, 255, 0), top, 2)
    end_point = top_list[randint(0, 2)]
    end_point = ((end_point[0] + start_point[0]) / 2,(end_point[1] + start_point[1]) / 2,)
    end_point += ((randint(0, 255), randint(0, 255), randint(0, 255)),)
    point_list.append(end_point)
    start_point = end_point
    for point in point_list:
        pygame.draw.circle(window, point[2], (point[0], point[1]), 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test = False
    iterations += 1
    text = font.render(f"Количество итераций: {iterations}", True, (0, 255, 0))
    window.blit(text, (0, 0))
    pygame.display.update()
pygame.quit()

import pygame
pygame.init()

test = True

x = 1

y = 600

point_list = []

start_point = [x, y]

win = pygame.display.set_mode((600, 600))

while test:
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test = False
    
    next_point = [start_point[0] + 1, 100 / (start_point[0] / 100)]

    

    for point in point_list:
        pygame.draw.circle(win, (0, 255, 255), (point[0], point[1]), 2)

    point_list.append(next_point)

    start_point = next_point



    pygame.time.delay(50)

    pygame.display.update()

pygame.quit()
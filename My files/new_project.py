import pygame
pygame.init()

window = pygame.display.set_mode((1000, 750))
run = True

font = pygame.font.SysFont('arial', 20)

shuttle = [490, 650, 20, 50]

bullet_list = []

bullet_delay_temp = 0
bullet_delay_temp2 = 0
bullet_delay = 1000

gun_queue = 1

energy = 200

color1 = 0
color = 0

while run:
    window.fill((0, 0, 0))

# Отрисовка кабины корабля  
    pygame.draw.rect(window, (0, 100, 100), shuttle )

# Передвижение корабля

    if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
        shuttle[0] += 0.5
    if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
        shuttle[0] -= 0.5

    if shuttle[1] >= 500:
        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
            shuttle[1] -= 0.5

    if shuttle[1] <= 700:
        if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
            shuttle[1] += 0.5

# Части коробля

    L_wing = [shuttle[0] - 10, shuttle[1] + 25, 10, 20]
    R_wing = [shuttle[0] + 20, shuttle[1] + 25, 10, 20]
    L_gun = [L_wing[0] - 1, L_wing[1] + 20, L_wing[0] - 1, L_wing[1] - 20, 3]
    R_gun = [R_wing[0] + 10, R_wing[1] + 20, R_wing[0] + 10, R_wing[1] - 20, 3]


# Отрисовка частей коробля 

    pygame.draw.rect(window, (0, 80, 90), L_wing)
    pygame.draw.rect(window, (0, 80, 90), R_wing)
    pygame.draw.line(window, (0, 90, 80), (L_gun[0], L_gun[1]), (L_gun[2], L_gun[3]), L_gun[4])
    pygame.draw.line(window, (0, 90, 80), (R_gun[0], R_gun[1]), (R_gun[2], R_gun[3]), R_gun[4])

# Телепорт по краям экрана

    if L_gun[0] <= 0:
        shuttle[0] = 970
    elif R_gun[0] >= 1000:
        shuttle[0] = 12

# Выстрел
    
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        if bullet_delay_temp <= 0 and gun_queue == 1 and bullet_delay_temp2 <= 1 and energy > 10:
            bullet_list.append([L_gun[0], L_gun[1] - 20, L_gun[0], L_gun[1] - 30])
            bullet_delay_temp = bullet_delay
            gun_queue = 0
            energy -= 10


        if bullet_delay_temp2 <= 0 and gun_queue == 0 and bullet_delay_temp <= 1 and energy > 10:
            bullet_list.append([R_gun[0], R_gun[1] - 20, R_gun[0], R_gun[1] - 30])
            bullet_delay_temp2 = bullet_delay
            gun_queue = 1
            energy -= 10 


    for bullet in bullet_list:
        pygame.draw.line(window, (0, 255, 0), (bullet[0], bullet[1]), (bullet[2], bullet[3]), 3)
        bullet[1] -= 0.5
        bullet[3] -= 0.5

        if bullet[3] < 0:
            bullet_list.remove(bullet) 

# Энергия на выстрел

    pygame.draw.rect(window, (0, 155, 155), (0, 0, 200, 40), 1)

    pygame.draw.rect(window, (color, color1, 0), (3, 3, 200 * energy / 200 - 6, 34) )
    if energy > 150:
        color1 = 255
        color = 0

    elif energy < 60:
        color1 = 0
        color = 255


    # print(shuttle, L_wing, R_wing)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    bullet_delay_temp -= 1
    bullet_delay_temp2 -= 1
    if energy < 200:
        energy += 0.005

    text = font.render("ENERGY", True, (230, 200, 155))
    window.blit(text, (60, 10))

    print(energy)
    pygame.display.update()
pygame.quit()
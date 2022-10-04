import pygame
from random import randint
pygame.init()


window = pygame.display.set_mode((1000, 750))

run = True

font = pygame.font.SysFont('colibri', 40)

shuttle = [490, 650, 20, 50]

bullet_list = []

bullet_delay_temp = 0

bullet_delay_temp2 = 0

bullet_delay = 10

gun_queue = 1

energy = 200

energy_regen = 0.3

energy_color_green = 0

energy_color_red = 0

FPS = 60

meteor_list = []

meteor_speed = [10, 10]

meteor = [475, 10, 50, 50]

meteor_list.append(meteor[:])

frag = 0

health = 100

while run:
    window.fill((0, 0, 0))

# Передвижение корабля

    if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
        shuttle[0] += 8
    if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
        shuttle[0] -= 8
    if shuttle[1] >= 500:
        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
            shuttle[1] -= 8
    if shuttle[1] <= 700:
        if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
            shuttle[1] += 8

# Части коробля

    L_wing = [shuttle[0] - 10, shuttle[1] + 25, 10, 20]
    R_wing = [shuttle[0] + 20, shuttle[1] + 25, 10, 20]
    L_gun = [L_wing[0] - 1, L_wing[1] + 20, L_wing[0] - 1, L_wing[1] - 20, 3]
    R_gun = [R_wing[0] + 10, R_wing[1] + 20, R_wing[0] + 10, R_wing[1] - 20, 3]

# Телепорт по краям экрана

    if L_gun[0] <= 0:
        shuttle[0] = 970
    elif R_gun[0] >= 1000:
        shuttle[0] = 12

# Здоровье

    pygame.draw.rect(window, (0, 155, 155), (794, 0, 206, 40), 1)
    pygame.draw.rect(window,(0, 255, 0),(797, 3, 200 * health / 100, 34))

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
        bullet[1] -= 10
        bullet[3] -= 10

        if bullet[3] < 0:
            bullet_list.remove(bullet) 

# Энергия на выстрел

    pygame.draw.rect(window, (0, 155, 155), (0, 0, 206, 40), 1)

    pygame.draw.rect(window, (energy_color_red, energy_color_green, 10), (3, 3, 200 * energy / 200, 34))
    if energy > 150:
        energy_color_green = 255
        energy_color_red = 0

    elif energy < 60:
        energy_color_green = 0
        energy_color_red = 255

    text = font.render("ENERGY", True, (255, 255, 255))
    window.blit(text, (45, 9))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    bullet_delay_temp -= 1
    bullet_delay_temp2 -= 1
    if energy < 200:
        energy += energy_regen

# Отрисовка частей коробля 

    pygame.draw.rect(window, (0, 80, 90), L_wing)
    pygame.draw.rect(window, (0, 80, 90), R_wing)
    pygame.draw.line(window, (0, 90, 80), (L_gun[0], L_gun[1]), (L_gun[2], L_gun[3]), L_gun[4])
    pygame.draw.line(window, (0, 90, 80), (R_gun[0], R_gun[1]), (R_gun[2], R_gun[3]), R_gun[4])

# Отрисовка кабины корабля  

    pygame.draw.rect(window, (0, 100, 100), shuttle )

# Отрисовка врагов

    for enemy in meteor_list:
        pygame.draw.rect(window, (160, 160, 160), (enemy[0], enemy[1], enemy[2], enemy[3]))
        enemy[1] += 2

        if enemy[1] >= 710:
            meteor_list.remove(enemy)
            meteor[0] = randint(0, 950)
            meteor_list.append(meteor[:])
            health -= 10

    if health == 0:
        run = False

    print(meteor_list)

# Уничтожение врага

    for bullet in bullet_list:
        for enemy in meteor_list:
            if enemy[1] + 50 > bullet[3] and enemy[1] < bullet[3] and enemy[0] + 50 > bullet[0] and enemy[0] < bullet[0]:
                bullet_list.remove(bullet)
                meteor_list.remove(enemy)
                meteor[0] = randint(0, 950)
                meteor_list.append(meteor[:])
                
                if frag == 3:
                    meteor[0] = randint(0, 950)
                    meteor_list.append(meteor[:])
                frag += 1
    
    print(bullet_list)

    text = font.render(f"Enemy destoyed : [{frag}]", True, (230, 200, 155))
    window.blit(text, (350, 10))

# Прицел

    pygame.draw.line(window, (0, 100, 0), (shuttle[0], shuttle[1] - 400), (shuttle[0] + 20, shuttle[1] - 400), 1)
    pygame.draw.line(window, (0, 100, 0), (shuttle[0] + 10 , shuttle[1] - 410), (shuttle[0] + 10, shuttle[1] - 390), 1)
    




#====
    pygame.display.update()
    pygame.time.Clock().tick(FPS)


pygame.quit()
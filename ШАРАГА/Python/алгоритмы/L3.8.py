hours = int(input("Введите количество часов: "))

minut = int(input("Введите количество минут: "))

sec = int(input("Введите количество секунд: "))

minut = minut * 60

hours = hours * 3600

dig = ((sec + minut + hours) * 36) / 4320

print(f"Часовая стрелка прошла {round(dig, 2) % 360} градусов")
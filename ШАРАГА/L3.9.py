deg = int(input("Введите сколько градусов прошла часовая стрелка: "))

deg = deg % 30

minut = deg * 12 

print(minut)
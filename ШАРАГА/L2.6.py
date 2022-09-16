time = int(input("Введите время в минутах: "))

time %= 1440

hours = time // 60

minutes = time % 60

if minutes < 10:
    minutes = "0" + str(minutes)

if hours < 10:
    hours = "0" + str(hours)

print(f"{hours}:{minutes}")
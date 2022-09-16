from math import ceil

carkm = int(input("Введите сколько киллометров в день может проехать машина:"))

km = int(input("Введите длинну маршрута в километрах:"))

days = km / carkm

days = ceil(days)

pad = days % 100

if pad >= 10 and pad <= 20:
    print(f"Машина проедет это растояние за {days} дней")
elif pad < 10 or pad > 20:
    pad %= 10
    if pad == 1:
        print(f"Машина проедет это растояние за {days} день")
    elif pad > 1 and pad < 5:
        print(f"Машина проедет это растояние за {days} дня")
    else:
        print(f"Машина проедет это растояние за {days} дней")


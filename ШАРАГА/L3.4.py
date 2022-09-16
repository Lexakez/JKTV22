from math import ceil
carkm = int(input("Введите сколько киллометров в день может проехать машина:"))

km = int(input("Введите длинну маршрута в километрах:"))

days = km / carkm

days = ceil(days)

print(f"машина проедет это растояние за: {days} days")


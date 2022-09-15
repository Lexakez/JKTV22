from math import ceil

c1 = int(input("Students in first class: "))
c2 = int(input("Students in second class: "))
c3 = int(input("Students in third class: "))

# Первый вариант

bc1 = (c1 // 2) + (c1 % 2) \
      + (c2 // 2) + (c2 % 2) \
      + (c3 // 2) + (c3 % 2)

print(f"Парт надо закупить {bc1}")

# Второй вариант

bc2 = (ceil(c1 / 2)) + (ceil(c2 / 2)) + (ceil(c3 / 2))

print(f"Парт надо закупить: {bc2}")

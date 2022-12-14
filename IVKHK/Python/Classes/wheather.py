

arr = []

with open("weather.txt", "r+") as file:
    pogoda = file.readlines()
    for day in pogoda:
        arr.append([day])

print(arr)
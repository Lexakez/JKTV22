pogoda_list = []

with open("weather.txt", "r+") as file:
    pogoda = file.readlines()
    for den in pogoda:
        pogoda_list.append(den.split(","))


class Weather:

    def __init__(self, city, day, temp):
        self.__city = city
        self.__day = day
        self.__temp = temp
    
    def set_city(self, city):
        self.__city = city

    def set_day(self, day):
        self.__day = day

    def set_temp(self, temp):
        self.__temp = temp

print(pogoda_list)
print(pogoda_list[0][1])

weather_list = []

for i in pogoda_list:
    # print(pogoda_list[i][1])
    Weather.set_city(i[1])
    Weather.set_day(i[0])
    Weather.set_temp(i[2])
weather_list.append(Weather)
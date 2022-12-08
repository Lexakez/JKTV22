class Person:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def printInfo(self):
        print(self.name,"Isikukood", self.code)

    def printGender(self):
        s = self.code[0]
        if s == "3" or s == "5":
            print("mees")
        else:
            print("naine")
            
    def birthDay(self):
        kood = self.code
        if kood[0] == str(3) or kood[0] == str(5):
            print("Пол: Мужчина")
        elif kood[0] == str(4) or kood[0] == str(6):
            print("Пол: Женщина")
        print(f"Дата рождения: {kood[5: 7]}.{kood[3: 5]}.{kood[1: 3]}")
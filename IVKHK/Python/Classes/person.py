from classes import Person

person1 = Person("Anna", "40101912248")
person2 = Person("Andrei", "50308283341")

persons = []

persons.append(person1)
persons.append(person2)

for p in persons:
    p.printInfo()
    p.printGender()
    p.birthDay()
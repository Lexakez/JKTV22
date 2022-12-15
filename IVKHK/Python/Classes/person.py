from classes import Person,Employee

person1 = Person("Anna", "40101912248")
person2 = Person("Andrei", "50308283341")

persons = []

persons.append(person1)
persons.append(person2)
persons.append(Employee("Kirill", "50209195523", "VKG"))

for p in persons:
    p.printInfo()
    p.printGender()
    p.birthDay()
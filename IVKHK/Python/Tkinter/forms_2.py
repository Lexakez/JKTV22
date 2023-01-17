from tkinter import *
import ttk
import csv

root = Tk()

def click_lisa():
    student_name = text_nimi.get()
    student_code = text_kood.get()
    if int(keel.get()) == 2:
        student_language = "Vene"
    else:
        student_language = "Eesti"
    student_course = koolitus_text.get()
    if algteadmised.get() == 1:
        student_knowledge = "On"
    elif algteadmised.get() == 0:
        student_knowledge = "Ei ole"


    student = {
        'Nimi': student_name,
        'Isikukood': student_code,
        'Keel': student_language,
        'Koolitus': student_course,
        'Algteadmised': student_knowledge
    }
    

    enter_nimi.delete(0, END)
    enter_kood.delete(0, END)
    keel.set(0)
    koolitus_text.set(None)
    algteadmised.set(0)


    print(student)
    students_count = len(koolitused.students)
    students_count_label.config(text=f'Number of students: {students_count}')
    koolitused.add_student(student)

class Koolitused:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def save_to_file(self):
        with open('students.csv', "w",newline = '') as file:
            columns = ["Nimi", "Isikukood", "Keel", "Koolitus", "Algteadmised"]
            writer = csv.DictWriter(file, fieldnames = columns)
            writer.writeheader()
            writer.writerows(self.students)

        

koolitused = Koolitused()



root.title("Form")
root.geometry("500x500")

Nimi = Label(
    text = "Sisestage nimi ja isikukood:",
    font = "15"
)

text_nimi = StringVar()
text_kood = StringVar()

enter_nimi = Entry(
    textvariable = text_nimi,
    width = "34"
)

enter_kood = Entry(
    textvariable = text_kood,
    width = "34"
)

Keel = Label(
    text = "Keel: ",
    font = "15"
)

keel = IntVar()

Eesti_checkbtn = Radiobutton(
    text = "Eesti",
    value = 1,
    font = "15",
    variable = keel
)

Vene_checkbtn = Radiobutton(
    text = "Vene",
    value = 2,
    font = "15",
    variable = keel
)

koolitus = Label(
    text = "Vali koolitus: ",
    font = "15"
)

koolitused_list = ["Python", "Java", "AutoCad", "SolidWorks"]

koolitus_text = StringVar()

koolitused_box = ttk.Combobox(
    values = koolitused_list,
    width = 10,
    textvariable = koolitus_text
)

algteadmised = IntVar()

algteadmised_checkbtn = Checkbutton(
    text = "On olemas algteadmised",
    font = 15,
    variable = algteadmised
)

btnLisa = Button(
    text = "Lisa",
    command = click_lisa
)

students_count_label = Label(
    text = "Number of students: 1",
    font = "15"
)

btnSalvesta = Button(
    text = "Salvesta",
    command = koolitused.save_to_file
)

def draw():
    '''Расположение элементов.'''
    Nimi.grid(
        row = 0,
        column = 0,
        sticky = "w",
        padx = 10
    )
    enter_nimi.grid(
        row = 1,
        column = 0,
        sticky = "w",
        padx = 10
    )
    enter_kood.grid(
        row = 1,
        column = 0,
        sticky = "w",
        padx = 225
    )
    Keel.grid(
        row = 3,
        column = 0,
        sticky = "w",
        padx = 10
    )
    Vene_checkbtn.grid(
        row = 4,
        column = 0,
        padx = "10",
        sticky = "w"
    )
    Eesti_checkbtn.grid(
        row = 4,
        column = 0,
        padx = "75",
        sticky = "w"
    )
    koolitus.grid(
        row = 5,
        column = 0,
        sticky = "w",
        padx = 10
    )
    koolitused_box.grid(
        row = 5,
        column = 0,
        sticky = "w",
        padx = 110
    )
    algteadmised_checkbtn.grid(
        row = 6,
        column = 0,
        sticky = "w",
        padx = 10
    )
    btnLisa.grid(
        row = 7,
        column = 0,
        sticky = "w",
        padx = 10
    )
    students_count_label.grid(
    row = 9,
    column = 0,
    sticky = "w",
    padx = 10
    )
    btnSalvesta.grid(
    row = 8,
    column = 0,
    sticky = "w",
    padx = 10
    )

draw()

root.mainloop()


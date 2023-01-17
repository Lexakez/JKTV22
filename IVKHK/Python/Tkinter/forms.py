from tkinter import *

root = Tk()

root.title("Forms")
root.geometry("500x500")


def click_salvesta():
    with open("inimesed.txt", "w") as file:
        file.write(f"{entnimi.get()} {entkood.get()} {entruhm.get()}")

Nimi = Label(
    text = "Nimi: ",
    font = "20"
)

entnimi = StringVar()
textnimi = Entry(textvariable = entnimi)

Isikukood = Label(
    text = "Isikukood: ",
    font = "20"
)

entkood = StringVar()
textkood = Entry(textvariable = entkood)

Ruhm = Label(
    text = "Rühm: ",
    font = "20"
)

entruhm = StringVar()
textruhm = Entry(textvariable = entruhm)

btnSalvesta = Button(
    text = "Salvesta",
    relief = "groove",
    command = click_salvesta
)


Nimi.grid(row = 0, column = 0, sticky = "w", padx = 10)
textnimi.grid(row = 1, column = 0, sticky = "w", padx = 10)
Isikukood.grid(row = 2, column = 0, sticky = "w", padx = 10)
textkood.grid(row = 3, column = 0, sticky = "w", padx = 10)
Ruhm.grid(row = 4, column = 0, sticky = "w", padx = 10)
textruhm.grid(row = 5, column = 0, sticky = "w", padx = 10)
btnSalvesta.grid(row = 6, column = 0, sticky = "w", padx = 10)




root.mainloop()
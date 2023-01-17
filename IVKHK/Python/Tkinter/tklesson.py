from tkinter import *

root = Tk()

root.title("Графическая программа на Python")
root.geometry("400x300")

count = 0

def click_button():
    global count
    count += 1
    print(count)

def click_button2():
    global count
    count += 1
    btext.set(str(count))
    print(count)

# def click_message():


btn = Button(text = "Hello",
            background = "#772",
            foreground = "#481",
            font = "10",
            command = click_button)

btext = StringVar()
btext.set(str("click Here"))

btn_2 = Button(textvariable = btext,
            background = "#772",
            foreground = "#481",
            font = "10",
            command = click_button2)

message =StringVar()
textentry = Entry(textvariable = message)

textentry.grid(row = 0, column = 0, sticky= 'w')

btn.grid(row = 0, column = 1, sticky = "w")
# btn_2.pack()

root.mainloop()
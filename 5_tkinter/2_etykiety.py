from tkinter import *

window = Tk()

window.geometry('800x600')

window.title("Witaj w aplikacji!")

lbl = Label(window, text="Witaj Świecie!", font=("Arial Bold", 50), fg="blue")

lbl.grid(column=0, row=0)

window.mainloop()

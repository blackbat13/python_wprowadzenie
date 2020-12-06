from tkinter import *

window = Tk()

window.geometry('800x600')

window.title("Witaj w aplikacji!")

lbl = Label(window, text="Witaj Świecie!", font=("Arial Bold", 50), fg="blue")

lbl.grid(column=0, row=0)


def klik():
    lbl.configure(text="Kliknięto przycisk!!")


btn = Button(window, text="Kliknij!", font=("Arial Bold", 30), bg="black", fg="white", command=klik)

btn.grid(column=2, row=2)

window.mainloop()

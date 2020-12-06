from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

window.geometry('800x600')

window.title("Witaj w aplikacji!")

lbl = Label(window, text="Witaj Świecie!", font=("Arial Bold", 25), fg="blue")

lbl.grid(column=0, row=0)

txt = Entry(window, width=10, font=("Arial Bold", 25))

txt.grid(column=0, row=4)

txt.focus()

combo = Combobox(window)

combo['values'] = (1, "Mleko", 3, "Jabłko", 5)

combo.current(1)

combo.grid(column=0, row=5)

def klik():
    lbl.configure(text=f"Wpisano: {txt.get()}, wybrano: {combo.get()}")


btn = Button(window, text="Kliknij!", font=("Arial Bold", 30), bg="black", fg="white", command=klik)

btn.grid(column=2, row=2)

window.mainloop()

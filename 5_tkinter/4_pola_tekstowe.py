from tkinter import *

window = Tk()

window.geometry('800x600')

window.title("Witaj w aplikacji!")

lbl = Label(window, text="Witaj Świecie!", font=("Arial Bold", 50), fg="blue")

lbl.grid(column=0, row=0)

txt = Entry(window, width=10, font=("Arial Bold", 25))

txt.grid(column=0, row=4)

txt.focus()

# txt.insert(0, "Hello")

# txt["state"] = "disabled"


def klik():
    lbl.configure(text=f"Wpisano: {txt.get()}")


btn = Button(window, text="Kliknij!", font=("Arial Bold", 30), bg="black", fg="white", command=klik)

btn.grid(column=2, row=2)

window.mainloop()

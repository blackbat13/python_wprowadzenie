from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter.ttk import Combobox, Checkbutton


def klik():
    lbl.configure(
        text=f"Wpisano: {txt.get()}, wybrano: {combo.get()}, zaznaczony: {chk_state.get()}, radio: {selected.get()}, textarea: {scrtxt.get('1.0', 'end-1c')}")
    messagebox.showinfo('Test', 'Test okienek, nie przejmuj się tym :)')
    messagebox.showwarning('Test', 'Test okienek, nie przejmuj się tym :)')
    messagebox.showerror('Test', 'Test okienek, nie przejmuj się tym :)')
    result = messagebox.askquestion('Test', 'Test okienek, nie przejmuj się tym :)')


window = Tk()

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

chk_state = BooleanVar()

chk_state.set(True)

chk = Checkbutton(window, text='Choose', var=chk_state)

chk.grid(column=0, row=6)

selected = IntVar()

rad1 = Radiobutton(window, text='Pierwszy', value=1, variable=selected)

rad2 = Radiobutton(window, text='Drugi', value=2, variable=selected)

rad3 = Radiobutton(window, text='Trzeci', value=3, variable=selected)

rad1.grid(column=0, row=7)

rad2.grid(column=1, row=7)

rad3.grid(column=2, row=7)

btn = Button(window, text="Kliknij!", font=("Arial Bold", 30), bg="black", fg="white", command=klik)

btn.grid(column=2, row=2)

scrtxt = scrolledtext.ScrolledText(window, width=50, height=30)

scrtxt.grid(column=0, row=8)

window.mainloop()

# En este ejercicio tenéis que crear una lista de RadioButton
# que muestre la opción que se ha seleccionado y que contenga
# un botón de reinicio para que deje tal y como estaba al principio.
#
# Al principio no tiene que haber una opción seleccionada.

import tkinter
from tkinter import ttk

window = tkinter.Tk()

lista = ['Windows', 'MacOS', 'Linux', 'Unix', 'Solaris', 'FreeBSD']

selected = tkinter.IntVar()

label = ttk.Label(window)


def reset():
    global selected
    global label
    selected = tkinter.IntVar(value=0)
    label.config(text="")


def sel():
    global selected
    global label
    label.config(text=f'Has seleccionado {lista[(selected.get()-1)]}.')


r1 = ttk.Radiobutton(window, text=lista[0], value='1', variable=selected, command=sel)
r2 = ttk.Radiobutton(window, text=lista[1], value='2', variable=selected, command=sel)
r3 = ttk.Radiobutton(window, text=lista[2], value='3', variable=selected, command=sel)
r4 = ttk.Radiobutton(window, text=lista[3], value='4', variable=selected, command=sel)
r5 = ttk.Radiobutton(window, text=lista[4], value='5', variable=selected, command=sel)
r6 = ttk.Radiobutton(window, text=lista[5], value='6', variable=selected, command=sel)

button_reset = ttk.Button(window, text="Reinicio", command=reset)

r1.pack(ipadx=30, ipady=10, anchor=tkinter.W)
r2.pack(ipadx=30, ipady=10, anchor=tkinter.W)
r3.pack(ipadx=30, ipady=10, anchor=tkinter.W)
r4.pack(ipadx=30, ipady=10, anchor=tkinter.W)
r5.pack(ipadx=30, ipady=10, anchor=tkinter.W)
r6.pack(ipadx=30, ipady=10, anchor=tkinter.W)

label.pack(ipady=10, anchor=tkinter.W)

button_reset.pack(ipady=10, anchor=tkinter.S)

window.mainloop()

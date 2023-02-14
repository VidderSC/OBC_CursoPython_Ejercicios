# En este segundo ejercicio, tendréis que crear una interfaz sencilla
# la cual debe de contener una lista de elementos seleccionables,
# también debe de tener un label con el texto que queráis.

import tkinter as tk

ventana = tk.Tk()

lista = tk.Listbox(ventana)

tk.Label(text="Listado de Sistemas Operativos:").pack()

for sistemas in ['Windows', 'MacOS', 'Linux', 'Unix', 'Solaris', 'FreeBSD']:
    lista.insert(tk.END, sistemas)

lista.pack()

ventana.mainloop()

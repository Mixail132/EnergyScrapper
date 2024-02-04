# Here is a user input window code

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("EnergyControlCenter")
days_label = tk.Label(window, text="Введите количество дней для опроса данных ")
days_label.pack()
days_entry = tk.Entry(window)
days_entry.pack()
get_button = tk.Button(text="Опросить", command="")
get_button.pack()
window.mainloop()

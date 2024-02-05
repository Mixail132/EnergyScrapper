# Here is a user input window code

import tkinter as tk
from tkinter import messagebox


class UserInput:
    """ Handles the user's input """

    def get_days_from_user(self):        
        d =  self.days_entry.get()
        print(d , type(d))


    def make_user_input(self):
        """ 
        Creates a user input window and takes text from a user.
        The text 
        """
        window = tk.Tk()
        window.title("EnergyControlCenter")
        days_label = tk.Label(window, text="Введите количество дней для опроса данных ")
        days_label.pack()
        self.days_entry = tk.Entry(window)
        self.days_entry.pack()
        get_button = tk.Button(text="Опросить", command=self.get_days_from_user)
        get_button.pack()
        # window.after(5000, lambda: window.destroy())
        window.mainloop()


if __name__=="__main__":
    win=UserInput()
    win.make_user_input()

# Here is a user input window code

import tkinter as tk
from tkinter import messagebox


class UserInput:
    """ Handles the user's input """


    def get_days_from_user(self):
        """ 
        Gets the text from user input window
        and make it as an int.
        """        
        global days 
        days = self.days_entry.get()
        self.window.destroy()


    def make_user_input(self):
        """ 
        Creates a user input window and takes text from a user.
        The text is number of days for getting data from the DB.
        """
        self.window = tk.Tk()
        self.window.title("EnergyControlCenter")
        self.days_label = tk.Label(self.window, text="Введите количество дней для опроса данных ")
        self.days_label.pack()
        self.days_entry = tk.Entry(self.window)
        self.days_entry.pack()
        self.days_entry.insert(0, 3)
        self.get_button = tk.Button(text="Опросить", command=self.get_days_from_user)
        self.get_button.pack()
        self.window.mainloop()
        return int(days)
     


if __name__=="__main__":
    win = UserInput()
    print(win.make_user_input())
    # print(win.get_days_from_user())
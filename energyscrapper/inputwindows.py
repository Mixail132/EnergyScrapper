# Here is a user input window code

import tkinter as tk
from tkinter import messagebox


class UserInput:
    """ Handles the user's input """


    def get_days_from_user(self):
        """ 
        Gets the text from user input window
        checks it, closes the window after input.
        """        
        global days 
        days = self.days_entry.get()
        if not days.isdigit():
            messagebox.showerror("Error", "Введите число, а не текст")
        else:
            self.window.destroy()


    def make_user_input(self):
        """ 
        Creates a user input window and takes text from a user.
        The text is number of days for getting data from the DB.
        """
        self.window = tk.Tk()
        x = (self.window.winfo_screenwidth()-self.window.winfo_reqwidth()) / 2
        y = (self.window.winfo_screenheight()-self.window.winfo_reqheight()) / 2
        self.window.wm_geometry("+%d+%d" % (x,y))
        self.window.title("EnergyControlCenter")
        self.days_label = tk.Label(self.window, text="Введите количество дней для опроса данных ")
        self.days_label.pack()
        self.days_entry = tk.Entry(self.window)
        self.days_entry.pack()
        self.days_entry.insert(0, 1)
        self.get_button = tk.Button(text="Опросить", command=self.get_days_from_user)
        self.get_button.pack()
        self.window.mainloop()
        return int(days)
     


if __name__=="__main__":
    win = UserInput()
    win.make_user_input()

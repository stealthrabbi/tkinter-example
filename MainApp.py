from tkinter import Tk, Label, Button, Entry, ttk
from tkcalendar import Calendar, DateEntry

import tkinter as tk
from tkinter import ttk

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.someThing = "abbaa"

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.editText = Entry(master)
        self.editText.insert(0, 'default text')
        self.editText.pack()

        # state= readonly prevents typing in combo box.
        # https://stackoverflow.com/a/44959378/680268
        self.comboExample = ttk.Combobox(state="readonly",
                                    values=[
                                        "January",
                                        "February",
                                        "March",
                                        "April"])

        self.comboExample.pack()
        # default the selection
        self.comboExample.current(1)

        self.greet_button = Button(master, text="Set Date", command=self.show_calendar_selector)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Save", command=self.handle_save)
        self.greet_button.pack()

    def show_calendar_selector(self):
        win = tk.Toplevel()
        win.wm_title("Window")

        self.datePicker = Calendar(win, font="Arial 14", selectmode='day', locale='en_US',
                       cursor="hand1", year=2018, month=2, day=5)

        self.datePicker.pack(fill="both", expand=False)


        setDateButton = ttk.Button(win, text="Okay", command=win.destroy)
        setDateButton.pack()

    def handle_save(self):
        print("Greetings!")
        print(self.someThing)
        print("edit field contains: ", self.editText.get())
        print("combo box selected item: ", self.comboExample.get())
        print("combo box selected index: ", self.comboExample.current())

        if hasattr(self, 'datePicker'):
            print("selected date: ", self.datePicker.get_date())
        else:
            print("why you no set Date?!")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
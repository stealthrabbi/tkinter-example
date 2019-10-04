from tkinter import Tk, Label, Button, Entry, ttk
from tkcalendar import Calendar, DateEntry
from tkinterclock01 import Clock
# from tkcaln
# from TkinterClock01
# from TkinterClock01 import tkinterclock01

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

        self.datePicker = Calendar(font="Arial 14", selectmode='day', locale='en_US',
                       cursor="hand1", year=2018, month=2, day=5)

        self.datePicker.pack(fill="both", expand=False)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")
        print(self.someThing)
        print("edit field contains: ", self.editText.get())
        print("combo box selected item: ", self.comboExample.get())
        print("combo box selected index: ", self.comboExample.current())
        print("selected date: ", self.datePicker.get_date())

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
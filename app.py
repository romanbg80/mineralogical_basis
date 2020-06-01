import tkinter as tk
from tkinter import ttk  # set of widgets


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mineralogical basis")

        ttk.Label(text="Baza mineralogiczna projektu Opus", padding=(30,10)).pack()
        option_button = ttk.Button(text="Dostepne opcje", command=self.options)
        option_button.pack(side="left")

        quit_button = ttk.Button(text="Wyjdź z aplikacji", command=self.destroy)
        quit_button.pack(side="left")

        DatabaseContentFrame(self).pack()

    def options(self):
        print("przycisk podłączony do funkcji")


class DatabaseContentFrame(ttk.Frame):
    pass


root = MainWindow()
root.mainloop()

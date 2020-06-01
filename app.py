import tkinter as tk
from tkinter import ttk  # set of widgets


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mineralogical basis")

        ttk.Label(text="Baza mineralogiczna projektu Opus", padding=(30,10)).pack()

        DatabaseContentFrame(self).pack()


class DatabaseContentFrame(ttk.Frame):
    pass


root = MainWindow()
root.mainloop()

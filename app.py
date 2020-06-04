import tkinter as tk
from tkinter import ttk             # set of widgets
from PIL import Image, ImageTk      # inserting pictures


class MineralogicalBasis(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Mineralogical basis")

        frame = MainWindow(self, padding=(60, 30))
        frame.grid()


class MainWindow(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.username = tk.StringVar()
        self.userpassword = tk.StringVar()

        headline = ttk.Label(self, text="Baza mineralogiczna projektu Opus")
        username_label = ttk.Label(self, text="Username: ")
        username_entry = ttk.Entry(self, width=15, textvariable=self.username)
        userpassword_label = ttk.Label(self, text="User Password: ")
        userpassword_entry = ttk.Entry(self, width=15, textvariable=self.userpassword)
        login_button = ttk.Button(self, text="Login", command=self.login)
        option_button = ttk.Button(self, text="Dostepne opcje", command=self.options)
        quit_button = ttk.Button(self, text="Wyjdź z aplikacji", command=self.destroy)

        image = ttk.Label(self)

        headline.grid(column=0, row=0, )
        username_label.grid(column=0, row=1, sticky="W")
        username_entry.grid(column=1, row=1, sticky="EW")
        username_entry.focus()
        userpassword_label.grid(column=2, row=1, sticky="W")
        userpassword_entry.grid(column=3, row=1, sticky="EW")
        userpassword_entry.focus()
        login_button.grid(column=4, row=1)
        option_button.grid(column=0, row=2)
        quit_button.grid(column=1, row=2)

        # jeszcze nie działa jak powinno
        image.grid(row=3, column=5)
        image_1 = Image.open('znaczki.jpg')
        photo_1 = ImageTk.PhotoImage(image_1)
        label = ttk.Label(image, image=photo_1, padding=5)
        label.grid(row=3, column=5)

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def login(self, *args):
        try:
            print(f"Użytkownik, {self.username.get() or 'trzeba dodać'}")
        except ValueError:
            pass

    def options(self):
        print("przycisk podłączony do funkcji")


class DatabaseContentFrame(ttk.Frame):
    pass


root = MineralogicalBasis()
root.mainloop()

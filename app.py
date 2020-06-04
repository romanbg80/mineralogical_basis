import tkinter as tk
from tkinter import ttk             # set of widgets
from PIL import Image, ImageTk      # inserting pictures


class MineralogicalBasis(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Mineralogical basis")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        #main_frame = MainWindow(container, self)
        #main_frame.grid(row=0, column=0, sticky="NSEW")

        #options_to_main = Options(container, self)
        #options_to_main.grid(row=0, column=0, sticky="NSEW")

        #self.frames[MainWindow] = main_frame
        #self.frames[Options] = options_to_main

        for FrameClass in (MainWindow, Options):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(MainWindow)



    def show_frame(self, container):
        frame = self.frames[container]
        #self.bind("<Return>", frame.show_options)
        #self.bind("<KP_Enter>", frame.show_options)
        frame.tkraise()


class MainWindow(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.username = tk.StringVar()
        self.userpassword = tk.StringVar()

        headline = ttk.Label(self, text="Baza mineralogiczna projektu Opus")
        username_label = ttk.Label(self, text="Username: ")
        username_entry = ttk.Entry(self, width=15, textvariable=self.username)
        userpassword_label = ttk.Label(self, text="User Password: ")
        userpassword_entry = ttk.Entry(self, width=15, textvariable=self.userpassword)
        login_button = ttk.Button(self, text="Login", command=self.login)
        option_button = ttk.Button(self, text="Dostepne opcje", command=lambda: controller.show_frame(Options))
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

    def show_options(self):
        print("przycisk podłączony do funkcji")


class Options(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        option1_label = ttk.Label(self, text="Opcja numer 1")
        option1_button = ttk.Button(self, text="Wykonaj opcje 1")
        option1_label.grid(column=0, row=0, sticky="W")
        option1_button.grid(column=1, row=0, sticky="EW")

        to_main_label = ttk.Label(self, text="Powrót do strony głównej")
        to_main_button = ttk.Button(self, text="Powróć", command=lambda: controller.show_frame(MainWindow))
        to_main_label.grid(column=0, row=1, sticky="W")
        to_main_button.grid(column=0, row=1, sticky="EW")


root = MineralogicalBasis()
root.mainloop()

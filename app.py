import tkinter as tk
from tkinter import ttk  # set of widgets
from PIL import Image, ImageTk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mineralogical basis")
        ttk.Label(text="Baza mineralogiczna projektu Opus", padding=(30,10)).grid()
        DatabaseContentFrame(self).grid()

        input_frame = ttk.Frame(padding=(20, 10, 20, 0))
        input_frame.grid(row=0, column=0)

        login_button = ttk.Button(input_frame, text="Login", command=self.login)
        login_button.grid(row=0, column=4)

        username = tk.StringVar()
        userpassword = tk.StringVar()

        username_label = ttk.Label(input_frame, text="Username: ")
        username_label.grid(row=0, column=0, padx=(0, 10))
        username_entry = ttk.Entry(input_frame, width=15, textvariable=username)
        username_entry.grid(row=0, column=1)
        username_entry.focus()

        userpassword_label = ttk.Label(input_frame, text="User Password: ")
        userpassword_label.grid(row=0, column=2, padx=(0, 10))
        userpassword_entry = ttk.Entry(input_frame, width=15, textvariable=userpassword)
        userpassword_entry.grid(row=0, column=3)

        buttons_frame = ttk.Frame(padding=(20, 10))
        buttons_frame.grid(row=1, column=0)

        option_button = ttk.Button(buttons_frame, text="Dostepne opcje", command=self.options)
        option_button.grid(row=1, column=0)

        quit_button = ttk.Button(buttons_frame, text="Wyjdź z aplikacji", command=self.destroy)
        quit_button.grid(row=1, column=1)

        # jeszcze nie działa jak powinno
        image_frame = ttk.Frame(padding=(20, 10))
        image_frame.grid(row=2, column=0)
        image_1 = Image.open('znaczki.jpg')
        photo_1 = ImageTk.PhotoImage(image_1)
        label = ttk.Label(image_frame, image=photo_1, padding=5)
        label.grid(row=2, column=5)

    def login(self, username):

        print(f"Użytkownik, {username.get()  or 'trzeba dodać'}")





    def options(self):
        print("przycisk podłączony do funkcji")




class DatabaseContentFrame(ttk.Frame):
    pass


root = MainWindow()
root.mainloop()

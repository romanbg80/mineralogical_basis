import tkinter as tk
from tkinter import ttk  # set of widgets


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mineralogical basis")
        ttk.Label(text="Baza mineralogiczna projektu Opus", padding=(30,10)).pack()
        DatabaseContentFrame(self).pack()

        input_frame = ttk.Frame(padding=(20, 10, 20, 0))
        input_frame.pack(fill='both')

        login_button = ttk.Button(input_frame, text="Login", command=self.login)
        login_button.pack(side='right')

        username = tk.StringVar()
        userpassword = tk.StringVar()

        username_label = ttk.Label(input_frame, text="Username: ")
        username_label.pack(side="left", padx=(0, 10))
        username_entry = ttk.Entry(input_frame, width=15, textvariable=username)
        username_entry.pack(side="left")
        username_entry.focus()

        userpassword_label = ttk.Label(input_frame, text="User Password: ")
        userpassword_label.pack(side='left', padx=(0, 10))
        userpassword_entry = ttk.Entry(input_frame, width=15, textvariable=userpassword)
        userpassword_entry.pack(side='left')

        buttons_frame = ttk.Frame(padding=(20, 10))
        buttons_frame.pack(fill='both')

        option_button = ttk.Button(buttons_frame, text="Dostepne opcje", command=self.options)
        option_button.pack(side="left")

        quit_button = ttk.Button(buttons_frame, text="Wyjdź z aplikacji", command=self.destroy)
        quit_button.pack(side="left")


    def login(self, username):

        print(f"Użytkownik, {username.get()  or 'trzeba dodać'}")





    def options(self):
        print("przycisk podłączony do funkcji")




class DatabaseContentFrame(ttk.Frame):
    pass


root = MainWindow()
root.mainloop()

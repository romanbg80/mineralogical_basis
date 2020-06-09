import tkinter as tk
from tkinter import ttk                             # set of widgets
from PIL import Image, ImageTk                      # inserting pictures
from config.ConnectSQL import ConnectionConfig      # connect to database


class MineralogicalBasis(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Mineralogical basis")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        for FrameClass in (MainWindow, Options, ShowDatabase):
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
        option_button = ttk.Button(self, text="Dodaj nowy wpis", command=lambda: controller.show_frame(Options))
        database_button = ttk.Button(self, text="Lista minerałów", command=lambda: controller.show_frame(ShowDatabase))
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
        database_button.grid(column=1, row=2)
        quit_button.grid(column=2, row=2)

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
        self.conn = ConnectionConfig().connection()
        self.c = self.conn.cursor()
        self.conn.autocommit(True)

        self.nazwa_pol = tk.StringVar()
        self.nazwa_ang = tk.StringVar()
        self.formula = tk.StringVar()
        self.group = tk.StringVar()
        self.system = tk.StringVar()
        self.a_axis = tk.StringVar()
        self.b_axis = tk.StringVar()
        self.c_axis = tk.StringVar()
        self.alpha = tk.StringVar()
        self.beta = tk.StringVar()
        self.gamma = tk.StringVar()
        self.z_number = tk.StringVar()
        self.code = tk.StringVar()

        name_pol_label = ttk.Label(self, width=20, text="nazwa polska")
        name_ang_label = ttk.Label(self, width=20, text="nazwa angielska")
        formula_label = ttk.Label(self, width=20, text="formuła")
        group_label = ttk.Label(self, width=20, text='grupa przestrzenna')
        system_label = ttk.Label(self, width=20, text='układ krystalograficzny')
        a_label = ttk.Label(self, width=20, text="a")
        b_label = ttk.Label(self, width=20, text="b")
        c_label = ttk.Label(self, width=20, text="c")
        alpha_label = ttk.Label(self, width=20, text="alpha")
        beta_label = ttk.Label(self, width=20, text="beta")
        gamma_label = ttk.Label(self, width=20, text="gamma")
        z_number_label = ttk.Label(self, width=20, text="Z number")
        code_label = ttk.Label(self, width=20, text="code")

        name_pol_entry = ttk.Entry(self, width=15, textvariable=self.nazwa_pol)
        name_ang_entry = ttk.Entry(self, width=15, textvariable=self.nazwa_ang)
        formula_entry = ttk.Entry(self, width=15, textvariable=self.formula)
        group_entry = ttk.Entry(self, width=15, textvariable=self.group)
        system_entry = ttk.Entry(self, width=15, textvariable=self.system)
        a_entry = ttk.Entry(self, width=15, textvariable=self.a_axis)
        b_entry = ttk.Entry(self, width=15, textvariable=self.b_axis)
        c_entry = ttk.Entry(self, width=15, textvariable=self.c_axis)
        alpha_entry = ttk.Entry(self, width=15, textvariable=self.alpha)
        beta_entry = ttk.Entry(self, width=15, textvariable=self.beta)
        gamma_entry = ttk.Entry(self, width=15, textvariable=self.gamma)
        z_number_entry = ttk.Entry(self, width=15, textvariable=self.z_number)
        code_entry = ttk.Entry(self, width=15, textvariable=self.code)

        name_pol_label.grid(row=0, column=0)
        name_ang_label.grid(row=0, column=1)
        formula_label.grid(row=0, column=2)
        group_label.grid(row=0, column=3)
        system_label.grid(row=0, column=4)
        name_pol_entry.grid(row=1, column=0)
        name_ang_entry.grid(row=1, column=1)
        formula_entry.grid(row=1, column=2)
        group_entry.grid(row=1, column=3)
        system_entry.grid(row=1, column=4)
        a_label.grid(row=2, column=0)
        b_label.grid(row=2, column=1)
        c_label.grid(row=2, column=2)
        alpha_label.grid(row=2, column=3)
        beta_label.grid(row=2, column=4)
        gamma_label.grid(row=2, column=5)
        a_entry.grid(row=3, column=0)
        b_entry.grid(row=3, column=1)
        c_entry.grid(row=3, column=2)
        alpha_entry.grid(row=3, column=3)
        beta_entry.grid(row=3, column=4)
        gamma_entry.grid(row=3, column=5)
        z_number_label.grid(row=4, column=0)
        code_label.grid(row=4, column=1)
        z_number_entry.grid(row=5, column=0)
        code_entry.grid(row=5, column=1)

        option1_button = ttk.Button(self, text="Dodaj", command=self.addToDatabase)
        option1_button.grid(column=0, row=6, sticky="EW")

        to_main_button = ttk.Button(self, text="Powrót do strony głównej",
                                    command=lambda: controller.show_frame(MainWindow))
        to_main_button.grid(column=0, row=7, sticky="EW")

    def addToDatabase(self):
        print("Podłączony")
        self.c.execute("INSERT INTO minerals_list_vials VALUES (default, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (self.nazwa_pol.get(), self.nazwa_ang.get(), self.formula.get(), self.group.get(),
                        self.system.get(), self.a_axis.get(), self.b_axis.get(), self.c_axis.get(),
                        self.alpha.get(), self.beta.get(), self.gamma.get(), self.z_number.get(), self.code.get()))

        self.conn.close()


class ShowDatabase(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.conn = ConnectionConfig().connection()
        self.c = self.conn.cursor()
        self.conn.autocommit(True)

        self.records = tk.StringVar()

        self.print_records = ''

        to_main_button = ttk.Button(self, text="Powrót do strony głównej",
                                    command=lambda: controller.show_frame(MainWindow))
        to_main_button.grid(column=1, row=1, sticky="EW")
        records_button = ttk.Button(self, text="Wyswietl wpisy", command=self.showrecords)
        records_button.grid(column=0, row=1)
        records_display = ttk.Label(self, textvariable=self.records)
        records_display.grid(column=0, row=2)

    def showrecords(self):
        self.c.execute("SELECT id, name_pol, name_ang, formula, code FROM minerals_list_vials")
        self.records = self.c.fetchall()       #
        print(self.records)

        for record in self.records:
            self.print_records += str(record) + "\n"

        query_label = ttk.Label(self, text=self.print_records)
        query_label.grid(column=0, row=3)

        self.conn.close()


root = MineralogicalBasis()
root.mainloop()

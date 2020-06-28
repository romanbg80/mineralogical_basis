import tkinter as tk
from tkinter import ttk                             # set of widgets
from PIL import Image, ImageTk                      # inserting pictures
from config.ConnectSQL import ConnectionConfig      # connect to database
from tkinter import messagebox                      # wyskakujące okienko
from tkinter import filedialog as fd                # do otwierania plików
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class MineralogicalBasis(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Mineralogical basis")

        #self.conn = ConnectionConfig().connection()
        #self.c = self.conn.cursor()
        #self.conn.autocommit(True)

        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        for FrameClass in (MainWindow, Options, ShowDatabase, DeleteRecord, ImproveRecord, GraphWizzard):
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
        del_record_button = ttk.Button(self, text="Usuń wpis z bazy",
                                       command=lambda: controller.show_frame(DeleteRecord))
        improve_record_button = ttk.Button(self, text="Popraw wpis w bazie",
                                           command=lambda: controller.show_frame(ImproveRecord))
        quit_button = ttk.Button(self, text="Wyjdź z aplikacji", command=self.quit)         # quit "a nie" destroy
        graphs_button = ttk.Button(self, text="Rysowanie wykresów", command=lambda: controller.show_frame(GraphWizzard))

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
        improve_record_button.grid(column=2, row=2)
        del_record_button.grid(column=3, row=2)
        quit_button.grid(column=4, row=2)
        graphs_button.grid(column=0, row=3)

        # obrazki znaczków pocztowych
        self.my_img = ImageTk.PhotoImage(Image.open('znaczki.jpg'))
        img_label = ttk.Label(image=self.my_img)
        img_label.grid(row=0, column=5)

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

        name_pol_label = ttk.Label(self, width=20, text="nazwa polska *")
        name_ang_label = ttk.Label(self, width=20, text="nazwa angielska *")
        formula_label = ttk.Label(self, width=20, text="formuła *")
        group_label = ttk.Label(self, width=20, text='grupa przestrzenna')
        system_label = ttk.Label(self, width=20, text='układ krystalograficzny')
        a_label = ttk.Label(self, width=20, text="a")
        b_label = ttk.Label(self, width=20, text="b")
        c_label = ttk.Label(self, width=20, text="c")
        alpha_label = ttk.Label(self, width=20, text="alpha")
        beta_label = ttk.Label(self, width=20, text="beta")
        gamma_label = ttk.Label(self, width=20, text="gamma")
        z_number_label = ttk.Label(self, width=20, text="Z number")
        code_label = ttk.Label(self, width=20, text="code *")
        mandatory_label = ttk.Label(self, text="* pola obowiązkowe do wypełnienia")

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
        mandatory_label.grid(row=6, column=0)

        option1_button = ttk.Button(self, text="Dodaj", command=self.addToDatabase)
        option1_button.grid(column=0, row=7, sticky="EW")

        to_main_button = ttk.Button(self, text="Powrót do strony głównej",
                                    command=lambda: controller.show_frame(MainWindow))
        to_main_button.grid(column=0, row=8, sticky="EW")

    def addToDatabase(self):
        #print("Podłączony")
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


class DeleteRecord(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.conn = ConnectionConfig().connection()
        self.c = self.conn.cursor()
        self.conn.autocommit(True)

        self.id_to_delete = tk.StringVar()

        to_main_button = ttk.Button(self, text="Powrót do strony głównej",
                                    command=lambda: controller.show_frame(MainWindow))
        to_main_button.grid(column=4, row=1, sticky="EW")

        select_record_label = ttk.Label(self, text="Nr Id wpisu do usunięcia")
        select_record_enter = ttk.Entry(self, width=15, textvariable=self.id_to_delete)
        delete_button = ttk.Button(self, text="Usuń wpis", command=self.deleteRecord)
        select_record_label.grid(column=0, row=0)
        select_record_enter.grid(column=0, row=1)
        delete_button.grid(column=0, row=3)

    def deleteRecord(self):

        self.c.execute("DELETE from minerals_list_vials WHERE id= %s", (self.id_to_delete.get()))
        self.conn.close()
        # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

        messagebox.showwarning("Usunięcie wpisu z bazy danych", "Wpis o podanym Id został usuniety")


class ImproveRecord(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.conn = ConnectionConfig().connection()
        self.c = self.conn.cursor()
        self.conn.autocommit(True)

        self.id_to_improve = tk.StringVar()
        self.nazwa_pol_edit = tk.StringVar()
        self.nazwa_ang_edit = tk.StringVar()
        self.formula_edit = tk.StringVar()
        self.group_edit = tk.StringVar()
        self.system_edit = tk.StringVar()
        self.a_axis_edit = tk.StringVar()
        self.b_axis_edit = tk.StringVar()
        self.c_axis_edit = tk.StringVar()
        self.alpha_edit = tk.StringVar()
        self.beta_edit = tk.StringVar()
        self.gamma_edit = tk.StringVar()
        self.z_number_edit = tk.StringVar()
        self.code_edit = tk.StringVar()

        name_pol_label_edit = ttk.Label(self, width=20, text="nazwa polska *")
        name_ang_label_edit = ttk.Label(self, width=20, text="nazwa angielska *")
        formula_label_edit = ttk.Label(self, width=20, text="formuła *")
        group_label_edit = ttk.Label(self, width=20, text='grupa przestrzenna')
        system_label_edit = ttk.Label(self, width=20, text='układ krystalograficzny')
        a_label_edit = ttk.Label(self, width=20, text="a")
        b_label_edit = ttk.Label(self, width=20, text="b")
        c_label_edit = ttk.Label(self, width=20, text="c")
        alpha_label_edit = ttk.Label(self, width=20, text="alpha")
        beta_label_edit = ttk.Label(self, width=20, text="beta")
        gamma_label_edit = ttk.Label(self, width=20, text="gamma")
        z_number_label_edit = ttk.Label(self, width=20, text="Z number")
        code_label_edit = ttk.Label(self, width=20, text="code *")
        mandatory_label_edit = ttk.Label(self, text="* pola obowiązkowe do wypełnienia")

        self.name_pol_entry_edit = ttk.Entry(self, width=15, textvariable=self.nazwa_pol_edit)
        self.name_ang_entry_edit = ttk.Entry(self, width=15, textvariable=self.nazwa_ang_edit)
        self.formula_entry_edit = ttk.Entry(self, width=15, textvariable=self.formula_edit)
        self.group_entry_edit = ttk.Entry(self, width=15, textvariable=self.group_edit)
        self.system_entry_edit = ttk.Entry(self, width=15, textvariable=self.system_edit)
        self.a_entry_edit = ttk.Entry(self, width=15, textvariable=self.a_axis_edit)
        self.b_entry_edit = ttk.Entry(self, width=15, textvariable=self.b_axis_edit)
        self.c_entry_edit = ttk.Entry(self, width=15, textvariable=self.c_axis_edit)
        self.alpha_entry_edit = ttk.Entry(self, width=15, textvariable=self.alpha_edit)
        self.beta_entry_edit = ttk.Entry(self, width=15, textvariable=self.beta_edit)
        self.gamma_entry_edit = ttk.Entry(self, width=15, textvariable=self.gamma_edit)
        self.z_number_entry_edit = ttk.Entry(self, width=15, textvariable=self.z_number_edit)
        self.code_entry_edit = ttk.Entry(self, width=15, textvariable=self.code_edit)

        name_pol_label_edit.grid(row=1, column=0)
        name_ang_label_edit.grid(row=1, column=1)
        formula_label_edit.grid(row=1, column=2)
        group_label_edit.grid(row=1, column=3)
        system_label_edit.grid(row=1, column=4)
        self.name_pol_entry_edit.grid(row=2, column=0)
        self.name_ang_entry_edit.grid(row=2, column=1)
        self.formula_entry_edit.grid(row=2, column=2)
        self.group_entry_edit.grid(row=2, column=3)
        self.system_entry_edit.grid(row=2, column=4)
        a_label_edit.grid(row=3, column=0)
        b_label_edit.grid(row=3, column=1)
        c_label_edit.grid(row=3, column=2)
        alpha_label_edit.grid(row=3, column=3)
        beta_label_edit.grid(row=3, column=4)
        gamma_label_edit.grid(row=3, column=5)
        self.a_entry_edit.grid(row=4, column=0)
        self.b_entry_edit.grid(row=4, column=1)
        self.c_entry_edit.grid(row=4, column=2)
        self.alpha_entry_edit.grid(row=4, column=3)
        self.beta_entry_edit.grid(row=4, column=4)
        self.gamma_entry_edit.grid(row=4, column=5)
        z_number_label_edit.grid(row=5, column=0)
        code_label_edit.grid(row=5, column=1)
        self.z_number_entry_edit.grid(row=6, column=0)
        self.code_entry_edit.grid(row=6, column=1)
        mandatory_label_edit.grid(row=7, column=0)

        to_main_button = ttk.Button(self, text="Powrót do strony głównej",
                                    command=lambda: controller.show_frame(MainWindow))
        to_main_button.grid(column=4, row=8, sticky="EW")

        select_record_label = ttk.Label(self, text="Nr Id wpisu do poprawienia")
        select_record_enter = ttk.Entry(self, width=15, textvariable=self.id_to_improve)
        show_data_button = ttk.Button(self, text="Pokaż dane dla tego Id", command=self.showDataForId)
        show_data_button.grid(column=2, row=0)
        improve_button = ttk.Button(self, text="Popraw wpis", command=self.improveRecord)
        select_record_label.grid(column=0, row=0)
        select_record_enter.grid(column=1, row=0)
        improve_button.grid(column=0, row=8)
        quit_button = ttk.Button(self, text="Wyjdź z aplikacji", command=self.quit)
        quit_button.grid(column=4, row=9)

    def showDataForId(self):
        self.c.execute("SELECT * from minerals_list_vials WHERE id= %s", (self.id_to_improve.get()))
        records = self.c.fetchall()
        for record in records:
            self.name_pol_entry_edit.insert(0, record[1])
            self.name_ang_entry_edit.insert(0, record[2])
            self.formula_entry_edit.insert(0, record[3])
            self.group_entry_edit.insert(0, record[4])
            self.system_entry_edit.insert(0, record[5])
            self.a_entry_edit.insert(0, record[6])
            self.b_entry_edit.insert(0, record[7])
            self.c_entry_edit.insert(0, record[8])
            self.alpha_entry_edit.insert(0, record[9])
            self.beta_entry_edit.insert(0, record[10])
            self.gamma_entry_edit.insert(0, record[11])
            self.z_number_entry_edit.insert(0, record[12])
            self.code_entry_edit.insert(0, record[13])
        self.conn.close()

    def improveRecord(self):
        self.c.execute("""UPDATE minerals_list_vials SET (name_pol = %s, name_ang = %s, formula = %s,
                        crystal_system = %s, space_group = %s, a_axis = %s, b_axis = %s, c_axis = %s,
                        alpha = %s, beta = %s, gamma = %s, Z_number = %s, code = %s = ) WHERE id = %s""",
                       (self.nazwa_pol_edit.get(), self.nazwa_ang_edit.get(), self.formula_edit.get(),
                        self.group_edit.get(), self.system_edit.get(), self.a_axis_edit.get(), self.b_axis_edit.get(),
                        self.c_axis_edit.get(), self.alpha_edit.get(), self.beta_edit.get(), self.gamma_edit.get(),
                        self.z_number_edit.get(), self.code_edit.get(), self.id_to_improve.get()))
        self.conn.close()


class GraphWizzard(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.pressure_value = tk.StringVar()

        to_main_button = ttk.Button(self, text="Powrót do strony głównej",
                                    command=lambda: controller.show_frame(MainWindow))
        to_main_button.grid(column=0, row=8, sticky="EW")

        test_graph_button = ttk.Button(self, text='wykres testowy', command=self.testGraph)
        test_graph_button.grid(column=0, row=0)

        ruby_cheap_label = ttk.Label(self, text="wykres pomiaru cisnienia")
        ruby_cheap_button = ttk.Button(self, text='otwórz plik', command=self.open_file)
        ruby_cheap_label.grid(column=0, row=1)
        ruby_cheap_button.grid(column=1, row=1)

        calculate_pressure_button = ttk.Button(self, text="Calculate pressure",
                                               command=self.calibration_equation)
        calculate_pressure_button.grid(column=2, row=1)
        calculate_pressure_label = ttk.Label(self, text="Cisnienie [GPa]")
        calculate_pressure_label.grid(column=3, row=0)
        calculate_pressure_display = ttk.Label(self, text="Value shown here", textvariable=self.pressure_value)
        calculate_pressure_display.grid(column=3, row=1)




    def open_file(self):
        filename = fd.askopenfilename(initialdir="/home/Documents/mineralogical_basis/pressure_charts/",
                                           title="Select a file",
                                           filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        # nie otwiera sie właściwy podkatalog

        data = pd.read_csv(filename, sep="\t", header=None, skiprows=17, error_bad_lines=False,
                           names=["nanometers", "intensity"])
        print(data.head())
        data.plot(kind='scatter', x='nanometers', y='intensity', color='blue')
        #plt.xlim([680, 710])   #limit chyba nie działa
        #plt.show()
        # plt.savefig("pressure.png")

        er_one = data[data['intensity'] == data['intensity'].max()]
        print(er_one)

        self.er_two = data.loc[data['intensity'].idxmax()]
        print(self.er_two[0])
        self.data_source = float(self.er_two[0])
        #print(self.data_source.type())

        return self.data_source

    def calibration_equation(self):
        const_a = 1876.0
        const_b = 10.71
        lambda_zero = 694.24
        pressure = (const_a / const_b) * (((self.data_source/lambda_zero) ** const_b) - 1)
        self.pressure_value.set(f"{pressure:.3f}")
        print(round(pressure, 2))

    def testGraph(self):
        house_prices = np.random.normal(200000, 25000, 5000)
        plt.hist(house_prices, 50)
        plt.show()

# CRM - Customer Ralationship Management

root = MineralogicalBasis()
root.mainloop()

from config.ConnectSQL import ConnectionConfig


class BasisManager:
    def __init__(self):
        self.conn = ConnectionConfig().connection()
        self.c = self.conn.cursor()

    def tableCreator(self):
        # wykonanie zapytania
        self.c.execute("""CREATE TABLE minerals_list_vials (
            id smallint(6) NOT NULL,
            name_pol varchar(32) NOT NULL,
            name_ang varchar(32) NOT NULL,
            formula varchar(64) NOT NULL,
            crystal_system varchar(16) DEFAULT NULL,
            space_group varchar(16) DEFAULT NULL,
            a_axis decimal(8,4) DEFAULT NULL,
            b_axis decimal(8,4) DEFAULT NULL,
            c_axis decimal(8,4) DEFAULT NULL,
            alpha decimal(8,4) DEFAULT NULL,
            beta decimal(8,4) DEFAULT NULL,
            gamma decimal(8,4) DEFAULT NULL,
            Z_number smallint(6) DEFAULT NULL,
            code varchar(16) NOT NULL,
            PRIMARY KEY (id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
        # pobranie wyniku zwracanego przez zapytanie
        result = self.c.fetchone()

        if result:
            print("zalogowano: ")

        else:
            print("niezalogowano")


creator = BasisManager()
#creator.tableCreator()

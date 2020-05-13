import pymysql


class ConnectionConfig:
    def connection(self, user="sql7339614", password="TeduW3rEnM"):
        self.conn = pymysql.connect("sql7.freemysqlhosting.net", user, password, "sql7339614")
        if self.conn:
            print("...connected with database...")
        else:
            print("Attention. Connection failed.")
        return self.conn

    def closeConnection(self):
        self.conn.close()
        print("...connection closed...")


#ConnectionConfig().connection()


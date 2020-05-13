from config.ConnectSQL import ConnectionConfig


class BasisManager:
    def __init__(self):
        self.conn = ConnectionConfig().connection()
        self.c = self.conn.cursor()


import pymysql


def disconnection(user="sql7339614", password="TeduW3rEnM"):
    conn = pymysql.connect("sql7.freemysqlhosting.net", user, password, "sql7339614")
    conn.close()
    print("...connection closed...")


disconnection()

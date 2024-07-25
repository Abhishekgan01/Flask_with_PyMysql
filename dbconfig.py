import pymysql


class dbconfig:

    @staticmethod
    def open_connection():
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="Abhi@123",
            db='pymysql',
        )
        return conn

    @staticmethod
    def close_connection(conn):
        conn.close()
import pymysql

conn = pymysql.connect(host='localhost',
                       database='word',
                       user='root',
                       password='root1234')

class DataBase:
    def __init__(self):
        self.cur = conn.cursor()

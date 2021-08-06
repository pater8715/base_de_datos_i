import sqlite3
from tkinter import messagebox
class Connection():
    def __init__(self, name_db):
        self.__name_db = name_db
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = sqlite3.connect(self.__name_db)
            messagebox.showinfo("Inform", "Connection successfully")
        except:
            messagebox.showinfo("Alert!!","Connection Failed")

    def create_db(self):
        try:
            self.execute_sql("CREATE TABLE pruebas3 (id integer , name varchar(20)) ")
            messagebox.showinfo("Inform", "Database created successfully")
        except:
            messagebox.showinfo("Alert!!", "Database already exists")

    def insert_db(self, id, name ):
        try:
            self.execute_sql("CREATE TABLE   (id integer , name varchar(20)) ")
            messagebox.showinfo("Inform", "Database created successfully")
        except:
            messagebox.showinfo("Alert!!", "Database already exists")

    def execute_sql(self, SQL):
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute(SQL)
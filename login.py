import os
import sys
import platform
import mysql.connector

def clear_everything():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        print("Sorry we do not now this system")

def error():
    clear_everything()
    print("Error please try again\n")


my_db = mysql.connector.connect(
    host="localhost",
    user="abbos",
    password="12345678",
    database="dang"
)
my_cursor = my_db.cursor()

class Register:
    def __init__(self):
        pass


    def manu(self):
        pass
    def choosed(self):
        pass

    def sig_in(self):
        pass
    def log_ing(self):
        pass
    def exit(self):
        pass
    def update_login(self):
        pass
    def update_password(self):
        pass
    def log_out(self):
        pass
    def delete_account(self):
        pass


    def manu_in(self):
        pass
    def choosed_in(self):
        pass


register = Register()



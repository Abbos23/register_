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
my_cursor.execute("create table if not exists register(id int(6) unsigned auto_increment primary key, name varchar(20), surname varchar(20), age int(3), login varchar(20), pasasword varchar (20))")
my_db.commit()

class Register:
    def __init__(self):
        self.manu()


    def manu(self):
        answer = input("""
What do you want?
Please choose one of them

    Sig in [1]
    Log in [2]
    Exit   [3]

 
""")
        self.choosed(answer)




    def choosed(self, chose):
        if chose == '1':
            clear_everything()
            self.sig_in()
        elif chose == '2':
            clear_everything()
            self.log_in()
        elif chose == '3':
            clear_everything()
            print("Bye ;)")
            exit()
        else:
            clear_everything()
            self.manu()





    def sig_in(self):
        name = self.name_surname("name")
        surname = self.name_surname("surname")
        age = self.age()


    def log_in(self):
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


    def name_surname(self, name_surname):
        name = input(f"Please enter your {name_surname}:\n:").strip().capitalize()
        if name:
            return name
        else:
            error()
            self.name_surname(name_surname)

    def age(self):
        age = input("Please enter your age:\n").strip()
        if age:
            if age.isdigit():
                return age
            else:
                error()
                self.age()
        else:
            error()
            self.age()

    # def login(self):
    #     login = loggin




register = Register()



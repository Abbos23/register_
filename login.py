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
my_cursor.execute("create table if not exists register(id int(6) unsigned auto_increment primary key, name varchar(20), surname varchar(20), age int(3), login varchar(20), password varchar (20))")
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
        login = self.login()
        password = self.password()
        self.write_to_database(name, surname, age, login, password)




    def log_in(self):
        login = input("Please enter your login:\n").strip().lower()
        if login:
            my_cursor.execute(f"select * from register where login='{login}'")
            result = my_cursor.fetchall()
            if result:
                current_password = result[0][5]
                print(current_password)
            else:
                error()
                self.login()

        else:
            error()
            self.login()

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
        answer = input("""
        What do you want?
        Please choose one of them

            Update login     [1]
            Update paassword [2]
            Log out          [3]
            Delete account   [4]

        """)
        self.choosed_in(answer)

    def choosed_in(self, chose):
        if chose == '1':
            clear_everything()
            self.update_login()
        elif chose == '2':
            clear_everything()
            self.update_password()
        elif chose == '3':
            clear_everything()
            self.manu()
        elif chose == '4':
            clear_everything()
            self.delete_account()
        else:
            clear_everything()
            self.manu_in()

    # ___________________________________For REGISTER_______________________________________________________
    def name_surname(self, name_surname):
        name = input(f"Please enter your {name_surname}:\n:").strip().capitalize()
        if name:
            clear_everything()
            return name
        else:
            error()
            self.name_surname(name_surname)

    def age(self):
        age = input("Please enter your age:\n").strip()
        if age:
            if age.isdigit():
                clear_everything()
                return age
            else:
                error()
                self.age()
        else:
            error()
            self.age()

    def login(self):
        login = input("Please enter login:\n").strip().lower()
        if login:
            my_cursor.execute(f"select * from register where login='{login}'")
            result = my_cursor.fetchall()
            if not result:
                clear_everything()
                return login
            else:
                clear_everything()
                print("Sorry this login teken")
                self.login()
        else:
            error()
            self.login()

    def password(self):
        passoword = input("PLease enter password:\n").strip()
        if passoword:
            passoword1 = input("Confirm password:\n")
            if passoword1 == passoword:
                clear_everything()
                return passoword
            else:
                error()
                self.password()

        else:
            error()
            self.password()

    def write_to_database(self,name,surname,age,login,password):
        clear_everything()
        my_cursor.execute(f"insert into register(name,surname,age,login,password) values ('{name}','{surname}','{age}','{login}','{password}')")
        my_db.commit()
# _____________________________________________________________________________________________________

# __________________________________OTHERS____________________________________________________________


register = Register()



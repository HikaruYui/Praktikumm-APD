import inquirer
from auth import login_menu, register_menu, keluar_sistem
from menuAdmin import menu_admin
from menuUser import menu_user
import os

def main():
    os.system('cls')
    while True:
        tampil_menu_awal = [
            inquirer.List(
                "menu_awal",
                message="Incident Respond Management System Program",
                choices=[
                    "1. Login",
                    "2. Register",
                    "3. Keluar"
                ]
            )
        ]
        jawaban = inquirer.prompt(tampil_menu_awal)
        menu_awal = int(jawaban["menu_awal"].split(".")[0])

        if menu_awal == 1:
            os.system('cls')
            login, username_login, role = login_menu()
            if login:
                if role == "admin":
                    menu_admin(username_login, role)
                else:
                    menu_user(username_login, role)
        elif menu_awal == 2:
            os.system('cls')
            register_menu()
        elif menu_awal == 3:
            os.system('cls')
            keluar_sistem()
            break

if __name__ == "__main__":
    main()

import inquirer
from fiturUtama import pengguna, keluar_program, clear

admin = ("diftya", "042")

def login_menu():
    clear()
    print("======== LOGIN ========")
    username = input("Username: ")
    password = input("Password: ")

    if username == admin[0] and password == admin[1]:
        print("Login Berhasil (Admin)")
        input("Tekan Enter untuk melanjutkan")
        clear()
        return True, username, "admin"

    for user, data in pengguna.items():
        if user == username and data.get("password") == password:
            print("Login Berhasil (User)")
            input("Tekan Enter untuk melanjutkan")
            clear()
            return True, username, "user"

    print("Username atau password salah.")
    input("Tekan Enter untuk melanjutkan")
    clear()
    return False, "", ""

def register_menu():
    clear()
    print("======= REGISTER ========")
    username = input("Masukkan username anda: ")
    password = input("Masukkan password: ")

    if username == admin[0]:
        print("Username ini tidak bisa dipakai.")
    elif username in pengguna:
        print("Username telah terdaftar.")
    else:
        pengguna[username] = {"password": password, "role": "user"}
        print("Registrasi berhasil.")
    input("Tekan Enter untuk melanjutkan")
    clear()

def keluar_sistem():
    keluar_program("SISTEM MANAJEMEN INSIDEN (SIEM)")
    input("Tekan Enter untuk keluar...")
    clear()

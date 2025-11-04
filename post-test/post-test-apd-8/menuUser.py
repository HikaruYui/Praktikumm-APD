import inquirer
from fiturUtama import tambah_insiden, lihat_insiden, ubah_status_insiden, filter_insiden, clear

def menu_user(username_login, role):
    while True:
        clear()
        pertanyaan = [
            inquirer.List(
                'menu',
                message=f"Menu User ({username_login})",
                choices=[
                    "1. Tambah Insiden",
                    "2. Lihat Insiden",
                    "3. Ubah Status Insiden",
                    "4. Filter Insiden",
                    "5. Logout"
                ]
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)
        pilih = int(jawaban['menu'].split('.')[0])
        clear()

        if pilih == 1:
            tambah_insiden(username_login)
        elif pilih == 2:
            lihat_insiden(username_login, role)
        elif pilih == 3:
            ubah_status_insiden(username_login, role)
        elif pilih == 4:
            filter_insiden(username_login, role)
        elif pilih == 5:
            print("Logout berhasil.")
            input("Tekan Enter untuk melanjutkan")
            clear()
            break

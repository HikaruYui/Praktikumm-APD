import inquirer
import os
from NIM_2509106042_DiftyaAzzahra_PT_8 import tambah_insiden, lihat_insiden, ubah_status_insiden, filter_insiden

def menu_user(username_login, role):
    while True:
        os.system('cls')
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
            input("Tekan Enter untuk lanjut")
            break

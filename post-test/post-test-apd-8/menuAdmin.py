import inquirer
import os
from NIM_2509106042_DiftyaAzzahra_PT_8 import tambah_insiden, lihat_insiden, ubah_status_insiden, statistik_insiden, filter_insiden, hapus_insiden, lihat_pengguna

def menu_admin(username_login, role):
    while True:
        os.system('cls')
        pertanyaan = [
            inquirer.List(
                'menu',
                message=f"Menu Admin ({username_login})",
                choices=[
                    "1. Tambah Insiden",
                    "2. Lihat Insiden",
                    "3. Ubah Status Insiden",
                    "4. Statistik Insiden",
                    "5. Filter Insiden",
                    "6. Hapus Insiden",
                    "7. Lihat Semua Pengguna",
                    "8. Logout"
                ]
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)
        pilih = int(jawaban['menu'].split('.')[0])
        os.system('cls')

        if pilih == 1:
            os.system('cls')
            tambah_insiden(username_login)
        elif pilih == 2:
            os.system('cls')
            lihat_insiden(username_login, role)
        elif pilih == 3:
            os.system('cls')
            ubah_status_insiden(username_login, role)
        elif pilih == 4:
            os.system('cls')
            statistik_insiden()
        elif pilih == 5:
            os.system('cls')
            filter_insiden(username_login, role)
        elif pilih == 6:
            os.system('cls')
            hapus_insiden()
        elif pilih == 7:
            os.system('cls')
            lihat_pengguna()
        elif pilih == 8:
            os.system('cls')
            print("Logout berhasil.")
            input("Tekan Enter untuk lanjut...")
            break

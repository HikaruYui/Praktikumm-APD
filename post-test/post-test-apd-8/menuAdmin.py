import inquirer
from fiturUtama import tambah_insiden, lihat_insiden, ubah_status_insiden, statistik_insiden, filter_insiden, hapus_insiden, lihat_pengguna, clear

def menu_admin(username_login, role):
    while True:
        clear()
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
        clear()

        if pilih == 1:
            tambah_insiden(username_login)
        elif pilih == 2:
            lihat_insiden(username_login, role)
        elif pilih == 3:
            ubah_status_insiden(username_login, role)
        elif pilih == 4:
            statistik_insiden()
        elif pilih == 5:
            filter_insiden(username_login, role)
        elif pilih == 6:
            hapus_insiden()
        elif pilih == 7:
            lihat_pengguna()
        elif pilih == 8:
            print("Logout berhasil.")
            input("Tekan Enter untuk melanjutkan")
            clear()
            break

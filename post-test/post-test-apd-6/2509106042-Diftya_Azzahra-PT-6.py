import os

print("=== Incident Respond Management System Program ===")

# Data insiden
insiden = {}

# Data admin dan pengguna
admin = ("diftya", "042")
pengguna = {}

id_counter = 0
login = False
username_login = ""
role = ""

# Daftar status 
daftar_status = {
"open" : "Insiden baru dilaporkan",
"in progress" : "Insiden sedang ditangani",
"resolved" : "Insiden berhasil diselesaikan",
"closed" : "Kasus telah ditutup",
}

while True:
    print("=== SISTEM MANAJEMEN INSIDEN (SIEM) ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu: ")

    if menu_awal == "1":
        os.system('cls')
        print("======== LOGIN ========")
        username = input("Username: ")
        password = input("Password: ")

        if username == admin[0] and password == admin[1]:
            login = True
            username_login = username
            role = "admin"
            print("Login Berhasil")
        else:
            ketemu = False
            for user, data in pengguna.items():
                if user == username and data["password"] == password:
                    login = True
                    username_login = username
                    role = data["role"]
                    ketemu = True
                    break
            if not ketemu:
                print("Username atau passwordmu salah")
            input("Tekan Enter untuk melanjutkan program")
        os.system('cls')

    # Fitur Register
    elif menu_awal == "2":
        os.system('cls')
        print("======= REGISTER ========")
        username = input("Masukkan username anda: ")
        password = input("Masukkan password: ")
        username_sama = False
        if username == admin[0]:
            print("Username ini tidak bisa dipakai.")
        else:
            for user, data in pengguna.items():
                if user == username:
                    username_sama = True
                    break
            if username_sama:
                print("Username telah terdaftar.")
            else:
                pengguna.update({
                    username: {
                        "password": password,
                        "role": "user"
                        }
                    })

                print("Selamat registrasi berhasil")
        input("Tekan Enter untuk lanjut ke menu")
        os.system('cls')

    # Fitur Keluar Program
    elif menu_awal == "3":
        print("Anda telah keluar dari program")
        break

    else:
        print("Menu tidak valid")
        input("Tekan Enter untuk lanjut")
        os.system('cls')
    # Setelah login
    while login:
        os.system('cls')
        if role == "user":
            print("=========== MENU UTAMA ===============")
            print(f"Login sebagai: {username_login} ({role})")
            print("1. Tambah Insiden")
            print("2. Lihat Insiden")
            print("3. Ubah Status Insiden")
            print("4. Logout")
            print("5. Filter Insiden berdasarkan Status")

        elif role == "admin":
            print("======== MENU UTAMA (ADMIN) =========")
            print(f"Login sebagai: {username_login} ({role})")
            print("1. Tambah Insiden")
            print("2. Lihat Insiden")
            print("3. Ubah Status Insiden")
            print("4. Logout")
            print("5. Filter Insiden berdasarkan Status")
            print("6. Hapus Insiden")
            print("7. Lihat Semua Pengguna")
            print("8. Statistik Insiden")

        pilih_menu = input("Pilih menu: ")

        # Tambah Insiden
        if pilih_menu == "1":
            os.system('cls')
            print("======================== Tambah Insiden ========================")
            judul = input("Judul insiden: ")
            tingkat = input("Tingkat keparahan: ")
            status = "open"
            tanggal = input("Tanggal (DD/MM/YYYY): ")

            id_counter += 1
            insiden.update({
                id_counter: {
                    "id_counter" : id_counter,
                    "judul" : judul,
                    "tingkat" : tingkat,
                    "status" : "open",
                    "tanggal" : tanggal,
                    "pemilik": username_login,
                }
            })
            print("Insiden berhasil ditambahkan!")
            input("Tekan Enter untuk melanjutkan")

        # Lihat Insiden
        elif pilih_menu == "2":
            os.system('cls')
            print("======================== Lihat Daftar Insiden ========================")
            if len(insiden) == 0:
                print("Belum ada insiden tercatat.")
            else:
                for id_insiden, data in insiden.items():
                    if role == "admin" or data["pemilik"] == username_login:
                        print(f"ID: {data['id_counter']}, Judul: {data['judul']},"
                              f" Tingkat: {data['tingkat']}, "
                              f"Status: {data['status']}, Tanggal: {data['tanggal']}, Pemilik: {data['pemilik']}")
            input("Tekan Enter untuk melanjutkan program")

        # Ubah Status Insiden
        elif pilih_menu == "3":
            os.system('cls')
            print("========= Mengubah Status Insiden =========")
            ubah_id = input("Masukkan ID insiden: ")
            ketemu = False

            for id_insiden, data in insiden.items():
                if str(data["id_counter"]) == ubah_id and data["pemilik"] == username_login:
                    print(f"Status sekarang: {data['status']}")
                    print("Pilihan status:", daftar_status)
                    status_baru = input("Masukkan status baru: ")
                    while status_baru not in daftar_status:
                        print("Status tidak valid! Pilihan:", daftar_status)
                        status_baru = input("Masukkan status lagi: ")

                    if status_baru in daftar_status:
                        data["status"] = status_baru
                        print("Status berhasil diubah!")
                    else:
                        print("Status tidak valid!")
                    ketemu = True
                    break
            if not ketemu:
                print("ID tidak ketemu atau bukan milik Anda.")
            input("Tekan Enter untuk melanjutkan")

        # Logout
        elif pilih_menu == "4":
            login = False
            username_login = ""
            role = ""
            print("Logout berhasil.")
            input("Tekan Enter untuk kembali ke menu awal")

        # Filter Insiden
        elif pilih_menu == "5":
            os.system('cls')
            print("======================== Filter Status Insiden ========================")
            status_filter = input("Masukkan status untuk filter: ")
            while status_filter not in daftar_status:
                print("Status tidak valid! Pilihan:", daftar_status)
                status_filter = input("Masukkan status lagi: ")
            ditemukan = False
            for id_insiden, data in insiden.items():
                if data["status"] == status_filter and (role == "admin" or data["pemilik"] == username_login):
                    print(f"ID: {data['id_counter']}, Judul: {data['judul']}, Status: {data['status']}, Pemilik: {data['pemilik']}")
                    ditemukan = True
            if not ditemukan:
                print("Tidak ada insiden dengan status tersebut.")
            input("Tekan Enter untuk lanjut")

        # Hapus Insiden (Admin)
        elif role == "admin" and pilih_menu == "6":
            os.system('cls')
            print("======================== Hapus Insiden ========================")
            if len(insiden) == 0:
                print("Tidak ada insiden untuk dihapus.")
            else:
                hapus_id = input("Masukkan ID insiden yang ingin dihapus: ")
                ketemu = False
                for id_insiden, data in insiden.items():
                    if str(insiden[id_insiden]["id_counter"]) == hapus_id:
                        del insiden[id_insiden]
                        print("Insiden berhasil dihapus.")
                        ketemu = True
                        break
                if not ketemu:
                    print("ID tidak ketemu.")
            input("Tekan Enter untuk melanjutkan program")

        # Lihat Semua Pengguna (Admin)
        elif role == "admin" and pilih_menu == "7":
            os.system('cls')
            print("========= Lihat Semua Pengguna =========")
            if len(pengguna) == 0:
                print("Belum ada pengguna terdaftar.")
            else:
                for username, data in pengguna.items():
                    print(f"Username: {username}, Role: {data['role']}")

            input("Tekan Enter untuk melanjutkan program")

        # Statistik Insiden (Admin)
        elif role == "admin" and pilih_menu == "8":
            os.system('cls')
            print("========= Statistik Insiden =========")
            if len(insiden) == 0:
                print("Belum ada insiden tercatat.")
            else:
                jumlah_status = {}
                for id_insiden, data in insiden.items():
                    status = data["status"]
                    if status in jumlah_status:
                        jumlah_status[status] += 1
                    else:
                        jumlah_status[status] = 1
                for status, jumlah in jumlah_status.items():
                        print(f"{status}: {jumlah} insiden")

            input("Tekan Enter untuk lanjut")

        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan")


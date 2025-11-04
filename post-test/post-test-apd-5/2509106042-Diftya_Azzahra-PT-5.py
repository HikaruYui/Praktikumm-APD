import os

print("=== Incident Respond Management System Program ===")

# Data insiden
insiden = []
logs = []

# Data admin dan pengguna
pengguna = []
admin = ("diftya", "042")

id_counter = 1
login = False
username_login = ""
role = ""

while True:
    print("=== SISTEM MANAJEMEN INSIDEN (SIEM) ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu: ")

    if menu_awal == "1":
        os.system('cls')
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")

        if username == admin[0] and password == admin[1]:
            login = True
            username_login = username
            role = "admin"
            print("Login Berhasil")
        else:
            ketemu = False
            for user in pengguna:
                if user[0] == username and user[1] == password:
                    login = True
                    username_login = username
                    role = "user"
                    ketemu = True
                    break
            if not ketemu:
                print("Username atau passwordmu salah")
            input("Tekan Enter untuk melanjutkan program")

    # Fitur Register
    elif menu_awal == "2":
        print("=== REGISTER ===")
        username = input("Masukkan username anda: ")
        password = input("Masukkan password: ")
        username_sama = False
        if username == admin[0]:
            print("Username ini tidak bisa dipakai.")
        else:
            for user in pengguna:
                if user[0] == username:
                    username_sama = True
                    break
            if username_sama:
                print("Username telah terdaftar.")
            else:
                pengguna.append([username, password, "user"])
                print("Selamat registrasi berhasil")
        input("Tekan Enter untuk lanjut ke menu")

    # Fitur Keluar Program
    elif menu_awal == "3":
        print("Anda telah keluar dari program")
        break

    else:
        print("Menu tidak valid")
        input("Tekan Enter untuk lanjut")

    # Setelah login
    while login:
        os.system('cls')
        if role == "user":
            print("=== MENU UTAMA ===")
            print(f"Login sebagai: {username_login} ({role})")
            print("1. Tambah Insiden")
            print("2. Lihat Insiden")
            print("3. Ubah Status Insiden")
            print("4. Logout")
            print("5. Filter Insiden berdasarkan Status")

        elif role == "admin":
            print("=== MENU UTAMA (ADMIN) ===")
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
            print("=== Tambah Insiden ===")
            judul = input("Judul insiden: ")
            tingkat = input("Tingkat keparahan: ")
            status = "open"
            tanggal = input("Tanggal (DD/MM/YYYY): ")
            insiden.append([id_counter, judul, tingkat, status, tanggal, username_login])
            id_counter += 1
            print("Insiden berhasil ditambahkan!")
            input("Tekan Enter untuk melanjutkan")

        # Lihat Insiden
        elif pilih_menu == "2":
            os.system('cls')
            print("=== List Daftar Insiden ===")
            if len(insiden) == 0:
                print("Belum ada insiden tercatat.")
            else:
                for i in range(len(insiden)):
                    if role == "admin" or insiden[i][5] == username_login:
                        print(f"ID: {insiden[i][0]}, Judul: {insiden[i][1]}, Tingkat: {insiden[i][2]}, "
                              f"Status: {insiden[i][3]}, Tanggal: {insiden[i][4]}, Pemilik: {insiden[i][5]}")
            input("Tekan Enter untuk melanjutkan program")

        # Ubah Status Insiden
        elif pilih_menu == "3":
            os.system('cls')
            print("=== Mengubah Status Insiden ===")
            ubah_id = input("Masukkan ID insiden: ")
            ketemu = False

            for i in range(len(insiden)):
                if str(insiden[i][0]) == ubah_id and insiden[i][5] == username_login:
                    print(f"Status sekarang: {insiden[i][3]}")
                    daftar_status = ["open", "in progress", "resolved", "closed"]
                    print("Pilihan status:", daftar_status)
                    status_baru = input("Masukkan status baru: ").strip().lower()

                    if status_baru in daftar_status:
                        insiden[i][3] = status_baru
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
            status_filter = input("Masukkan status untuk filter: ").strip().lower()
            ditemukan = False
            for i in insiden:
                if i[3] == status_filter and (role == "admin" or i[5] == username_login):
                    print(f"ID: {i[0]}, Judul: {i[1]}, Status: {i[3]}, Pemilik: {i[5]}")
                    ditemukan = True
            if not ditemukan:
                print("Tidak ada insiden dengan status tersebut.")
            input("Tekan Enter untuk lanjut")

        # Hapus Insiden (Admin)
        elif role == "admin" and pilih_menu == "6":
            os.system('cls')
            print("=== Hapus Insiden ===")
            if len(insiden) == 0:
                print("Tidak ada insiden untuk dihapus.")
            else:
                hapus_id = input("Masukkan ID insiden yang ingin dihapus: ")
                ketemu = False
                for i in range(len(insiden)):
                    if str(insiden[i][0]) == hapus_id:
                        del insiden[i]
                        print("Insiden berhasil dihapus.")
                        ketemu = True
                        break
                if not ketemu:
                    print("ID tidak ketemu.")
            input("Tekan Enter untuk melanjutkan program")

        # Lihat Semua Pengguna (Admin)
        elif role == "admin" and pilih_menu == "7":
            os.system('cls')
            print("=== DAFTAR PENGGUNA ===")
            if len(pengguna) == 0:
                print("Belum ada pengguna terdaftar.")
            else:
                for user in pengguna:
                    print(f"Username: {user[0]}, Role: {user[2]}")
            input("Tekan Enter untuk melanjutkan program")

        # Statistik Insiden (Admin)
        elif role == "admin" and pilih_menu == "8":
            os.system('cls')
            print("=== Statistik Insiden ===")
            if len(insiden) == 0:
                print("Belum ada insiden tercatat.")
            else:
                jumlah_status = {}
                for i in insiden:
                    if i[3] in jumlah_status:
                        jumlah_status[i[3]] += 1
                    else:
                        jumlah_status[i[3]] = 1
                for status, jumlah in jumlah_status.items():
                    print(f"{status}: {jumlah} insiden")
            input("Tekan Enter untuk lanjut")

        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan")
import os

print("=== Incident Respond Management System Program ===")

# Variabel Global (3 buah)
insiden = {}
pengguna = {}
daftar_status = {
    "open": "Insiden baru dilaporkan",
    "in progress": "Insiden sedang ditangani",
    "resolved": "Insiden berhasil diselesaikan",
    "closed": "Kasus telah ditutup",
}


# Prosedur 
def clear():
    os.system('cls')

# Fungsi tanpa parameter
def tampil_menu_awal():
    print("=== SISTEM MANAJEMEN INSIDEN (SIEM) ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

# Fungsi tanpa parameter
def tampil_daftar_status():
    print("Pilihan status yang tersedia:")
    for k, v in daftar_status.items():
        print(f"- {k} : {v}")

# Prosedur 
def keluar_program(nama_program):
    print("Anda telah keluar dari program")

# Tambah insiden 
def tambah_insiden(username_login):
    global insiden

    # 5 variabel lokal
    judul = input("Judul insiden: ")            
    tingkat = input("Tingkat keparahan: ")      
    status = "open"                             
    tanggal = input("Tanggal (DD/MM/YYYY): ")   
    id_counter = len(insiden) + 1               

    insiden.update({
        id_counter: {
            "id_counter": id_counter,
            "judul": judul,
            "tingkat": tingkat,
            "status": status,
            "tanggal": tanggal,
            "pemilik": username_login,
        }
    })
    print("Insiden berhasil ditambahkan!")
    input("Tekan Enter untuk melanjutkan")

# Lihat insiden
def lihat_insiden(username_login, role):
    if len(insiden) == 0:
        print("Belum ada insiden tercatat.")
    else:
        ditemukan = False
        for id_insiden, data in insiden.items():
            if role == "admin" or data.get("pemilik") == username_login:
                print(f"ID: {data['id_counter']}, Judul: {data['judul']}, "
                      f"Tingkat: {data['tingkat']}, Status: {data['status']}, "
                      f"Tanggal: {data['tanggal']}, Pemilik: {data['pemilik']}")
                ditemukan = True
        if not ditemukan:
            print("Tidak ada insiden yang dapat Anda lihat.")
    input("Tekan Enter untuk melanjutkan program")

# Ubah status insiden 
def ubah_status_insiden(username_login, role):
    global insiden

    while True:
        try:
            ubah_id = int(input("Masukkan ID insiden: "))
            break
        except ValueError:
            print("ValueError: input harus berupa angka!")
            input("Tekan Enter untuk lanjut")

    if ubah_id not in insiden:
        print("ID tidak ditemukan.")
        input("Tekan Enter untuk melanjutkan")
        return

    data = insiden[ubah_id]
    if data.get("pemilik") != username_login and role != "admin":
        print("Anda tidak memiliki izin untuk mengubah insiden ini.")
        input("Tekan Enter untuk melanjutkan")
        return

    print(f"Status sekarang: {data['status']}")
    tampil_daftar_status()

    while True:
        try:
            status_baru = input("Masukkan status baru: ")
            if status_baru not in daftar_status:
                
                raise ValueError
            break
        except ValueError:
            print("ValueError: Status tidak valid!")
            print("Pilihan status yang tersedia:")
            for k, v in daftar_status.items():
                print(f"- {k} : {v}")
            input("Tekan Enter untuk lanjut")

    data["status"] = status_baru
    print("Status berhasil diubah!")
    input("Tekan Enter untuk melanjutkan")

# Filter insiden berdasarkan status 
def filter_insiden(username_login, role):
    tampil_daftar_status()

    while True:
        try:
            status_filter = input("Masukkan status untuk filter: ")
            if status_filter not in daftar_status:
                raise ValueError
            break
        except ValueError:
            print("ValueError: Status tidak valid! Pilihan:", list(daftar_status.keys()))
            input("Tekan Enter untuk lanjut")

    ditemukan = False
    for id_insiden, data in insiden.items():
        if data.get("status") == status_filter and (role == "admin" or data.get("pemilik") == username_login):
            print(f"ID: {data['id_counter']}, Judul: {data['judul']}, Status: {data['status']}, Pemilik: {data['pemilik']}")
            ditemukan = True
    if not ditemukan:
        print("Tidak ada insiden dengan status tersebut.")
    input("Tekan Enter untuk lanjut")

# Hapus insiden (Admin) 
def hapus_insiden():
    global insiden
    clear()
    if len(insiden) == 0:
        print("Tidak ada insiden untuk dihapus.")
        input("Tekan Enter untuk melanjutkan program")
        return

    while True:
        try:
            hapus_id = int(input("Masukkan ID insiden yang ingin dihapus: "))
            break
        except ValueError:
            print("ValueError: input harus berupa angka!")
            input("Tekan Enter untuk lanjut")

    if hapus_id in insiden:
        del insiden[hapus_id]
        print("Insiden berhasil dihapus.")
    else:
        print("ID tidak ketemu.")
    input("Tekan Enter untuk melanjutkan program")

# Lihat semua pengguna (Admin)
def lihat_pengguna():
    if len(pengguna) == 0:
        print("Belum ada pengguna terdaftar.")
    else:
        for username, data in pengguna.items():
            print(f"Username: {username}, Role: {data.get('role','user')}")
    input("Tekan Enter untuk melanjutkan program")

# Statistik insiden (rekursif)
def jumlah_insiden(data_list):
    if not data_list:
        return 0
    return 1 + jumlah_insiden(data_list[1:])

def statistik_insiden():
    if len(insiden) == 0:
        print("Belum ada insiden tercatat.")
    else:
        jumlah_status = {}
        for _, data in insiden.items():
            status = data.get("status", "unknown")
            jumlah_status[status] = jumlah_status.get(status, 0) + 1
        for status, jumlah in jumlah_status.items():
            print(f"{status}: {jumlah} insiden")
        total = jumlah_insiden(list(insiden.items()))
        print(f"Total seluruh insiden: {total}")
    input("Tekan Enter untuk lanjut")

# program utama
def main():
    admin = ("diftya", "042")
    login = False
    username_login = ""
    role = ""

    while True:
        clear()
        tampil_menu_awal()

        while True:
            try:
                menu_awal = int(input("Pilih menu: "))
                if menu_awal not in [1, 2, 3]:
                    print("Pilihan tidak valid")
                    input("Tekan Enter untuk lanjut")
                    continue
                break
            except ValueError:
                print("ValueError: input harus berupa angka!")
                input("Tekan Enter untuk lanjut")

        if menu_awal == 1:
            clear()
            print("======== LOGIN ========")
            username = input("Username: ")
            password = input("Password: ")

            if username == admin[0] and password == admin[1]:
                login = True
                username_login = username
                role = "admin"
                print("Login Berhasil (Admin)")
            else:
                ketemu = False
                for user, data in pengguna.items():
                    if user == username and data.get("password") == password:
                        login = True
                        username_login = username
                        role = data.get("role", "user")
                        ketemu = True
                        break
                if not ketemu:
                    print("Username atau password salah.")
            input("Tekan Enter untuk lanjut")

        elif menu_awal == 2:
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
            input("Tekan Enter untuk lanjut")

        elif menu_awal == 3:
            keluar_program("SISTEM MANAJEMEN INSIDEN (SIEM)")
            break

        # Setelah login
        while login:
            clear()
            if role == "user":
                print("=========== MENU UTAMA (USER) ===============")
                print(f"Login sebagai: {username_login}")
                print("1. Tambah Insiden")
                print("2. Lihat Insiden")
                print("3. Ubah Status Insiden")
                print("4. Filter Insiden")
                print("5. Logout")
            elif role == "admin":
                print("======== MENU UTAMA (ADMIN) =========")
                print(f"Login sebagai: {username_login}")
                print("1. Tambah Insiden")
                print("2. Lihat Insiden")
                print("3. Ubah Status Insiden")
                print("4. Statistik Insiden")
                print("5. Filter Insiden")
                print("6. Hapus Insiden")
                print("7. Lihat Semua Pengguna")
                print("8. Logout")

            # input pilih menu (validasi angka)
            while True:
                try:
                    pilih_menu = int(input("Pilih menu: "))
                    if role == "admin" and pilih_menu not in [1, 2, 3, 4, 5, 6, 7, 8]:
                        print("Pilihan tidak valid")
                        input("Tekan Enter untuk lanjut")
                        continue
                    if role != "admin" and pilih_menu not in [1, 2, 3, 4, 5, 6]:
                        print("Pilihan tidak valid")
                        input("Tekan Enter untuk lanjut")
                        continue
                    break
                except ValueError:
                    print("ValueError: input harus berupa angka!")
                    input("Tekan Enter untuk lanjut")

            
            if pilih_menu == 1:
                clear()
                tambah_insiden(username_login)

            elif pilih_menu == 2:
                clear()
                lihat_insiden(username_login, role)

            elif pilih_menu == 3:
                clear()
                ubah_status_insiden(username_login, role)

            elif pilih_menu == 4 and role == "admin":
                clear()
                statistik_insiden()

            elif pilih_menu == 4 and role != "admin":
                clear()
                filter_insiden(username_login, role)

            elif pilih_menu == 5 and role == "admin":
                clear()
                filter_insiden(username_login, role)

            elif pilih_menu == 5 and role != "admin":
                login = False
                username_login = ""
                role = ""
                print("Logout berhasil.")
                input("Tekan Enter untuk lanjut")

            elif pilih_menu == 6 and role == "admin":
                clear()
                hapus_insiden()

            elif pilih_menu == 7 and role == "admin":
                clear()
                lihat_pengguna()

            elif pilih_menu == 8 and role == "admin":
                keluar_program("SISTEM MANAJEMEN INSIDEN (SIEM)")
                login = False
                username_login = ""
                role = ""
                input("Tekan Enter untuk lanjut")

            else:
                print("Menu tidak valid.")
                input("Tekan Enter untuk lanjut")

# Jalankan program utama
if __name__ == "__main__":
    main()

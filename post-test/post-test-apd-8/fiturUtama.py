from datetime import datetime
from prettytable import PrettyTable
import os

# ===== VARIABEL GLOBAL =====
insiden = {}
pengguna = {}
daftar_status = {
    "open": "Insiden baru dilaporkan",
    "in progress": "Insiden sedang ditangani",
    "resolved": "Insiden berhasil diselesaikan",
    "closed": "Kasus telah ditutup",
}

# ===== FUNGSI UTILITAS =====
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampil_daftar_status():
    print("Pilihan status yang tersedia:")
    for k, v in daftar_status.items():
        print(f"- {k} : {v}")

def keluar_program(nama_program):
    print(f"Anda telah keluar dari program {nama_program}")

# ===== FITUR-FITUR =====
def tambah_insiden(username_login):
    clear()
    global insiden
    judul = input("Judul insiden: ")
    tingkat = input("Tingkat keparahan: ")
    status = "open"
    tanggal = str(datetime.now())[:16]
    id_counter = len(insiden) + 1

    insiden[id_counter] = {
        "id_counter": id_counter,
        "judul": judul,
        "tingkat": tingkat,
        "status": status,
        "tanggal": tanggal,
        "pemilik": username_login,
    }
    print("Insiden berhasil ditambahkan!")
    input("Tekan Enter untuk melanjutkan")
    clear()

def lihat_insiden(username_login, role):
    clear()
    if len(insiden) == 0:
        print("Belum ada insiden tercatat.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Judul", "Tingkat", "Status", "Tanggal", "Pemilik"]
        ditemukan = False
        for _, data in insiden.items():
            if role == "admin" or data["pemilik"] == username_login:
                table.add_row([
                    data["id_counter"],
                    data["judul"],
                    data["tingkat"],
                    data["status"],
                    data["tanggal"],
                    data["pemilik"]
                ])
                ditemukan = True
        if ditemukan:
            print(table)
        else:
            print("Tidak ada insiden yang dapat Anda lihat.")
    input("Tekan Enter untuk melanjutkan")
    clear()

def ubah_status_insiden(username_login, role):
    clear()
    global insiden
    try:
        ubah_id = int(input("Masukkan ID insiden: "))
    except ValueError:
        print("Input harus berupa angka!")
        input("Tekan Enter untuk melanjutkan")
        clear()
        return

    if ubah_id not in insiden:
        print("ID tidak ditemukan.")
        input("Tekan Enter untuk melanjutkan")
        clear()
        return

    data = insiden[ubah_id]
    if data["pemilik"] != username_login and role != "admin":
        print("Anda tidak memiliki izin untuk mengubah insiden ini.")
        input("Tekan Enter untuk melanjutkan")
        clear()
        return

    tampil_daftar_status()
    status_baru = input("Masukkan status baru: ")
    if status_baru not in daftar_status:
        print("Status tidak valid.")
    else:
        data["status"] = status_baru
        print("Status berhasil diubah.")
    input("Tekan Enter untuk melanjutkan")
    clear()

def filter_insiden(username_login, role):
    clear()
    tampil_daftar_status()
    status_filter = input("Masukkan status untuk filter: ")
    clear()

    table = PrettyTable()
    table.field_names = ["ID", "Judul", "Tingkat", "Status", "Tanggal", "Pemilik"]
    ditemukan = False
    for _, data in insiden.items():
        if data["status"] == status_filter and (role == "admin" or data["pemilik"] == username_login):
            table.add_row([
                data["id_counter"],
                data["judul"],
                data["tingkat"],
                data["status"],
                data["tanggal"],
                data["pemilik"]
            ])
            ditemukan = True

    if ditemukan:
        print(table)
    else:
        print("Tidak ada insiden dengan status tersebut.")
    input("Tekan Enter untuk melanjutkan")
    clear()

def hapus_insiden():
    clear()
    global insiden
    if len(insiden) == 0:
        print("Tidak ada insiden untuk dihapus.")
        input("Tekan Enter untuk melanjutkan")
        clear()
        return
    try:
        hapus_id = int(input("Masukkan ID insiden yang ingin dihapus: "))
    except ValueError:
        print("Input harus berupa angka!")
        input("Tekan Enter untuk melanjutkan")
        clear()
        return
    if hapus_id in insiden:
        del insiden[hapus_id]
        print("Insiden berhasil dihapus.")
    else:
        print("ID tidak ditemukan.")
    input("Tekan Enter untuk melanjutkan")
    clear()

def lihat_pengguna():
    clear()
    if len(pengguna) == 0:
        print("Belum ada pengguna terdaftar.")
    else:
        table = PrettyTable()
        table.field_names = ["Username", "Role"]
        for username, data in pengguna.items():
            table.add_row([username, data.get("role", "user")])
        print(table)
    input("Tekan Enter untuk melanjutkan")
    clear()

def jumlah_insiden(data_list):
    return 0 if not data_list else 1 + jumlah_insiden(data_list[1:])

def statistik_insiden():
    clear()
    if len(insiden) == 0:
        print("Belum ada insiden tercatat.")
    else:
        jumlah_status = {}
        for _, data in insiden.items():
            s = data["status"]
            jumlah_status[s] = jumlah_status.get(s, 0) + 1

        table = PrettyTable()
        table.field_names = ["Status", "Jumlah Insiden"]
        for k, v in jumlah_status.items():
            table.add_row([k, v])
        print(table)
        print(f"Total seluruh insiden: {jumlah_insiden(list(insiden.items()))}")
    input("Tekan Enter untuk melanjutkan")
    clear()

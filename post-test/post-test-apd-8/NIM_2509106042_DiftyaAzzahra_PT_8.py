from datetime import datetime
import os
from prettytable import PrettyTable

insiden = {}
pengguna = {}
daftar_status = {
    "open": "Insiden baru dilaporkan",
    "in progress": "Insiden sedang ditangani",
    "resolved": "Insiden berhasil diselesaikan",
    "closed": "Kasus telah ditutup",
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampil_daftar_status():
    print("Pilihan status yang tersedia:")
    for k, v in daftar_status.items():
        print(f"- {k} : {v}")

def keluar_program(nama_program):
    print(f"Anda telah keluar dari {nama_program}")

def tambah_insiden(username_login):
    global insiden
    clear()
    print("======== TAMBAH INSIDEN ========")
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

def lihat_insiden(username_login, role):
    clear()
    print("======== LIHAT INSIDEN ========")
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
    input("Tekan Enter untuk melanjutkan program")

def ubah_status_insiden(username_login, role):
    global insiden
    clear()
    print("======== UBAH STATUS INSIDEN ========")

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

def filter_insiden(username_login, role):
    clear()
    print("======== FILTER INSIDEN ========")
    tampil_daftar_status()
    while True:
        try:
            status_filter = input("Masukkan status untuk filter: ")
            if status_filter not in daftar_status:
                raise ValueError
            break
        except ValueError:
            print("Status tidak valid! Pilihan status: open, in progress, resolved, closed")
            input("Tekan Enter untuk lanjut")

    ditemukan = False
    table = PrettyTable()
    table.field_names = ["ID", "Judul", "Tingkat", "Status", "Tanggal", "Pemilik"]

    for id_insiden, data in insiden.items():
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
    input("Tekan Enter untuk lanjut")

def hapus_insiden():
    global insiden
    clear()
    print("======== HAPUS INSIDEN ========")
    if len(insiden) == 0:
        print("Tidak ada insiden untuk dihapus.")
        input("Tekan Enter untuk melanjutkan program")
        return
    
    # Tampilkan daftar insiden terlebih dahulu
    table = PrettyTable()
    table.field_names = ["ID", "Judul", "Tingkat", "Status", "Tanggal", "Pemilik"]
    for _, data in insiden.items():
        table.add_row([
            data["id_counter"],
            data["judul"],
            data["tingkat"],
            data["status"],
            data["tanggal"],
            data["pemilik"]
        ])
    print(table)
    
    try:
        hapus_id = int(input("\nMasukkan ID insiden yang ingin dihapus: "))
    except ValueError:
        print("Input harus berupa angka!")
        input("Tekan Enter untuk lanjut")
        return

    if hapus_id in insiden:
        del insiden[hapus_id]
        print("Insiden berhasil dihapus.")
    else:
        print("ID tidak ketemu.")
    input("Tekan Enter untuk melanjutkan program")

def lihat_pengguna():
    clear()
    print("======== DAFTAR PENGGUNA ========")
    if len(pengguna) == 0:
        print("Belum ada pengguna terdaftar.")
    else:
        table = PrettyTable()
        table.field_names = ["Username", "Role"]
        for username, data in pengguna.items():
            table.add_row([username, data.get("role", "user")])
        print(table)
    input("Tekan Enter untuk melanjutkan program")

def jumlah_insiden(data_list):
    if not data_list:
        return 0
    return 1 + jumlah_insiden(data_list[1:])

def statistik_insiden():
    clear()
    print("======== STATISTIK INSIDEN ========")
    if len(insiden) == 0:
        print("Belum ada insiden tercatat.")
    else:
        jumlah_status = {}
        for _, data in insiden.items():
            status = data.get("status", "unknown")
            jumlah_status[status] = jumlah_status.get(status, 0) + 1
        
        table = PrettyTable()
        table.field_names = ["Status", "Jumlah Insiden"]
        for status, jumlah in jumlah_status.items():
            table.add_row([status, jumlah])
        
        total = jumlah_insiden(list(insiden.items()))
        print(table)
        print(f"\nTotal seluruh insiden: {total}")
    input("Tekan Enter untuk lanjut")
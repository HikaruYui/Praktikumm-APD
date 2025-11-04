print("Program untuk menentukan jenis segitiga dan menghitung luasnya")
print("="*62)
max_percobaan = 5
percobaan = 0

while(percobaan < max_percobaan):
    username = str(input("Silakan masukkan username Anda: "))
    password = str(input("Silakan masukkan password Anda: "))
    if (username == "tya" or username == "diftya") and password == "042":
        print("Login Berhasil")
        break
    else:
        print("Login Gagal")
        print("Coba lagi")
        percobaan += 1
        if percobaan >= max_percobaan:
            print("Maaf, sisa percobaan Anda sudah habis.")
            exit()

tanya = "y"

while tanya == "y" or tanya == "Y":
    sisi_a = int(input("Input panjang sisi A: "))
    sisi_b = int(input("Input panjang sisi B: "))
    sisi_c = int(input("Input panjang sisi C: "))

    if sisi_a + sisi_b <= sisi_c or sisi_a + sisi_c <= sisi_b or sisi_b + sisi_c <= sisi_a:
        print("Bukan Segitiga")
    else:
        print("Terdefinisi sebagai segitiga.")
        if sisi_a == sisi_b == sisi_c:
            print("Merupakan segitiga sama sisi.")
        elif sisi_a == sisi_b or sisi_b == sisi_c or sisi_a == sisi_c:
            print("Merupakan segitiga sama kaki.")
        else:
            print("Merupakan segitiga sembarang.")

        pertanyaan_tambahan = input("Apakah anda ingin menghitung luas segitiga ini? (y/n) ")
        if pertanyaan_tambahan == "n" or pertanyaan_tambahan == "N":
            print("Terima kasih telah menggunakan program ini")
            
        elif pertanyaan_tambahan == "y" or pertanyaan_tambahan == "Y":
            alas = float(input("Input panjang alas : "))
            tinggi = float(input("Input tinggi : "))
            luas_segitiga = 0.5 * alas * tinggi
            print("Luas segitiga adalah", luas_segitiga)
            
        tanya = "x"
        while tanya not in ["y", "Y", "n", "N"]:
            tanya = str(input("Apakah anda ingin melanjutkan program? (y/n) "))
            if tanya == "n" or tanya == "N":
                tanya = "n"
                print("Terima kasih telah menggunakan program ini")
                exit()
            elif tanya == "y" or tanya == "Y":
                tanya = "y"
                print("Program Berlanjut")
                break
            else:
                print("Input tidak valid, program berhenti")
                print("Input tidak valid, silakan masukkan 'y' atau 'n'")
                continue

        




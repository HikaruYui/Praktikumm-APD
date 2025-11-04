#Pembuatan Fungsi Dengan Parameter
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print ("luas persegi panjang adalah ", luas)

#Pemanggilan Fungsi luas_persegi_panjang
luas_persegi_panjang(4, 5)

# Contoh Program mengembalikan hasil fungsi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# pemanggilan fungsi luas persegi
print ("Luas persegi :", luas_persegi(8))

# rumus: sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi

    print ("Volume Persegi = ", volume)

# pemanggilan Fungsi
luas_persegi(4)
volume_persegi(6)

# membuat variabel global
Nama = "Hambali"
Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

# membuat variabel lokal
def info():
    Nama = "Informatika"
    Mata_Kuliah = "Logika Informatika"

# mengakses variabel lokal
print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)

# mengakses variabel global
print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)

# memanggil fungsi info
info()

# Membuat set

# buah = {"apel", "jeruk", "mangga", "apel"]
# buah = (“apel”, “jeruk”, “mangga”, “apel”)

# Membuat set
# buah = {'apel', 'jeruk", "mangga", "apel"]
# buah = (['apel', “jeruk”, “mangga”, “apel”])
# print(buah)

# angka_ganjil = [1, 3, 5, 7, 9]

# unik = set(angka_ganjil)
# print(angka_ganjil)

# Dictionary
# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# print(Daftar_buku[buku_1])

Biodata = {
"Nama" : "Ananda Daffa Harahap",
"NIM" : 2409106050,
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Social Media" : {"Instagram" : "daffahrhap"}
}

# for i, j in Biodata.items():
#     print(i, j)
   
# #  .items buat ngambil value 

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("Nama"))

# Kalau pake get error nya bisa diganti jadi none
# kalau gapakai error

# Film ={
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"}
# print(Film)

# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})
# print(Film)

#  kalau list pakai append kalau dictionary pakai .update
# Film.pop('Sherlock Holmes')
# print(Film)

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][0])

# angka = {10, 11, 12}
# b = {11, 13, 14}
# c =  angka | b
# print(c)

# & = irisan
# | = himpunan semesta (gabungan)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# print("Nilai : ", Nilai.setdefault("Kimia", 70))

# mahasiswa = [["santoso", "dante","lina"],["tya, ammara"]]
# for i in mahasiswa:
#     for j in i: 
#         print(j)
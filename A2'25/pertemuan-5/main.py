#mendefinisikan list
matakuliah = ["PTI", "APD", "Kalkulus", "Orsikom"]
praktikum = ["Mahasiswa", 20, True, 45.10, ["APD", 25]]

# for i in matakuliah:
#     print(f"matakuliah {i}")

# enumerate adalah fungsi untuk membaca index

# for index, i in enumerate(matakuliah):
#     print(index, i )

# list bisa jadi database

# print(dir(list))
# print(matakuliah[1:3])
# print(matakuliah[-1])
# print(matakuliah[1:3:2])

# matakuliah.append("matdis")
# print(matakuliah)

# matakuliah.insert(1, "alpro")
# matakuliah.insert(3, "kriptografi")
# matakuliah.insert(-1, "logmat")
# print(matakuliah)

# praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# print(praktikum[4][0])

# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# studyclub[2] = "web"
# print(studyclub)

# del = hapusnya speifik di indeks tertentu

# del matakuliah[1]
# print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# # matakuliah.remove("Kalkulus")

# # kalo mau hapus dari belakang pakai pop
# # pop juga bisa disimpan ke variabel
# #  misal

# hapus = matakuliah.pop()

# # matakuliah.pop(2)
# print(hapus)

# a = [1, 2, 3]
# b = [4, 5, 6]

# hasil = a + b
# kali = a * 3
# print(hasil)
# print(kali)
# print (sum(a)/len(a))

kelas = [
    ["Ridho", "Lian", "Nabil"],
    ["Daffa", "Dante", "Santoso"],
    ["Pernanda", "Riyadi", "Ahnaf"],
]

# kelas[1].append("lima")
# print(kelas)

for i in kelas:
    for nama in i:
        print(nama)

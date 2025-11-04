# for i in range(10):
#     print(i + 1)

# [0,1,2,3,4,5,6,7,8,9]

# for i in range(1,11,2):
#     print(i) 

# nama = ['bakil', 'diftya', 'anugerah']

# for i in nama:
#     print(i)

# for j in range(3):
#     print("Raffi")

# while loop
# jawab = 'ya'
# hitung = 0

# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi? ")

# print(f"Total jawab: {hitung}")

# cuaca = "hujan"

# while(cuaca == "hujan" or cuaca == "Hujan"):
#     print("jangan keluar rumah")
#     cuaca = input("Masukkan cuaca hari ini: ")

# print("pergi ke luar rumah")

# angka = 10

# while(angka > 1):
#     print(angka)
#     angka -= 2
# selama angka lebih besar dari 10, maka akan dikurang 2, 
# sampai kondisi bernilai false

# for i in range(1,5):
#     for j in range(1,5):
#         print(f" {i} x {j} = {i * j}")
#     print()

# for i in range(0,2):
#     kanan()
#     atas()

# break

# angka = [2, 5, 8, 12, 15, 7, 20]

# print("Mencari angka pertama yang lebih besar dari 10...")

# for i in angka:
#     print(f"Memeriksa angka: {i}")
#     if i > 10:
#         print(f"{i} lebih besar dari 10")
#         break
    
# print("program selesai")

# continue

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     print(f'angka ditemukai yaitu: {i}')

# print("program selesai")

# list comprehension
# kuadrat = [i**2 for i in range(1,6)]
# print(kuadrat)
# # output = list

# for i in range(1,6):
#     print(i**2)
# # output = integer

# angka_genap = [x for x in range (1,11) if x % 2 == 0]
# print(angka_genap)

# for x in range(1,11):
#     if x % 2 == 0:
#         print(x)



# for i in range(2,11):
#     print(i)



# while True:
#     if kpk % x == 0 and kpk % y == 0:
#         break
#     kpk += 1


# for i in range(1,6):
#     print('*' * i)

# # segitiga sama kaki

# for i in range(1,7):
#     print(' ' * (6-i) + '*' * (2*i-1))
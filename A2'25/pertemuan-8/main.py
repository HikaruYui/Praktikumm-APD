num = int("42") # 42
name = str(123) # "123"
data = list("abc") # ['a', 'b', 'c']
data = dict(a=1, b=2) # {'a': 1, 'b': 2}
print(type(data)) #


angka = 10
print(bin(angka))  # Output: 0b1010

nilai = 0
print(bool(nilai))  # Output: False

data = dict(nama="Budi", umur=17)
print(data)  # Output: {'nama': 'Budi', 'umur': 17}

angka = 7
print(float(angka))  # Output: 7.0

buah = frozenset(["apel", "jeruk", "mangga"])
print(buah)  # Output: frozenset({'apel', 'jeruk', 'mangga'})

angka = int(7.9)
print(angka)  # Output: 7

teks = "halo"
print(list(teks))  # Output: ['h', 'a', 'l', 'o']

angka = [1, 2, 2, 3, 3]
print(set(angka))  # Output: {1, 2, 3}

angka = 123
print(str(angka))  # Output: '123'

data = [1, 2, 3]
print(tuple(data))  # Output: (1, 2, 3)

x = 10
print(type(x))  # Output: <class 'int'>

angka = -10
print(abs(angka))  # Output: 10

hasil = divmod(17, 5)
print(hasil)         # Output: (3, 2)
print(hasil[0])      # hasil bagi → 3
print(hasil[1])      # sisa bagi  → 2

angka = [4, 9, 1, 7]
print(max(angka))  # Output: 9
print(min(angka))  # Output: 1

print(pow(2, 3))       # 2³ = 8
print(pow(2, 3, 5))    # (2³) % 5 = 3

print(round(3.14159))     # Output: 3
print(round(3.14159, 2))  # Output: 3.14

angka = [1, 2, 3, 4, 5]
print(sum(angka))  # Output: 15

buah = ["apel", "pisang", "mangga"]
for i, item in enumerate(buah):
    print(i, item)

angka = [10, 20, 30]
it = iter(angka)
print(next(it))  # 10
print(next(it))  # 20

angka = [1, 2, 3, 4]
print(list(reversed(angka)))  # Output: [4, 3, 2, 1]

angka = [10, 20, 30, 40, 50]
potongan = slice(1, 4)
print(angka[potongan])  # Output: [20, 30, 40]

data = [3, 1, 4, 2]
print(sorted(data)) 

nama = ["Ani", "Budi", "Cici"]
umur = [17, 18, 19]
gabung = zip(nama, umur)
print(list(gabung))
      
angka = [1, 2, 3, 4, 5, 6]
genap = filter(lambda x: x % 2 == 0, angka)
print(list(genap))  # Output: [2, 4, 6]


angka = [1, 2, 3, 4]
kuadrat = map(lambda x: x ** 2, angka)
print(list(kuadrat))  # Output: [1, 4, 9, 16]

huruf = "a,b,c"
ganti = huruf.split(',')
print(ganti)

import inquirer
pertanyaan = [
    inquirer.List(
        "bahasa",
        message="Kamu mau belajar bahasa apa?",
        choices=["Python", "Java", "C++", "JavaScript"]
    )
]

jawaban = inquirer.prompt(pertanyaan)
print("Kamu memilih:", jawaban["bahasa"])
#1. Kamu bisa menyetak kata atau kalimat dengan perintah print("isi kata")
print("1. Langkah Pertama Cetak tulisan")
print("hello world")

#2. Bagian kedua kamu bisa memasukan sebuah variabel , 
#   sebagai contoh variabel untuk memunculkan nama
print()
print("2.Tutorial Memunculkan Variabel String/Integer")
nama = "Rizki"
print("Halo semua nama saya", nama)

#3. kamu bisa juga membuat perhitungan matematika dengan python, sama seperti 
#   semua bahasa pemrograman bisa di implementasikan 
print()
print("3.Tutorial Perhitungan Matematika")
a = 1
b = 9
total = a + b
print(a,"+",b)
print("Hasil pertambahan diatas =",total)

#4. kamu bisa membuat beberapa perulangan seperti for, dan while
print()
print("4.Tutorial Perulangan For untuk range interval")
for i in range(0,7):
    print (i)

print()
print("4.Tutorial Perulangan Urutan String")
x = "abc" 
for i in x:
    print (i)

print()
print("4.Tutorial Perulangan Urutan List Seperti Array")
y = ["Andi", "Toto", "Fenix"]
for i in y:
    print (i)

print()
print("4.Tutorial Perulangan Urutan List dengan Else")
x = ["Andi", "Toto", "Fenix", "Filix"]

for i in x:
    print(i, "panjang elemen list", len(i))
else:
    print("Semua isi list telah dijalankan")
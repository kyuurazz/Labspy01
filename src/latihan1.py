print("Latihan 1 if statement")
print("======================")

bil1 = int(input("Masukan Bilangan Pertama : "))
bil2 = int(input("Masukan Bilangan Kedua   : "))

hasil = 0

if (int(bil1) > bil2):
    hasil = bil1
else:
    hasil = bil2
    
print("Bilangan Terbesar Adalah", hasil)
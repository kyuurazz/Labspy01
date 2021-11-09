print("Latihan 4 Bilangan acak")
print()

from random import random
n = int(input("Masukan Nilai N: "))
for i in range(n):
    while True:
        n = random()
        if n < 0.5:
            break
    print(n)
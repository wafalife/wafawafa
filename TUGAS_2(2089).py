
x = int(input("Masukkan Bilangan Bulat :"))

y = " Bilangan yang anda entrikan adalah Bilangan Genap "
z = " Bilangan yang anda entrikan adalah Bilangan Gasal "

a = " dan termasuk nilai kecil "
b = " dan terasuk nilai sedang "
c = " dan termasuk nilai besar "

# Ganjil/Genap

if x % 2 == 0:
    print(y)
else:
    print(z)

# Nilai Kecil/sedang/besar

if x < 10:
    print(a)

elif x > 50:
    print(c)

elif x < 10 > 50 :
    print(b)

# pegulangan



print('='*5,"For",'='*5)
for a in [1, 2, 3 , 4, 5, 6, 7, 8, 9]:
    print("ini adalah pengulangan:", a)
print('='*5,"While",'='*5)
a = 1
while a <= 9:                               # while apaan # jelaskan # while digunakan untuk melakukan pengulangan selama kondisi True
    print("ini adalah pengulangan:", a)
    a += 1
print('='*5,"Break",'='*5)
for a in [1, 2, 3 , 4, 5, 6, 7, 8, 9]:
    if a == 5:
        print("break pada angka:", a)
        break                               # jelaskan # break digunakan untuk menghentikan pengulangan
    print("ini adalah pengulangan:", a)
print('='*5,"Continue",'='*5)
for a in [1, 2, 3 , 4, 5, 6, 7, 8, 9]:
    if a == 5:
        print("continue pada angka:", a)
        continue                            # jelaskan # continue digunakan untuk melewati iterasi saat kondisi terpenuhi
    print("ini adalah pengulangan:", a)     # maksudnya adalah jika a == 5 maka akan melewati iterasi tersebut dan melanjutkan ke iterasi berikutnya
print('='*5,"Pass",'='*5)
for a in [1, 2, 3 , 4, 5, 6, 7, 8, 9]:
    if a == 5:
        print("pass pada angka:", a)
        pass                                  # jelaskan # pass digunakan untuk melewati iterasi tanpa melakukan apapun
    print("ini adalah pengulangan:", a)       # maksudnya adalah jika a == 5 maka akan melewati iterasi tersebut dan melanjutkan ke iterasi berikutnya
# # Latihan
# Buatlah program yang meminta input dari user berupa angka,

inputUser = str(input("masukna kata kata :\t"))
for i in [1, 2, 3, 4, 5]:
    print(f"Kamu mengetik {inputUser} : {i}")
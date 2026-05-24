# for Loop (perulangan)
print("="*5, "FOr Loop", "="*5)
for i in (1, 2, 3, 4, 5):
    print(f"Perulangan ke-{i} ")

print("="*5, "for Loop dengan range", "="*5)
for i in range(5):
    print(f"Perulangan ke-{i} ")

print("="*5, "for Loop dengan star and stop", "="*5)
for i in range(1, 5):
    print(f"Perulangan ke-{i} ")

print("="*5, "cara lain", "="*5)
number_list = [1, 2, 3, 4, 5]
for i in number_list:
    print(f"Perulangan ke-{i} ")

print("="*5, "Melompati 2 ", "="*5)
for i in range(1, 10, 2):
    print(f"Perulangan ke-{i} ")

print("="*5, "Mencetak string", "="*5)
string = "Python"
for i in string:
    print(f"Perulangan ke-{i} ")


print("="*5, "angka bertambah", "="*5)
angka = 0
for i in range(1, 11):
    angka += i
    print(f"Perulangan ke-{i} angka bertambah menjadi {angka}")

print("="*5, "Membuat segitiga bintang", "="*5)
number = 0 
for i in range(1,10):
    number += 1     # jelaskan # number = number + 1 
 # number += 1 adalah cara singkat untuk menambahkan 1 ke variabel number
    # print(f"Perulangan ke-{i} angka bertambah menjadi {number}")
    print("*" * number)




































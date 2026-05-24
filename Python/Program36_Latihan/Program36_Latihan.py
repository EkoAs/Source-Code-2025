# latihan for loop
userInput = str(input("Masukan Simbol: \t"))
number = 0
for i in range(1, 15):
    number = number + 1 # atau bisa menggunakan number += 1
    print(f"{userInput} " * number)  # mencetak simbol sesuai dengan jumlah perulangan
    # print(f"{userInput} " * number)  # cara lain untuk mencetak simbol sesuai dengan jumlah perulangan
# apapun yang ada di dalam for akan di ulang sesuai jumlah range yang ditentukan 

number = 15 
for i in range(1, 15):
    number -= 1  # mengurangi nilai number setiap perulangan
    print(f"{userInput} " * number)  # mencetak simbol sesuai dengan jumlah perulangan yang berkurang
    # print(f"{userInput} " * number)  # cara lain untuk mencetak simbol sesuai dengan jumlah perulangan yang berkurang
    
# apapun yang ada di dalam for akan di ulang sesuai jumlah range yang ditentukan
# latihan for loop dengan kondisi
for i in range(1, 15):
    if i % 2 == 0:  # jika i genap
        print(f"{userInput} " * i)  # mencetak simbol sesuai dengan jumlah perulangan genap
    else:
        print(f"{userInput} " * (i - 1))  # mencetak simbol sesuai dengan jumlah perulangan ganjil dikurangi satu
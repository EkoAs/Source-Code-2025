# write eksternal file

# mode write
with open("data1.txt",mode='w',encoding='utf-8') as file:
    file.write("Ini adalah data pertama\n")
    file.write("Ini adalah data kedua\n")
    file.write("Ini adalah data ketiga\n")
    
# mode append # menambahkan data ke file
# jika file tidak ada, maka akan dibuatkan file baru
with open("data1.txt",mode='a',encoding='utf-8') as file:
    file.write("Ini adalah data keempat\n")
    file.write("Ini adalah data kelima\n")
    
# mode r+ # read and write
# jika file tidak ada, maka akan error
# with open("data1.txt",mode='r+', encoding='utf-8') as file:
#     content = file.read()
#     print(content, end=" ")
#     file.write("Ini adalah data terakhir\n")
#     file.write("Ini adalah data ke enam\n") # akan menimpa data
#     file.seek(0,2)
#     # file.write("Ini adalah data ke enam\n") # akan menimpa data
    # file.write("ini adalah data terpanjang\n") # kok ga terbaca? 
    # file.seek(0) # pindah ke awal file
    # print(file.read()) # baca file

with open("data1.txt", mode='r+', encoding='utf-8') as file:
    file.seek(0, 2)  # pindah ke akhir file
    file.write("Ini adalah data tambahan dengan r+\n")
    file.seek(0)     # pindah ke awal file
    content = file.read()
    print(content, end=" ")

# mode w+ # write and read
# jika file tidak ada, maka akan dibuatkan file baru
# with open("data1.txt", mode='w+', encoding='utf-8') as file:
#     file.write("ini adalah data super terakhir\n") # tambahkan data ke terakhir
    
#     # file.seek(0) # pindah ke awal file
#     # baca file
#     content = file.read()
#     print(content,end=" ")
    
with open("data1.txt", mode='w+', encoding='utf-8') as file:
    file.write("ini adalah data super terakhir\n")
    file.seek(0)  # pindah ke awal file
    content = file.read()
    print(content, end=" ")
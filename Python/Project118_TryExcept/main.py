# cara mengatasi error
from math import nan
# contoh
# data = int(input("angka :"))
# hasil = nan
# try:
#     hasil = 10/data # kalo ini berhasil tidak error makanyg bawah gak di cetak
# except:
#     print("hasil tidak boleh 0") # kalo ada yang error yg ini akan di cetak
    
# print(f"haisil = {hasil}")


# # kalo di aplikasi
# while(True):
#     angka = int(input("maukan angka:"))
#     try:
#         hasil = 10/angka
#         print(f"hasil = {hasil}")
#         done = input("y/n")
#         if done != 'y':
#             break # akan terus berlanjut programnya. kalo input salah bakal minta lagi yang benar
#     except:
#         print("pembagi nol")
        
# print("end the program")

# # untuk memebuka file dan membuat file
# while(True):
#     try:
#         with open("data.txt",'r') as file:
#             print(file.read())
#         break
#     except:
#         print(f"data file tidak di temukan. membuat file baru")
#         with open("data.txt", 'w',encoding='utf-8') as file:
#             file.write("file baru") #kalo file gada bakal ngebuat file baru
#         break
# print("end the program")


# 
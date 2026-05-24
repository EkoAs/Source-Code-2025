# cara membaca file eksternal
print(3*"=","membaca file txt",3*"=")  
# membaca seluruh isi file
file = open("datatxt.txt",mode="r")
print(file.read())

# baca file per baris
print("Baca file per baris:")
# print(file.readline())
# print(file.readline())

# baca sebagal list
# print(file.readlines(), end=" ")

# # cara tutup file
# print(f"File sudah di tutup : {file.closed}")
# # menutup file
# file.close()
# print(f"File sudah di tutup : {file.closed}")

print(3*"=","membaca file dengan with",3*"=")
with open("datatxt.txt",mode="r") as file:
    content = file.read()
    print(content, end=" ")
# menutup file secara otomatis
# tidak perlu menutup file secara manual
print(f"File sudah di tutup : {file.closed}")
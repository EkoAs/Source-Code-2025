'''Default Fungsi Argumen'''

# Contoh satu
def helo(nama = "Bukan Ucup"):
    print(f"Halo {nama}")
helo()  # Memanggil fungsi tanpa argumen, akan menggunakan nilai default
helo("Ucup")  # Memanggil fungsi dengan argumen, akan menggantikan nilai default

# contoh dua
# akses langsung ke argumen default
def tambah(angka, angka1):
    hasil = angka + angka1
    return hasil
y = tambah(2, 3)  # Memanggil fungsi dengan argumen
x = tambah(angka1 = 5, angka = 9)
print(y,x)  # Output: 5 dan 14

# contoh 3
# modifikasi argumen default
def modif(input0 = 2, input1 = 1, input3 = 3, input4 = 4):
    hasil = input0 + input1 + input3 + input4
    return hasil
print(f"{modif()}")
print(f"{modif(input3 = 10)}") # mengubah nilai input3, dan yang default akan digantikan

def operator():
    while True:
        num = input("Masukkan angka: ")
        num2 = input("Masukkan angka ke dua: ")
        if num.isdigit() and num2.isdigit():
            num = float(num)
            num2 =float(num2)
            break
        else:
            print("Input harus angka. Silakan masukkan angka yang benar.")
    return num, num2

num, num2 = operator()
print(f"Angka pertama: {num}, Angka kedua: {num2}")
print(f"Perkalian: {num} x {num2} = {num * num2}")
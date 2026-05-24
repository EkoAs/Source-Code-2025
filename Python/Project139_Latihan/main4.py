def luas():
    panjang = int(input("Masukkan panjang: "))
    lebar = int(input("Masukkan lebar: "))
    luas = panjang * lebar
    print(f"Luas persegi panjang: {luas} cm^2")
    
    return luas
luas_persegi_panjang = luas()
inputUser = str(input("masukan sesuatu :"))
format = int(f"{len(inputUser)}")
inputUser2 = str(input("masukan sesuatu :"))
formats = int(f"{len(inputUser2)}")
if format > 5:
    nilai = f"({format:03d})"
    maka = f"({len(nilai)})"
    print(f"Nilai {format} adalah {nilai} dan {inputUser2} maka {formats}")
    print(f"Sedangkan nilai len adalah {nilai} To {maka}")
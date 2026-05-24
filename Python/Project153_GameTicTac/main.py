
papan =["1","2","3","4","5","6","7","8","9"]
pemain = "C"
total = 0

while(True):
    print(f"{papan[0]} | {papan[1]} | {papan[2]}")
    print(f"{papan[3]} | {papan[4]} | {papan[5]}")
    print(f"{papan[6]} | {papan[7]} | {papan[8]}")
    
    user = input("Masukkan angka 1-9 untuk memilih posisi: ")
    if user not in papan:
        print("Masukan input yag benar!!")
        continue
    
    indeks= int(user) - 1
    
    if papan[indeks] in ["X","O"]:
        print("Posisi sudah terisi, pilih posisi lain!!")
        continue
    papan[indeks] = pemain  
    total+=1
    
    menang =False
    
    if (papan[0] == papan[1] == papan[2]) or (papan[3] == papan[4] == papan[5]) or (papan[6] == papan[7] == papan[8]) or (papan[0] == papan[3] == papan[6]) or (papan[1] == papan[4] == papan[7]) or (papan[2] == papan[5] == papan[8]) or (papan[0] == papan[4] == papan[8]) or (papan[2] == papan[4] == papan[6]):
        menang = True
    
    if menang:
        print(f"{papan[0]} | {papan[1]} | {papan[2]}")
        print(f"{papan[3]} | {papan[4]} | {papan[5]}")
        print(f"{papan[6]} | {papan[7]} | {papan[8]}")
        print(f"Selamat {pemain} menang!!")
        
        break        
    elif total == 9:
        print(f"{papan[0]} | {papan[1]} | {papan[2]}")
        print(f"{papan[3]} | {papan[4]} | {papan[5]}")
        print(f"{papan[6]} | {papan[7]} | {papan[8]}")
        print("Permainan seri!!")
        break
    else:
        
        pemain="O" if pemain == "C" else "C"
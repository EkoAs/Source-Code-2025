
import os as OS
sistem = OS.name

if __name__ == "__main__":
    match sistem:
        case "nt": OS.system("cls")
    class Conditionals:
        def __init__(self):
            pass
        
        
        def Tugas_awal():
            user_1 = input("Masukan bilangan bulat: ")
            if user_1.isdigit():
                user_1 = int(user_1)
                if user_1 == 0:
                    print(f"{user_1} adalah bilangan negatif")
                else:
                    print
                    
                    
                    
        def Tugas_dua():
            suhu = input("masukan suhu: ")
            if suhu.isdigit():
                suhu= int(suhu)
                if suhu <= 0:
                    print(f"Suhu {suhu} adalah bentuk es")
                elif suhu >= 100:
                    print(f"Suhu {suhu} adalah bentuk gas")
                else:
                    print(f"Suhu {suhu} dalam kondisi air normal")
                    
                    
                    

        def Tugas_tiga():
            users = input("Masukan Sebuah angka: ")
            if users.isdigit():
                users = int(users)
                if ((users <= 100) and (users > 80)):
                    print(f"Bilangan {users} Masuk kategori A")
                elif ((users <= 80) and (users > 60)):
                    print(f"Bilangan {users} Masuk kategori B")
                elif ((users <= 60) and (users > 40)):
                    print(f"Bilangan {users} Masuk kategori C")
                elif ((users <= 40) and (users > 20)):
                    print(f"Bilangan {users} Masuk kategori D")
                elif ((users <=20) and (users > 0)):
                    print(f"Bilangan {users} Masuk kategori E")
                else:
                    print(f"NILAI A++++=")
                    return 0
                
                
                
                
        def Loop_terus():
           for genap in range(1,100):
               if ((genap % 2) == 0):
                    print(f"Bilang {genap} Adalah Genap")
               else:
                   print(genap)
                    
    
    
    Conditionals.Loop_terus()
        
else:
    print(f"System is not respoding")

print(f"Perogram telah berakhir")
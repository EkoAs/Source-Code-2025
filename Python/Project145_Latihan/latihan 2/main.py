
import os as OS
sistem = OS.name


if __name__=="__main__":
    class Games:
        def __init__(self,name,hp,attack):
            self.name = name
            self.hp = hp
            self.attack = attack
            Games.attack()
        def attack(self):
            pass
            
            
        def looping(self=None):
            while(True):
                nilai = input(f"masukan input: ")
                if nilai.isdigit():
                    nilai =int(nilai)
                    break
                else:
                    print("input bukan angka!")
                    continue
            while(nilai>0):
                print(f"Loop ke {nilai}")
                nilai -=1
            print(f"\nProgram berakhir.")
            
            
        
        def name(self=None):
            while(True):
                user_name = input(f"Masukan nama (ketik 1 untuk stop): ")
                if (user_name == "1"):
                    break
                else:
                    print(f"Halo {user_name}")
            print(f"\nProgram berakhir")
    Games.name(self=None) 
            
            
            
            
    # def forloop():
    #     for i in range(1,9):
    #         if (i==2):
    #             continue
    #         print(f"{i} ")

    # forloop()
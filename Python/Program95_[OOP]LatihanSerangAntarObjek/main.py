# game sederhana saling serang
# hero, punya nama,  hp, attack power, defense power
# membuat hero 1 nyerang hero 2, begitu sebaliknya
# jika salah satu di serang, maka yg diserang akan diserang dan bertahan, begitu sebaiknya

# dua hero saling serang, jika di serang maka hp nya akan berkurang
class Hero:
    def __init__(self,name,health,attackPower,defensePower):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.defensePower = defensePower
    def serang(self,lawan):
        print(f"{self.name} Menyerang dengan attack power {self.attackPower} pada {lawan.name}\n")
        lawan.diserang(self, self.attackPower) # memanggil fungsi bawah jika diserang
        
    def diserang(self,lawan, attackPower_lawan):
        print(f"{self.name} diserang {lawan.name}")
        attackTrima = attackPower_lawan / self.defensePower
        print(f"{self.name} terkena {str(attackTrima)} HP")
        self.health -= attackTrima
        print(f"darah {self.name} tersisa {str(self.health)} HP\n")


# sniper.serang(figher)
print("\n")
def inputUS():
    print('''
          1. Sniper
          2. Fighter
          3. TeamZ
          4. ZeroHunter
          5. KruTank
          6. PenembakRunduk
          7. Captain
          8. RedBarret
          9. KamikazeDrone
          ''')
    inputHero = int(input("Masukan Hero Pilihan :"))
    heroLawan = int(input("masukan Hero Lawan :"))
    
    # tamplate nama, hp, attackpower, defense
    heroAll = {
        1: Hero('Sniper',50,90,90),
        2: Hero('Fighter',80,35,40),
        3: Hero('TeamZ',120,30,80),
        4: Hero('ZeroHunter', 90, 70,50),
        5: Hero('KruTank',40,30,20),
        6: Hero('PenembakRunduk',30,70,75),
        7: Hero('Captain', 150, 40, 85),
        8: Hero('RedBarret', 70, 60, 65),
        9: Hero('KamikazeDrone', 20, 200, 10)
    }
    if inputHero in heroAll and heroLawan in heroAll :
        hero1 = heroAll[inputHero]
        hero2 = heroAll[heroLawan]
        print(f"Kamu memilih {hero1.name} dan melawan {hero2.name}")
        return hero1, hero2
    else: 
        print(f"Pilihan tidak valid!")
        return inputUS()
    
    
# game loop
while True:
    hero1, hero2 = inputUS()
    while hero1.health > 0 and hero2.health > 0:
        hero1.serang(hero2)
        if hero2.health <= 0:
            print(f"{hero2.name} Kalah!")
            break
        hero2.serang(hero1)
        if hero1.health <= 0:
            print(f"{hero1.name} Kalah!")
            break
        else:
            print(f"Semuanya kalah!")
    # Tanyakan apakah ingin bermain lagi
    play_again = input("Ingin bermain lagi? (y/n): ")
    if play_again.lower() != 'y':
        break
    
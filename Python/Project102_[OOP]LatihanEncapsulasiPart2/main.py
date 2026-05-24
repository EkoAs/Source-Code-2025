class Hero:
    __num = 0
    def __init__(self,name,health,attackpower,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attackpowerStd = attackpower
        self.__armorSts = armor
        self.__level = 1
        self.__exp = 0
        # bagian max max nya
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attackpowerStd *  self.__level
        self.__armor = self.__armorSts *  self.__level
        
        self.__health = self.__healthMax
        Hero.__num += 1
        # bagian info
    def info(self):
        print("{} memiliki {}".format(self.name,self.health))
        
        
        
        
        
    @property
    def info(self):
        return "{} level {}:\n health = {}/{} \n attack = {} \n armor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)

    # bagian setter
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(f"\n{self.__name} Naik Level!\n")
            self.__level += 1
            self.__exp -= 100
            
            # mengulang dan memanggil yang maksimumnya
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attackpowerStd *  self.__level
            self.__armor = self.__armorSts *  self.__level

        
    def serang(self,lawan):
        self.gainExp = 5
        print(f"{self.__name} kamu mendapatkan {self.exp} exp ")
        print(f"{lawan.__name} kamu mendapatkan {lawan.exp} exp ")
        print(f"{self.__name} Menyerang dengan attack power {self.__attPower} pada {lawan.name}\n")
        lawan.diserang(self, self.attPower) # memanggil fungsi bawah jika diserang
        
    def diserang(self,lawan, attackPower_lawan):
        
        print(f"{self.__name} diserang {lawan.name}")
        attackTrima = attackPower_lawan / self.defensePower
        print(f"{self.name} terkena {str(attackTrima)} HP")
        self.health -= attackTrima
        print(f"darah {self.name} tersisa {str(self.health)} HP\n")

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = max(0, value)

    @property
    def defensePower(self):
        return self.__armor

    @property
    def attPower(self):
        return self.__attPower
    
    @property
    def exp(self):
        return self.__exp
    
    @exp.getter 
    def exp(self):
        return self.__exp

class HeroBest(Hero):
    def __init__(self,name):
        super().__init__(name, 200)
        super().info()

print("\n")
def inputUS():
    comanndo = ('''
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
    
    best = ('''
            1. Intellegent
            2. Pilots
            3. Sniper ++
            4. Figher ++
            5. Heavy Weapons
            6. Zenda Maria
            7. Snow Tiger
            8. Sniper (Exssutif++)
            
            
            ''')
     # tamplate nama, hp, attackpower, defense
    heroAll = {
        1: Hero('Sniper',50,90,1),
        2: Hero('Fighter',80,35,10),
        3: Hero('TeamZ',120,30,80),
        4: Hero('ZeroHunter', 90, 70,50),
        5: Hero('KruTank',40,30,20),
        6: Hero('PenembakRunduk',30,70,75),
        7: Hero('Captain', 150, 40, 85),
        8: Hero('RedBarret', 70, 60, 65),
        9: Hero('KamikazeDrone', 20, 200, 10)
    }
    # tamplate nama, hp, attackpower, defense
    bestHero = {
        1:Hero("Intellegent",200,50,250 ),
        2:Hero("Pilots",160,30,150 ),
        3:Hero("Sniper ++",350,250,650 ),
        4:Hero("Figher ++",200,40,50 ),
        5:Hero("Heavy Weapons",250,450,150 ),
        6:Hero("Zenda Marina",220,55,450 ),
        7:Hero("Snow Tiger",260,45,450 ),
        8:Hero("Sniper (Best++)",350,750,1250 )
    }
    
    pilihan = str(input("Pilih kategori Hero : "))
    if pilihan.lower() != "best":
        print(comanndo)
        inputHero = int(input("Masukan Hero Pilihan :"))
        heroLawan = int(input("masukan Hero Lawan :"))
        if inputHero in heroAll and heroLawan in heroAll :
            hero1 = heroAll[inputHero]
            hero2 = heroAll[heroLawan]
        else:
            print("try again")
            return inputUS()
    else:
        print(best)
        inputHero = int(input("Masukan Hero Pilihan :"))
        heroLawan = int(input("masukan Hero Lawan :"))
        if inputHero in bestHero and heroLawan in bestHero :
            hero1 = bestHero[inputHero]
            hero2 = bestHero[heroLawan]
        else:
            print("try again")
            return inputUS()
    return hero1, hero2
        
    
# game loop
while True:
    hero1, hero2 = inputUS()
    while hero1.health > 0 and hero2.health > 0:
        hero1.serang(hero2)
        if hero2.health <= 0:
            print(f"{hero2.name} Kalah!")
            # print(hero2.info)
            break
        hero2.serang(hero1)
        if hero1.health <= 0:
            print(f"{hero1.name} Kalah!")
            # print(hero1.info)
            break
        else:
            print(f"Semuanya kalah!")
    print(f"\n\n{5*'='}Info Akhir Kedua Hero{5*'='}")
    print(hero1.info,"\n")
    print(hero2.info,"\n")
    # Tanyakan apakah ingin bermain lagi
    
    play_again = input("Ingin bermain lagi? (y/n): ")
    if play_again.lower() != 'y':
        break
print("\n\n")
print(hero1.info)
print("\n")
print(f"\nTotal EXP {hero1.name}: Level {hero1._Hero__level}, {hero1.exp}/100 exp")
print(f"Total EXP {hero2.name}: Level {hero2._Hero__level}, {hero2.exp}/100 exp")
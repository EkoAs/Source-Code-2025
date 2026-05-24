
from data.hero import Hero, BestHero, IntellegentHero
class UserIN:
    @staticmethod
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
            1: Hero('Sniper',50, 70, 20),
            2: Hero('Fighter', 40, 30, 50),
            3: Hero('TeamZ',60, 30, 40),
            4: Hero('ZeroHunter', 60, 50, 20),
            5: Hero('KruTank',20, 40, 5),
            6: Hero('PenembakRunduk', 45, 65, 50),
            7: Hero('Captain', 80, 20, 95),
            8: Hero('RedBarret',65, 60, 120),
            9: Hero('KamikazeDrone', 10, 150, 5)
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
        while True:
            pilihan = str(input("Pilih kategori Hero : "))
            if pilihan.lower() != "best":
                print(comanndo)
                inputHero = int(input("Masukan Hero Pilihan :"))
                heroLawan = int(input("masukan Hero Lawan :"))
                if inputHero in heroAll and heroLawan in heroAll :
                    hero1 = heroAll[inputHero]
                    hero2 = heroAll[heroLawan]
                    return hero1, hero2
                else:
                    print("try again")
                    continue
            else:
                print(best)
                inputHero = int(input("Masukan Hero Pilihan :"))
                heroLawan = int(input("masukan Hero Lawan :"))
                if inputHero in bestHero and heroLawan in bestHero :
                    hero1 = bestHero[inputHero]
                    hero2 = bestHero[heroLawan]
                    return hero1, hero2
                    
                else:
                    print("try again")
                    continue
            

inputUS = UserIN.inputUS       
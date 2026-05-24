# latian 
# menggunakan sub class yang kelakuannya beda beda
# from data.daftarHero import inputUS
class Hero:
    """
    # Hero class
    # -------------
    # Representasi karakter hero dengan atribut level, exp, health, attack power, dan armor.
    # Memiliki sistem level up berdasarkan exp yang dikumpulkan.
    #
    # Attributes:
    #   healthPool (list): Daftar nilai health berdasarkan level.
    #   attPower (list): Daftar nilai attack power berdasarkan level.
    #   armorPool (list): Daftar nilai armor berdasarkan level.
    #   __name (str): Nama hero.
    #   __exp (int): Experience yang dimiliki hero.
    #   __level (int): Level hero saat ini.
    #   __health (int): Health hero sesuai level.
    #   __power (int): Attack power hero sesuai level.
    #   __armor (int): Armor hero sesuai level.
    #
    # Methods:
    #   __init__(name):
    #       Inisialisasi objek Hero dengan nama dan atribut dasar.
    #
    #   info():
    #       Menampilkan informasi lengkap hero (nama, level, health, attack power, armor).
    #
    #   healthPool (property):
    #       Getter dan setter untuk pool health berdasarkan level.
    #
    #   attPower (property):
    #       Getter dan setter untuk pool attack power berdasarkan level.
    #
    #   armorPool (property):
    #       Getter dan setter untuk pool armor berdasarkan level.
    #
    #   level (property):
    #       Getter dan setter untuk level hero. Setter juga mengupdate health, power, dan armor sesuai level baru.
    #
    #   exp (property):
    #       Getter dan setter untuk exp hero. Setter akan menaikkan level jika exp mencapai kelipatan 100, dan menyimpan sisa exp.
    """
     # tamplate nama, hp, attackpower, defense
    def __init__(self,name,health,attpower,defense):
        self.__name = name
        self.__health = health
        self.__attpower = attpower
        self.__defense = defense
        self.__exp = 0
        self.__level = 0
        
    def info(self):
        print("{} \n\tLevel: {} \n\tHealth: {} \n\tattPower: {} \n\tarmor: {}".format(
            self.__name,
            self.__level,
            self.__health,
            self.attpower,
            self.defense
        ))
    @property
    def lawan(lawan):
        return lawan.__name
    @property
    def name(self):
        return self.__name
    @property
    def health(self):
        return self.__health
    @property
    def attpower(self):
        return self.__attpower
    @property
    def defense(self):
        return self.__defense
    @property
    def level(self):
        return self.__level
    @property
    def exp(self):
        return self.__exp
    
    @health.setter
    def healthPool(self,input):
        self.__health = input
        
    @attpower.setter
    def attpower(self,input):
        self.__attpower = input
        
    @defense.setter
    def armorPool(self,input):
        self.__defense = input
        
    @exp.setter    
    def exp(self, input): # Setter untuk exp (experience)
        self.__exp += input
        if(self.__exp >= 100):  # Setiap kali exp bertambah, dicek apakah exp sudah mencapai 100 atau lebih.
            self.level = self.__exp // 100  # Jika sudah, maka level akan dinaikkan sesuai jumlah kelipatan 100 pada exp.
            self.__exp %= 100 # Sisa exp setelah naik level akan disimpan (modulo 100).
    
    @property
    def upragre(self):
        self.__healthPool = [100,200,300,400,500]
        self.__attPower = [100,200,300,400,500]
        self.__armorPool = [100,200,300,400,500]
    @level.setter
    def level(self,input):
        self.__level += input
        self.__health = self.__health + self.__healthPool[self.__level]
        self.__attpower = self.__attpower + self.__attPower[self.__level]
        self.__defense = self.__defense + self.__armorPool[self.__level]
    
        
        
    def serang(self,lawan):
        self.gainExp = 5
        print(f"{self.__name} kamu mendapatkan {self.exp} exp ")
        print(f"{lawan.__name} kamu mendapatkan {lawan.exp} exp ")
        print(f"{self.__name} Menyerang dengan attack power {self.attpower} pada {lawan.name}\n")
        lawan.diserang(self, self.attpower) # memanggil fungsi bawah jika diserang
        
    def diserang(self,lawan, attackPower_lawan):
        
        print(f"{self.__name} diserang {lawan.name}")
        attackTrima = attackPower_lawan / self.defense
        print(f"{self.__name} terkena {str(attackTrima)} HP")
        self.health -= attackTrima
        print(f"darah {self.__name} tersisa {str(self.health)} HP\n")
         
class BestHero(Hero):
    def __init__(self, name):
        super().__init__(name, 100, 40, 20)
        self.healthPool = [100, 200, 250, 300, 350, 360, 500]
        self.attPower = [0, 40, 60, 70, 80, 120, 150]
        self.armorPool = [10, 20, 30, 40, 50, 60, 70]
        self.level = 1

class IntellegentHero(Hero):
    def __init__(self, name):
        super().__init__(name, 80, 30, 15)
        self.healthPool = [80, 160, 200, 240, 280, 320, 400]
        self.attPower = [0, 30, 50, 65, 75, 100, 130]
        self.armorPool = [0, 20, 40, 60, 70, 120, 150]
        self.level = 1


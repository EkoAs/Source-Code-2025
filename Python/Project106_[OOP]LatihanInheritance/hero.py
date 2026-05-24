# latian 
# menggunakan sub class yang kelakuannya beda beda
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
    def __init__(self,name):
        self.healthPool = [0,100,200,300,400,500]
        self.attPower = [0, 10,20,30,40,45,48,50]
        self.armorPool = [10,20,40,50,70,200]
        self.__name = name
        self.__exp = 0
        self.__level = 0
        
    def info(self):
        print("{} \n\tLevel: {} \n\tHealth: {} \n\tattPower: {} \n\tarmor: {}".format(
            self.__name,
            self.__level,
            self.__health,
            self.__power,
            self.__armor
        ))
        
    @property
    def healthPool(self):
        pass
       
    @property
    def attPower(self):
        pass
    
    @property
    def armorPool(self):
        pass
    
    @property
    def level(self):
        pass
    
    @property
    def exp(self):
        pass
    
    @healthPool.setter
    def healthPool(self,input):
        self.__healthPool = input
        
    @attPower.setter
    def attPower(self,input):
        self.__attPower = input
        
    @armorPool.setter
    def armorPool(self,input):
        self.__armorPool = input
        
    @exp.setter    
    def exp(self, input): # Setter untuk exp (experience)
        self.__exp += input
        if(self.__exp >= 100):  # Setiap kali exp bertambah, dicek apakah exp sudah mencapai 100 atau lebih.
            self.level = self.__exp // 100  # Jika sudah, maka level akan dinaikkan sesuai jumlah kelipatan 100 pada exp.
            self.__exp %= 100 # Sisa exp setelah naik level akan disimpan (modulo 100).
    
    @level.setter
    def level(self,input):
        self.__level += input
        self.__health = self.__healthPool[self.__level]
        self.__power = self.__attPower[self.__level]
        self.__armor = self.__armorPool[self.__level]
            
class BestHero(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.healthPool =[100,200,250,300,350,360,500]
        self.attPower = [0, 40, 60, 70, 80, 120]
        self.level = 1
        
        
class IntellegentHero(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.healthPool =[200,290,300,400,550,660,900]
        self.attPower = [0, 90, 160, 270, 380,600]
        self.armorPool = [0, 20, 40, 60, 70, 120]
        self.level = 1
        
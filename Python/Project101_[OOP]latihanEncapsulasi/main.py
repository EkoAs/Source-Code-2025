#  latihan encapsulasi
# sistem level dan expirence 
class Hero:
    __num = 0
    def __init__(self,name,health,attackpower,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attackpowerStd = attackpower
        self.__armorSts = armor
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attackpowerStd *  self.__level
        self.__armor = self.__armorSts *  self.__level
        
        self.__health = self.__healthMax
        Hero.__num += 1
        # bagian info
    @property
    def info(self):
        return "{} level {}:\n\t health = {}/{} \n\t attack = {} \n\t armor = {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)

    # bagian setter
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(f"{self.__name} Naik Level!")
            self.__level += 1
            self.__exp -= 100
            
            # mengulang dan memanggil yang maksimumnya
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attackpowerStd *  self.__level
            self.__armor = self.__armorSts *  self.__level

    def attack(self,musuh):
        self.gainExp = 50




hunter = Hero("hunger", 100, 5, 10)
ucup = Hero("bandit", 100, 5, 10)
print(ucup.info)
ucup.gainExp = 50
ucup.gainExp = 50
ucup.gainExp = 50
ucup.attack(hunter)
print(ucup.info)
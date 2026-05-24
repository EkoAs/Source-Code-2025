# getter, setter, deleter decorator
class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        
    # property variable
    @property
    def info(self):
        return "name {}:\n\t health {}:".format(self.name, self.__health)

    @property # wajib me return nya sebelum menggunakan getter setter dan deleter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        self.__armor += value
        
    @armor.getter
    def armor2(self):
        self.__armor
    @armor.deleter
    def armor(self):
        self.__armor = None

sniper = Hero("ucup", 200, 50)
print(sniper.info)
sniper.armor = 30
del sniper.armor
print("Armor:", sniper.armor)

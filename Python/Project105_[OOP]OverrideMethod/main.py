class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def infoHero(self):
        print(f"ovrride dari class Hero")
        print("{} \n\t health : {}".format(self.name,self.health))
               
class HeroBest(Hero):
    def __init__(self,name):
        super().__init__(name,100)
    
    def info(self):         # menimpa yang atas
        print(f"override dari class BestHero")
        print("{} \n\ttipe : Best hero, \n\t health:{}".format(self.name,self.health))
        
ucup = Hero("ucup", 100)
ucup.infoHero()  # Memanggil method infoHero dari class Hero

otong = HeroBest("otong")
otong.info()     # Memanggil method info yang sudah di-override di HeroBest
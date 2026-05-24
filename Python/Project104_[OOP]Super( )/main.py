class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
    def info(self):
        print("{} dengan Health: {}".format(self.name,self.health))
# sub class
class Hero_intelligent(Hero):
    def __init__(self,name):
       # Hero.__init__(self, name, 100) # untuk menghindari pengulangan
        super().__init__(name,100) # artinya kita ngambil init yang di super class, mengambil method init di super
        super().info() # memanggil info tanpa print
                      
                                #  setiap bikin hero intelegent, hp nya 100
                                # 
class Hero_spedd(Hero):
    def __init__(self,name):
        # Hero.__init__(self, name, 300)
        super().__init__(name,300) # artinya kita ngambil init yang di super class
        
luna = Hero_intelligent("luna")
ucup = Hero_spedd("ucup")
print(luna.name, " ", luna.health)
print(ucup.name, " ", ucup.health)
        
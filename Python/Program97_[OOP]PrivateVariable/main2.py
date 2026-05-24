# Private and protected variable
class Hero: 
    num = 0 # ini adalah class variable (public)
    def __init__(self,name,heatht):
        # self.name = name
        self.health = heatht
        self.__name = name # private variable
        # self._name = name # protected variable
    
    # cara akses yang private
    def get(self):
        self.__name
lina = Hero("Lina", 200)
print(lina.get._name())
lina.__name = "dain" # bisa meng akses tapi dengan data yang berbeda


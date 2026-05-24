class Hero:
    def __init__(self,name,hp):
        self.__name = name # menggunakan private 
        self.__hp = hp
        
    # pakai getter 
    def get_name(self):
        return self.__name
    def darah(self):
        return self.__hp
    
    # setter
    def diserang(self,serang):
        self.__hp -= serang
        
# awal dari gamenya
raja = Hero("raja mtk", 30)

# game berjalan
# raja.__name = "Anjir" # gak akan berubah
print(raja.get_name())
raja.diserang(8)
print(raja.darah())
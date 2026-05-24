class Hero:
    num = 0 # ini yg nempel dengan class variable
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
        # membuat variiable instace private
        # private nama variable (khusus c dan java)
        self.__private = "private"
        # variable instance protected
        self._protected = "prokontera"
        #  kalo pakai under score cuma bisa di dalam class, dan gakbisa dirubah cuma bisa di akses
         
    
    
    
lina = Hero("lina", 200)
print(lina.__dict__)
# print diatas yg mencangkup nama dan lainnya, termasuk public
print(lina.health)
# lina.private = "testign" malah bikin variable baru, yg hero tetep ada
# assigmend yg variablenya dikuar darri class .
# bisa nambahin variable dari luar class



# memiliki hubungan dengan multiple inheritance

class A:
    def show(self): # kalo methodnya sama, yg diambil pertama adalah yg awal
        print(f"Ini adalah A")
class B:
    def show(self):
        print(f"Ini adalah B")
    
class C(B,A):
    pass
    # def show(self):      # kalo ada mthodnya. maka yg dieksekusi yg c dulu
    #     print(f"Ini adalah C")
        # super().show()      # menampilkan c dan b atau
        # A.show(self) # akan mencetak c dan a

objek = C()

objek.show()
# help(objek) # menampilkan  urutan semua
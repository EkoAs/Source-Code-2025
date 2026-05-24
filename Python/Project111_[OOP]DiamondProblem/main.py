# masalah yg muncul ketika multiple inheritance # bentuknya seperti diamond
class A:
    def show(self):
        print(f"Ini adalah A")
        
class B(A):
    pass
    # def show(self):
    #     print(f"Ini adalah B")
    
class C(A):
    pass
    # def show(self):
    #     print(f"Ini adalah C")
        
class D(B,C):
    pass

objek = D()
objek.show() # jika b gada akan ke c, jika c gada akan ke a
# help(objek)
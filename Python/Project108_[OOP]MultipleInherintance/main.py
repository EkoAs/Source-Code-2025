# multiple inheritance
class A:
    def methodA(self):
        print(f"Ini class A")
class B:
    def methodB(self):
        print(f"Ini class B")
class C(A,B):
    pass


# ketika memanggil class c, maka akan mencari method di class A terlebih dahulu, jika tidak ada baru ke class B
c = C()
c.methodA()
c.methodB()

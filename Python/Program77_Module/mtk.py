def tambah(*args):
    num = 0
    for i in args:
        num += i
    return num   
        
def kurang(*args):
    num = 0
    for i in args:
        num -= i
    return num   
        
def kali(*args):
    num = 1
    for i in args:
        num *= i
    return num   
        
def pangkat(num:int):
    return lambda x:x ** num    
        
        
        
        
        
        
        
        
        
'''Module mtk'''
def tambah(*data):
    num = 0
    for i in data:
        num += i
    return num

def kurang(*data):
    num = 0
    for i in data:
        num -= i
    return num

def kali(x):
    num = 1
    return lambda num:num**x









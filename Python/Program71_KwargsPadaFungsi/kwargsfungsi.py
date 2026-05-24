# Kwargs pada fungsi
# selengkapnya baca di buku (p71)

def data(**kwargs):
    dataCop = kwargs.copy()
    dataCop['nama'] = 'Otong' # mengganti isi key 
    return dataCop
fulldata = data(nama='ucup', tanggal='29292')
print(fulldata)

'''Contoh 2'''
def hello(**nomor):
    dat = 0
    for i in nomor.values():
        dat += i
    return dat
dataNum = hello(a=1, s=2, c=3, h=4, d=5)
print(dataNum)


'''Fungsi gabungan'''
def gabungan(*args, **kwargs):
    for arg in args:
        print(arg)
    for kw in kwargs.items(): # item(), value(), key(). selengkapnya di P59 looping dict
        print(kw)

gabungan(1, 2, 3, 4, nama='cup', tinggal='Jakarta')
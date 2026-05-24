# magic method untuk pembuatan class
            #  keyword yg bisa di pakai
class Mangga:
    def __init__(self,nama,jumlah):       
        self.nama = nama
        self.jumlah = jumlah
    # contoh magic method pertama                                 
    # kelakukan init akan bekerja ketika di panggil
    # kalot print nama langsung akan keluar itunya
    def __repr__(self):
        # peit("ini repet")
        # atau
        return "arumanis jumlah:{}".format(self.jumlah)
        # dia ada urutannya
        # jika di panggil print(belanja) akan mencetak return di atas

    # def __str__(self): 
    #     pass
        #kelakuannya sama kayak repr
        # str untuk program sudah jadi, kalo yg reapry saat debug
        # caranya print(repr(mannga)
        
        # magic method pale underscore
    def __add__(self,objek):
        return self.jumlah + objek.jumlah
        
        # jadi bisa print(belanja1 + belanja2)
        # menjjumlahkan 2 buah objek

        # meng ovveridae
    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah"
        # kalo cetak print(belanja.__dict__) akan mencetak yg atas
        
# kalo di panggil 
belanja = Mangga("Arumanis", 2)
belanja2 = Mangga("Arumanis", 2)
print(belanja2) #maka akan mencetak mangga:arumanis dari fungsi repr dan str       
print(belanja.__dict__) # mencetak keteragan return dari fungsi __dict__
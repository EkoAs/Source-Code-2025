
class DataDasar:
    def __init__(value, data_awal):
        value._items = data_awal

class WarungBelanja(DataDasar):
    def __init__(value, data_awal):
        super().__init__(data_awal)

    @property
    def items(value):
        return value._items

    @items.setter
    def items(value, data_baru):
        value._items = data_baru

    def tampilkan_list(value):
        print(value.items,"\n")

    def tambah_barang(value):
        print("Masukkan 2 barang baru:")
        for i in range(2):
            barang = input(f"Barang {i+1}: ")
            value.items.append(barang)
# no 4
    def hitung_jumlah(value):
        return len(value.items)

    def tampilkan_jumlah(value):
        print(f"Jumlah barang : {value.hitung_jumlah()}\n")

    def tampilkan_loop(value):
        nomor = 1
        for barang in value.items:
            print(f"Barang ke-{nomor}: {barang}")
            nomor += 1

    def hapus_barang(value):
        target = input("Masukkan nama barang yang dihapus: ")
        if target in value.items:
            value.items.remove(target)
            print(f"{target} berhasil dihapus.\n")
        else:
            print("Barang tidak ditemukan.\n")


    def cek_barang(value):
        cari = input("Cek barang: ")
        if cari in value.items:
            print("Barang tersedia\n")
        else:
            print("Barang tidak tersedia\n")

if __name__=='__main__':
        
    data_belanja = ["beras", "gula", "minyak"]
    app = WarungBelanja(data_belanja)

    # no 1
    app.tampilkan_list()
    # no 2
    app.tambah_barang()
    # no3
    app.tampilkan_list()
    # no 4 and 5
    app.tampilkan_jumlah()
    # no 6
    app.tampilkan_loop()
    # no 7
    app.hapus_barang()
    # no 8
    app.tampilkan_list()
    # no 9
    app.cek_barang()
    
    
    
    
    

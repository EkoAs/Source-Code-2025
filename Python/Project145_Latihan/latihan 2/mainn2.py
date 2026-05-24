
# SOAL NO 2
class DataDasar:
    def __init__(value, data_awal):
        value._items = data_awal

class MonitoringPengunjung(DataDasar):
    def __init__(value, data_awal):
        super().__init__(data_awal)

    @property
    def items(value):
        return value._items

    @items.setter
    def items(value, data_baru):
        if all(isinstance(x, int) for x in data_baru):
            value._items = data_baru
        else:
            print("Error: Semua elemen harus berupa integer (jumlah pengunjung).")
# no 1
    def tampilkan_semua(value):
        print(value.items)
# no 2
    def hitung_hari(value):
        return len(value.items)

    def tampilkan_jumlah_hari(value):
        print(value.hitung_hari())
# no 3
    def hitung_total_pengunjung(value):
        return sum(value.items)

    def tampilkan_total_pengunjung(value):
        print(value.hitung_total_pengunjung())

    def hitung_rata_rata(value):
        total = value.hitung_total_pengunjung()
        hari = value.hitung_hari()
        if hari > 0:
            return total / hari
        return 0
# no 4
    def tampilkan_rata_rata(value):
        rata = value.hitung_rata_rata()
        print(f"{rata:.2f}")
# no 5
    def tampilkan_loop(value):
        nomor = 1
        for jumlah in value.items:
            print(f"Hari ke-{nomor}: {jumlah} pengunjung")
            nomor += 1
# no 6
    def tambah_pengunjung(value):
        try:
            jumlah_baru = int(input("Masukkan jumlah pengunjung hari baru: "))
            if jumlah_baru >= 0:
                value.items.append(jumlah_baru) # no 7
                print(f"Data {jumlah_baru} pengunjung berhasil ditambahkan.")
            else:
                print("Jumlah pengunjung harus non-negatif.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
# no 8
    def cari_terbanyak_tersedikit(value):
        if not value.items:
            print("Data pengunjung kosong.")
            return
        terbanyak = max(value.items)
        tersedikit = min(value.items)
        print(f"Terbanyak: {terbanyak}")
        print(f"Tersedikit: {tersedikit}")
# no 9
    def hapus_di_bawah_100(value):
        new_items = [p for p in value.items if p >= 100]
        jumlah_dihapus = len(value.items) - len(new_items)
        value.items = new_items

        print(f"{jumlah_dihapus} data pengunjung di bawah 100 telah dihapus.")


pengunjung_awal = [120, 150, 90, 200, 175]
monitor = MonitoringPengunjung(pengunjung_awal)

print("Menampilkan seluruh data jumlah pengunjung (Awal)")
monitor.tampilkan_semua()

print("\nMenampilkan jumlah hari yang tercatat")
monitor.tampilkan_jumlah_hari()

print("\nMenghitung total seluruh pengunjung")
monitor.tampilkan_total_pengunjung()

print("\nMenghitung rata-rata pengunjung per hari")
monitor.tampilkan_rata_rata()

print("\nMenampilkan data pengunjung menggunakan perulangan")
monitor.tampilkan_loop()

print("\nMenambahkan data jumlah pengunjung hari baru")
monitor.tambah_pengunjung()

print("\nTampilkan list setelah penambahan")
monitor.tampilkan_semua()

print("\nMenentukan jumlah pengunjung terbanyak dan tersedikit")
monitor.cari_terbanyak_tersedikit()

print("\nMenghapus data pengunjung di bawah 100 orang")
monitor.hapus_di_bawah_100()

print("\nTampilkan list setelah penghapusan")
monitor.tampilkan_semua()
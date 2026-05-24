class TugasDEF:
    def __init__(self, teks):
        self.teks = teks

    def tampilkan_huruf(self):
        print(f"Masukkan teks: {self.teks}")
        print(f"Huruf besar: {self.teks.upper()}")
        print(f"Huruf kecil: {self.teks.lower()}")
        print(f"Kapital awal: {self.teks.capitalize()}")
        print() 

    def balik_kapital(self):
        print(f"Masukkan teks: {self.teks}")
        hasil = self.teks.swapcase()
        print(f"Hasil: {hasil}")
        print()

    def ganti_kata(self, kata_lama, kata_baru):
        print(f"Masukkan kalimat: {self.teks}")
        print(f"Kata yang ingin diganti: {kata_lama}")
        print(f"Kata pengganti: {kata_baru}")
        kalimat_baru = self.teks.replace(kata_lama, kata_baru)
        print(f"Kalimat baru: {kalimat_baru}")


# ====== Bagian Utama Program ======


print(f"{'='*10} TUGAS D. E. F. {'='*10}")
print(f"\nTUGAS D.")
tp1 = TugasDEF("belajar python itu mudah")
tp1.tampilkan_huruf()

# Bagian e
print(f"\nTUGAS E.")
tp2 = TugasDEF("PyThOn")
tp2.balik_kapital()

print(f"\nTUGAS F.")
tp3 = TugasDEF("Saya suka Java")
tp3.ganti_kata("Java", "Python")

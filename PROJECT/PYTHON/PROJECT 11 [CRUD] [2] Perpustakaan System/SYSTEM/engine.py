import json
import os
from datetime import datetime

class LibraryEngine:
    def __init__(self, filename="data_buku.txt"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except:
            return []

    # ================================penulisan data buku ================================
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def tambah_peminjaman(self, nim, nama, judul, lama):
        
        id_pinjam = f"P{int(datetime.now().timestamp())}"[-4:] 
        
        entry = {
            "id": f"P{id_pinjam}",
            "nim": nim,
            "nama": nama,
            "judul": judul,
            "lama": int(lama)
        }
        self.data.append(entry)
        self.save_data()
        return True

    # ambil data berbasiss nim 
    def get_data_by_nim(self, nim):
        return [buku for buku in self.data if buku['nim'] == nim]

    # =========================== kalo terlanbat balikin============================================
    def hitung_denda(self, lama_pinjam):
        if lama_pinjam > 7:
            keterlambatan = lama_pinjam - 7
            return keterlambatan * 2000
        return 0

    # ===========================================kemBALKAN pinjaman / hapus data buku =============================
    def kembalikan_buku(self, id_pinjam):
       
        for i, buku in enumerate(self.data):
            if buku['id'] == id_pinjam:
                del self.data[i]
                self.save_data()
                return True
        return False
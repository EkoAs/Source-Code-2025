import json
import os
import random

class BarangManager:
    def __init__(self):
        # Path file untuk menyimpan data yang persisten
        self.file_path = os.path.join(os.path.dirname(__file__), 'database_stok.txt')
        
       
        self.data_awal = {
            "pakaian": [
                {
                    "id": 101, 
                    "nama": "Kaos Polos Oversize Cotton", 
                    "harga": 85000, "stok": 50, "rating": 4.8, "terjual": 120, 
                    "img": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=500", 
                    "diskon": 0
                },
                {
                    "id": 102, 
                    "nama": "Kemeja Flanel Premium", 
                    "harga": 185000, "stok": 25, "rating": 4.7, "terjual": 85, 
                    "img": "https://images.unsplash.com/photo-1589310243389-96a5483213a8?q=80&w=500", 
                    "diskon": 0
                },
                {
                    "id": 103, 
                    "nama": "Jaket Bomber Waterproof", 
                    "harga": 275000, "stok": 15, "rating": 4.9, "terjual": 45, 
                    "img": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?q=80&w=500", 
                    "diskon": 0
                },
                {
                    "id": 104, 
                    "nama": "Celana Chino Slim Fit", 
                    "harga": 150000, "stok": 40, "rating": 4.5, "terjual": 210, 
                    "img": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?q=80&w=500", 
                    "diskon": 0
                },
                {
                    "id": 105, 
                    "nama": "Hoodie Pullover Black", 
                    "harga": 210000, "stok": 20, "rating": 4.6, "terjual": 95, 
                    "img": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?q=80&w=500", 
                    "diskon": 0
                },
                {
                    "id": 106, 
                    "nama": "Rok Plisket A-Line", 
                    "harga": 95000, "stok": 35, "rating": 4.4, "terjual": 60, 
                    "img": "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?q=80&w=500", 
                    "diskon": 0
                },
                {
                    "id": 107, 
                    "nama": "T-Shirt Grafis Streetwear", 
                    "harga": 125000, "stok": 45, "rating": 4.7, "terjual": 150, 
                    "img": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?q=80&w=500", 
                    "diskon": 0
                },
                {
                    "id": 108, 
                    "nama": "Cardigan Rajut Wanita", 
                    "harga": 135000, "stok": 22, "rating": 4.8, "terjual": 40, 
                    "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=500", 
                    "diskon": 0
                }
            ]
        }
        
        self._inisialisasi_database()

    def _inisialisasi_database(self):
        """Membuat file database jika belum ada atau kosong."""
        if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
            self.simpan_semua_data(self.data_awal)

    def simpan_semua_data(self, data):
        """Menulis data dict ke file txt."""
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def baca_semua_data(self):
        """Membaca data dari file txt dan memberikan diskon random."""
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        
       
        for item in data['pakaian']:
            if random.random() < 0.3:
                item['diskon'] = random.randint(5, 50)
            else:
                item['diskon'] = 0
        return data

        """Mengurangi stok barang setelah pembelian berhasil."""
    def kurangi_stok(self, product_id, jumlah=1):
        data = self.baca_semua_data()
        for item in data['pakaian']:
            if item['id'] == product_id:
                if item['stok'] >= jumlah:
                    item['stok'] -= jumlah
                    item['terjual'] += jumlah
                    self.simpan_semua_data(data)
                    return True, "Berhasil"
                return False, "Stok Habis"
        return False, "Produk Tidak Ditemukan"

        """Mencari barang berdasarkan kemiripan nama."""
    def cari_barang(self, keyword):
        data = self.baca_semua_data()
        hasil = [p for p in data['pakaian'] if keyword.lower() in p['nama'].lower()]
        return hasil
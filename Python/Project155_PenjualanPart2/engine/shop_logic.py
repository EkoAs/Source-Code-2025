import json
import os

DB_FILE = 'database_stok.json'

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        try:
            return json.load(f)
        except:
            return []

def save_data(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def process_pembelian_satuan(cart):
    """
    Menerima list barang yang dibeli (cart)
    Format cart: [{"id": "CPU01", "qty": 1}, ...]
    """
    all_components = load_data()
    updated_items = []
    total_bayar = 0
    
    # Validasi stok dulu sebelum memproses semua
    for item_cart in cart:
        target_id = item_cart.get('id')
        qty_beli = item_cart.get('qty', 1)
        
        found = False
        for comp in all_components:
            if comp['id'] == target_id:
                found = True
                if comp['stok'] < qty_beli:
                    return {
                        "status": "error",
                        "message": f"Stok {comp['nama']} tidak mencukupi!"
                    }
                # Hitung sementara
                comp['stok'] -= qty_beli
                total_bayar += comp['harga'] * qty_beli
                updated_items.append(comp)
                break
        
        if not found:
            return {
                "status": "error",
                "message": f"Barang ID {target_id} tidak ditemukan!"
            }

    # Jika semua stok aman, simpan ke database
    save_data(all_components)
    
    return {
        "status": "success",
        "message": "Pembelian berhasil diproses!",
        "total_pembayaran": total_bayar,
        "detail_pembelian": updated_items
    }
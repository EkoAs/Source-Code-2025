import json
import random
import os

DB_FILE = 'database_stok.json'

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def generate_smart_build(budget):
    all_components = load_data()
    
    # Persentase alokasi budget ideal untuk PC Desktop
    allocation = {
        "CPU": 0.20,
        "Motherboard": 0.12,
        "VGA": 0.35,
        "RAM": 0.08,
        "SSD": 0.07,
        "PSU": 0.07,
        "Casing": 0.05,
        "Kipas CPU": 0.06
    }

    selected_build = []
    total_harga_build = 0
    score_performa = 0 # Untuk hitung FPS nanti

    # Ambil satu barang terbaik per kategori yang masuk budget alokasi
    categories = ["CPU", "Motherboard", "VGA", "RAM", "SSD", "PSU", "Casing", "Kipas CPU"]
    
    for cat in categories:
        target_price = budget * allocation[cat]
        # Filter barang berdasarkan kategori
        items = [i for i in all_components if i['kategori'] == cat]
        
        # Logika Diskon Random (10-30% diskon untuk barang tertentu secara acak)
        for item in items:
            if random.random() < 0.3: # 30% peluang dapat diskon
                potongan = random.randint(5, 20) / 100
                item['harga_display'] = int(item['harga'] * (1 - potongan))
                item['is_discount'] = True
            else:
                item['harga_display'] = item['harga']
                item['is_discount'] = False

        # Cari yang paling mendekati target budget tapi tidak melebihi
        eligible_items = [i for i in items if i['harga_display'] <= target_price + (budget * 0.05)]
        
        if not eligible_items:
            # Jika tidak ada yang masuk budget, ambil yang paling murah di kategori itu
            eligible_items = sorted(items, key=lambda x: x['harga_display'])
        
        if eligible_items:
            best_pick = sorted(eligible_items, key=lambda x: x['harga_display'])[-1]
            selected_build.append(best_pick)
            total_harga_build += best_pick['harga_display']
            
            # Hitung skor performa sederhana (berdasarkan harga VGA & CPU)
            if cat in ["CPU", "VGA"]:
                score_performa += best_pick['harga']

    # Cek apakah total melebihi budget
    if total_harga_build > budget + (budget * 0.1): # Toleransi 10%
        return {
            "status": "error",
            "message": "Dana Gak Cukup! Coba naikkan budget atau ganti spek."
        }

    # Logika Estimasi Performa GTA V
    fps_estimate = int(score_performa / 150000) # Formula simulasi
    if fps_estimate < 30: kesimpulan = "Office Work & Browsing"
    elif fps_estimate < 60: kesimpulan = "Casual Gaming (GTA V Low-Med)"
    else: kesimpulan = "High-End Gaming (GTA V Ultra Fluid)"

    return {
        "status": "success",
        "items": selected_build,
        "total": total_harga_build,
        "performance": {
            "gtav_fps": f"{fps_estimate} - {fps_estimate + 20} FPS",
            "summary": kesimpulan
        }
    }
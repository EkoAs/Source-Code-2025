from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

# Import logika dari folder engine
from engine.shop_logic import process_pembelian_satuan
from engine.build_logic import generate_smart_build

app = Flask(__name__)
CORS(app) # Agar bisa diakses oleh PHP (XAMPP)

DB_FILE = 'database_stok.json'

# Fungsi Helper untuk baca data
def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        return json.load(f)

# 1. API UNTUK KATALOG (Tampilan Satuan)
@app.route('/api/components', methods=['GET'])
def get_components():
    data = load_data()
    return jsonify(data)

# 2. API UNTUK RAKIT PC (Smart Recommendation)
@app.route('/api/recommend', methods=['POST'])
def recommend():
    req_data = request.get_json()
    budget = float(req_data.get('budget', 0))
    
    # Panggil fungsi dari build_logic.py
    hasil = generate_smart_build(budget)
    return jsonify(hasil)

# 3. API UNTUK CHECKOUT/PEMBAYARAN
@app.route('/api/checkout', methods=['POST'])
def checkout():
    req_data = request.get_json()
    cart = req_data.get('cart', [])
    
    # Panggil fungsi dari shop_logic.py
    status = process_pembelian_satuan(cart)
    return jsonify(status)

if __name__ == '__main__':
    if not os.path.exists(DB_FILE):
        print("Peringatan: database_stok.json belum ada!")
        
    print("NEURO TECH SUPPLY Engine - Running...")
    app.run(debug=True, port=5000)
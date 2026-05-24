from flask import Blueprint, jsonify, request
from engine.barang import DatabaseStok

home_bp = Blueprint('home', __name__)
db = DatabaseStok()

@home_bp.route('/api/produk')
def get_produk_api():
    query = request.args.get('search', '').lower()
    data = db.baca_semua_data()
    produk_list = data['pakaian']

    # Logika Pencarian (Search)
    if query:
        produk_list = [p for p in produk_list if query in p['nama'].lower()]

    return jsonify(produk_list)
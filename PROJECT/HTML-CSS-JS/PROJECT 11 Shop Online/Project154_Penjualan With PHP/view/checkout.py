from flask import Blueprint, render_template, request, session, redirect, url_for
from engine.barang import BarangManager
import random

checkout_bp = Blueprint('checkout', __name__)
db = BarangManager()

@checkout_bp.route('/')
def display_checkout():
    if 'cart' not in session or not session['cart']:
        return "Keranjang kosong, Asif. Silakan belanja dulu."

    data_barang = db.baca_semua_data()['pakaian']
    keranjang_user = []
    subtotal = 0

    # Ambil detail barang berdasarkan ID di session
    for item_id in session['cart']:
        for p in data_barang:
            if p['id'] == item_id:
                # Hitung harga setelah diskon jika ada
                harga_final = p['harga'] - (p['harga'] * p['diskon'] // 100)
                keranjang_user.append({
                    'nama': p['nama'],
                    'harga_asli': p['harga'],
                    'diskon': p['diskon'],
                    'harga_final': harga_final
                })
                subtotal += harga_final

    ongkir = random.randint(10000, 50000)
    pajak = int(subtotal * 0.11) # PPN 11%
    total_akhir = subtotal + ongkir + pajak

    # Simpam info transaksi sementara di session untuk strukkk
    session['last_transaction'] = {
        'daftar_barang': keranjang_user,
        'subtotal': subtotal,
        'ongkir': ongkir,
        'pajak': pajak,
        'total': total_akhir
    }

    return render_template('checkout.html', data=session['last_transaction'])

@checkout_bp.route('/bayar', methods=['POST'])
def proses_bayar():
    metode = request.form.get('metode')
    
  
    for item_id in session['cart']:
        db.kurangi_stok(item_id)

   
    session['cart'] = []
    
    # Generate kode bayar jika bukan COD
    kode_bayar = f"PAY-{random.randint(100000, 999999)}" if metode != 'cod' else "COD-CASH"
    
    return redirect(url_for('receipt.show_receipt', metode=metode, kode=kode_bayar))
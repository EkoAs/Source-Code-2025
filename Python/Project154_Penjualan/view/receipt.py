from flask import Blueprint, render_template, request, session, redirect, url_for
from datetime import datetime

receipt_bp = Blueprint('receipt', __name__)

@receipt_bp.route('/print')
def show_receipt():
    # get data transaksi terakhir dari session
    transaksi = session.get('last_transaction')
    
#    kalo masuk ke halaman struk tapi daftar ksomsong
    if not transaksi:
        return redirect(url_for('home.index'))

    metode = request.args.get('metode', 'Tidak Diketahui')
    kode = request.args.get('kode', '-')
    
   
    # %A=Hari, %d=Tgl, %B=Bulan, %Y=Tahun
    waktu_sekarang = datetime.now()
    format_waktu = waktu_sekarang.strftime("%A, %d %b %Y %H:%M:%S")

    return render_template('receipt.html', 
                           t=transaksi, 
                           metode=metode.upper(), 
                           kode=kode, 
                           waktu=format_waktu)
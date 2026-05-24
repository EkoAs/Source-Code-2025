from flask import Blueprint, render_template, request, session, redirect, url_for
from engine.barang import BarangManager

home_bp = Blueprint('home', __name__)
db = BarangManager()

@home_bp.route('/')
def index():
    query = request.args.get('search')
    if query:
       
        produk_list = db.cari_barang(query)
    else:
        
        data = db.baca_semua_data()
        produk_list = data['pakaian']
    
    return render_template('index.html', produk=produk_list)

@home_bp.route('/add_to_cart/<int:id>')
def add_to_cart(id):
   
    if 'cart' not in session:
        session['cart'] = []
    
    session['cart'].append(id)
    session.modified = True
    return redirect(url_for('home.index'))
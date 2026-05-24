from flask import Flask, render_template, request, redirect, url_for
import os
import time
import random
import string

app = Flask(__name__)
DB_NAME = "data.txt"

# --- KUMPULAN FUNGSI BANTUAN (PENGGANTI UTIL & OPERASI) ---

def buat_pk_random(panjang):
    # Membuat kode acak misal: aX7zQb
    return ''.join(random.choice(string.ascii_letters) for i in range(panjang))

def baca_database():
    # Membaca file txt dan mengubahnya jadi list of dictionary
    buku_list = []
    if not os.path.exists(DB_NAME):
        return []

    with open(DB_NAME, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                # Pecah data berdasarkan koma
                data = line.strip().split(',')
                if len(data) >= 5:
                    buku_list.append({
                        'pk': data[0],
                        'date_add': data[1],
                        'penulis': data[2].strip(), # strip() biar spasi berlebih hilang
                        'judul': data[3].strip(),
                        'tahun': data[4]
                    })
            except:
                continue
    return buku_list

def simpan_ke_file(buku_list):
    # Menulis ulang seluruh data ke file data.txt
    with open(DB_NAME, 'w', encoding='utf-8') as file:
        for buku in buku_list:
            # Kita bikin formatnya rapi lagi: pk,date,penulis,judul,tahun
            # Kita tidak pakai padding 255 spasi biar file txt nya hemat tempat
            line = f"{buku['pk']},{buku['date_add']},{buku['penulis']},{buku['judul']},{buku['tahun']}\n"
            file.write(line)

# --- BAGIAN ROUTING FLASK (PENGGANTI MENU TERMINAL) ---

# 1. MENU UTAMA (READ)
@app.route('/')
def index():
    data_buku = baca_database()
    return render_template('index.html', data=data_buku)

# 2. TAMBAH BUKU (CREATE)
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        # Ambil data dari Form HTML
        judul = request.form['judul']
        penulis = request.form['penulis']
        tahun = request.form['tahun']
        
        # Buat Data Baru
        buku_baru = {
            'pk': buat_pk_random(6),
            'date_add': time.strftime("%Y-%m-%d", time.gmtime()),
            'penulis': penulis,
            'judul': judul,
            'tahun': tahun
        }
        
        # Baca data lama, tambah data baru, simpan ulang
        data_lama = baca_database()
        data_lama.append(buku_baru)
        simpan_ke_file(data_lama)
        
        return redirect(url_for('index')) # Balik ke menu utama
    
    return render_template('form.html', mode="tambah")

# 3. EDIT BUKU (UPDATE)
@app.route('/edit/<pk>', methods=['GET', 'POST'])
def edit(pk):
    data_buku = baca_database()
    # Cari buku mana yang mau diedit
    buku_dipilih = None
    for buku in data_buku:
        if buku['pk'] == pk:
            buku_dipilih = buku
            break
            
    if request.method == 'POST':
        # Update datanya
        buku_dipilih['judul'] = request.form['judul']
        buku_dipilih['penulis'] = request.form['penulis']
        buku_dipilih['tahun'] = request.form['tahun']
        
        # Simpan ulang semuanya
        simpan_ke_file(data_buku)
        return redirect(url_for('index'))

    return render_template('form.html', mode="edit", data=buku_dipilih)

# 4. HAPUS BUKU (DELETE)
@app.route('/hapus/<pk>')
def hapus(pk):
    data_buku = baca_database()
    # Ambil semua buku KECUALI yang pk-nya mau dihapus
    data_baru = [buku for buku in data_buku if buku['pk'] != pk]
    
    simpan_ke_file(data_baru)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
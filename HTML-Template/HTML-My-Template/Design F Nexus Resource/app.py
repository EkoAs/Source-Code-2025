from flask import Flask, render_template, request, redirect, url_for
import os
import json # Tambahan modul JSON
from werkzeug.utils import secure_filename
from flask import send_from_directory

app = Flask(__name__)

# Konfigurasi
UPLOAD_FOLDER = 'uploads'
DB_FILE = 'database.json' # Lokasi file database
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- FUNGSI BANTUAN DATABASE ---

def load_data():
    """Membaca data dari file JSON"""
    if not os.path.exists(DB_FILE):
        return [] # Kalau file gak ada, kembalikan list kosong
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_data(new_item):
    """Menambah data baru dan menyimpan ke JSON"""
    current_data = load_data() # Ambil data lama
    current_data.insert(0, new_item) # Masukkan data baru ke paling atas
    
    with open(DB_FILE, 'w') as f:
        json.dump(current_data, f, indent=4) # Tulis ulang file JSON

# --- ROUTE ---

@app.route('/')
def index():
    # Baca data dari file JSON, bukan list manual lagi
    items = load_data()
    return render_template('index.html', items=items)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    # Ambil data form
    title = request.form.get('title', 'Untitled')
    category = request.form.get('category', 'project')
    tech = request.form.get('tech', '')
    desc = request.form.get('desc', '')

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        # 1. Simpan Fisik File
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # 2. Hitung Ukuran
        file_size = os.path.getsize(file_path)
        if file_size > 1024 * 1024:
            size_str = f"{round(file_size / (1024 * 1024), 1)} MB"
        else:
            size_str = f"{round(file_size / 1024, 1)} KB"

        # 3. Buat Dictionary Data Baru
        new_entry = {
            "title": title,
            "category": category,
            "tech": tech,
            "desc": desc,
            "file": filename,
            "size": size_str
        }

        # 4. Simpan PERMANEN ke JSON
        save_data(new_entry)

        return redirect(url_for('index'))


# --- ROUTE UNTUK DOWNLOAD FILE ---
@app.route('/uploads/<filename>')
def download_file(filename):
    # Fungsi ini akan mencari file di folder 'uploads' dan mengirimnya ke user
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
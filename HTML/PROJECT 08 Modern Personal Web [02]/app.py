from flask import Flask, render_template

# --- KONFIGURASI KHUSUS STRUKTUR KAMU ---
# 1. template_folder='templates' -> HTML diambil dari folder templates (standar)
# 2. static_folder='templates'   -> INI KUNCINYA. Kita suruh Flask cari gambar/css di dalam folder 'templates' juga.
# 3. static_url_path=''          -> Biar link di HTML (misal: href="assets/css/style.css") bisa langsung jalan.

app = Flask(__name__, 
            template_folder='templates', 
            static_folder='templates', 
            static_url_path='')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
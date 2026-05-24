from flask import Flask,render_template, jsonify
app = Flask(__name__)
# folder harus bernama 'templates' standar flask
# kalo mau ubah harus
# Tambahkan template_folder='nama foldernya'
# app = Flask(__name__, template_folder='data')

# panggil halaman utama
@app.route('/')
def hataman_depan():
    return render_template('main.html')

@app.route('/hitung') #bagian hitung
def hinungin():
    a = 2
    b = 5
    c = a * b
    # Bungkus hasil jadi paket JSON biar bisa dikirim
    return jsonify({"Isi_disinu": c})

if __name__=='__main__':
    app.run(debug=True)


from flask import Flask, render_template, jsonify
import random as rd

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/soal')
def soal():
    # a dan b pilih angka random 1-10
    a = rd.randint(1,10)
    b = rd.randint(1,10)
    op = ['+','-']
    simbol = rd.choice(op)
    # simbol membilih random didalam data list []
    
    # rakit soal nya pakai format string 'f'
    teks_soal = f"{a} {simbol} {b}"
    
    kunci_jawaban = eval(teks_soal)
    
    
    # kirim jawaban ke js 
    return jsonify({
        "soal":teks_soal, # bagian yg diliat user
        "jawab": kunci_jawaban # jawaban yg disimpan di js (perbandingan nanti)
    })
    
if __name__=='__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from full_engine.math_engine import MathEngine # Import dari folder full_engine

app = Flask(__name__)
engine = MathEngine()

# ==============================================================================
#                               ROUTE: HALAMAN UTAMA
# ==============================================================================
@app.route('/')
def index():
    return render_template('index.html')

# ==============================================================================
#                               ROUTE: API REQUEST SOAL
#  Menerima 'mode' dari JS -> Minta Engine Masak -> Kirim JSON ke JS
# ==============================================================================
@app.route('/get_question', methods=['POST'])
def get_question():
    data = request.json
    mode = data.get('mode', 'perkalian')
    
    # Panggil Engine
    paket_soal = engine.generate_question(mode)
    
    return jsonify(paket_soal)

if __name__ == '__main__':
    app.run(debug=True)
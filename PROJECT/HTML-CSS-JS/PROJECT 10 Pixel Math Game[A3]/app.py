from flask import Flask, render_template, jsonify, request
from ENGINE.RUMUS import perkalian, penambahan, pengurangan, campuran, pembagian
from ENGINE.SUPPORT import rank_manager

app = Flask(__name__)

# ==============================================================================
# ROUTE: TAMPILAN (VIEW)
# ==============================================================================
@app.route('/')
def menu():
    # Baca Top Rank dari file txt lewat Manager
    top_rank = rank_manager.get_top_rank()
    return render_template('menu.html', highscore=top_rank)

@app.route('/play/<mode>')
def play(mode):
    # ======================= /play/perkalian -> templates/modes/perkalian.html
    return render_template(f'modes/{mode}.html', mode=mode)

# ==============================================================================
@app.route('/api/get_soal', methods=['POST'])
def api_get_soal():
    data = request.json
    mode = data.get('mode')
    
    # Switch Case ke Engine Rumus yang sesuai
    if mode == 'perkalian':
        result = perkalian.generate()
    elif mode == 'penambahan':
        result = penambahan.generate()
    elif mode == 'pengurangan':
        result = pengurangan.generate()
    elif mode == 'pembagian':
        result = pembagian.generate()
    else:
        result = campuran.generate()
        
    return jsonify(result)

@app.route('/api/save_score', methods=['POST'])
def api_save_score():
    data = request.json
    nama = data.get('nama')
    score = data.get('score')
    

    rank_manager.save_score(nama, score)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
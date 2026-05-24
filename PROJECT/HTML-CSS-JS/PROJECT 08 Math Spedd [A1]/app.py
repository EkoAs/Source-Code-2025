from flask import Flask, render_template, request, jsonify
from Engine import MathEngine

app = Flask(__name__)
engine = MathEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_question', methods=['POST'])
def get_question():
    data = request.json
    mode = data.get('mode', 'perkalian')
    
    # Panggil class MathEngine
    question_data = engine.generate_question(mode)
    
    return jsonify(question_data)

if __name__ == '__main__':
    app.run(debug=True)
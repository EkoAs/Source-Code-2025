from flask import Flask, render_template
import os

from view.home import home_bp
from view.checkout import checkout_bp
from view.receipt import receipt_bp

def create_app():
    app = Flask(__name__, 
                static_folder='static', 
                template_folder='templates')
    
    app.secret_key = 'kunci_rahasia_asif_123'

    #Registrasi B
    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(checkout_bp, url_prefix='/checkout')
    app.register_blueprint(receipt_bp, url_prefix='/receipt')

    # pemnangana error
    @app.errorhandler(404)
    def page_not_found(e):
        return "Halaman tidak ditemukan. Silakan kembali ke menu utama.", 404

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
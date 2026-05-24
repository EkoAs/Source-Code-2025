from flask import Flask
from flask_cors import CORS
from view.home import home_bp

def create_app():
    app = Flask(__name__)
    
   
    app.config['SECRET_KEY'] = 'dev_store_99_x_secure_token_2025'

    # Izinkan PHP (XAMPP) mengakses data dari Python
    CORS(app)

    # Register Blueprint
    app.register_blueprint(home_bp, url_prefix='/')

    return app

if __name__ == '__main__':
    app = create_app()
    
    app.run(debug=True, port=5000)
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import logging
import json_log_formatter

# Configuración de la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'flaskdb')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos
db = SQLAlchemy(app)

# Configuración de logging en formato JSON
formatter = json_log_formatter.JSONFormatter()
json_handler = logging.StreamHandler()
json_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

# Modelo de la base de datos
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Endpoint para obtener todos los ítems
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

# Endpoint para crear un nuevo ítem
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id, 'name': new_item.name}), 201

# Inicialización de la base de datos
def init_db():
    with app.app_context():  # Asegura que tienes un contexto de la aplicación
        db.create_all()

# Ejecutar la inicialización de la base de datos al inicio de la aplicación
init_db()

# Ejecución de la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


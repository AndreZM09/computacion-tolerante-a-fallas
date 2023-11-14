# auth_service.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/authenticate/<username>/<password>')
def authenticate(username, password):
    # Lógica de autenticación (puede ser muy básica en este ejemplo)
    if username == 'usuario' and password == 'contrasena':
        return jsonify({'message': 'Autenticación exitosa'})
    else:
        return jsonify({'message': 'Autenticación fallida'})

if __name__ == '__main__':
    app.run(port=5001)

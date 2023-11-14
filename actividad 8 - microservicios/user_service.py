# user_service.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/user/<username>')
def get_user_profile(username):
    # Lógica para obtener el perfil del usuario desde la base de datos (simulado)
    user_data = {'username': username, 'email': f'{username}@example.com'}
    return jsonify(user_data)

if __name__ == '__main__':
    app.run(port=5002)

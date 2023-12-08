from clases import Usuario, Mensaje
from BD import BD
from datetime import datetime
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/mensajeria/contactos')
def contactos():
    mialias = request.args.get('mialias')
    usuario = next((u for u in BD if u.alias == mialias), None)
    if usuario:
        return {contacto: next((u.nombre for u in BD if u.alias == contacto), None) for contacto in usuario.contactos}
    else:
        return "Usuario no encontrado", 404

@app.route('/mensajeria/enviar', methods=['POST'])
def enviar():
    mialias = request.args.get('mialias')
    aliasdestino = request.args.get('aliasdestino')
    texto = request.args.get('texto')
    usuario = next((u for u in BD if u.alias == mialias), None)
    if usuario and aliasdestino in usuario.contactos:
        mensaje = Mensaje(aliasdestino, datetime.now(), texto)
        usuario.mensajes.append(mensaje)
        return "Realizado en {}.".format(mensaje.fecha.strftime("%d/%m/%Y"))
    else:
        return "Usuario no encontrado o contacto no válido", 404

@app.route('/mensajeria/recibidos')
def recibidos():
    mialias = request.args.get('mialias')
    usuario = next((u for u in BD if u.alias == mialias), None)
    if usuario:
        return [f"{m.alias_destino} te escribió: \"{m.texto}\" el {m.fecha.strftime('%d/%m/%Y')}" for m in usuario.mensajes]
    else:
        return "Usuario no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
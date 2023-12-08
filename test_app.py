import unittest
from flask import json
from app import app
from BD import BD
from clases import Usuario, Mensaje
from datetime import datetime

#En total son 6 test. 3 exitosos y 3 de fallo

#Hacemos 2 test por cada funcion del app, 1 donde el resultado es correcto y otro donde esperammos un error

class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

        #Esperamos que el app retorne correctamente los contactos del usuario de esta en la BD de ejemplo
    def test_contactos_exitoso(self):
        response = self.app.get('/mensajeria/contactos?mialias=cpaz')
        self.assertEqual(response.status_code, 200)
        #Esperamos que el app retorne un error al pedir un usuario que no esta en la BD de ejemplo
    def test_contactos_error(self):
        response = self.app.get('/mensajeria/contactos?mialias=alias_inexistente')
        self.assertEqual(response.status_code, 404)

        #Esperamos que el app envie correctamente el mensaje usando el endpoint
    def test_enviar_exitoso(self):
        response = self.app.post('/mensajeria/enviar?mialias=cpaz&aliasdestino=lmunoz&texto=hola')
        self.assertEqual(response.status_code, 200)

        #Esperamos que el app falle al enviar el mensaje usando un url erroneo
    def test_enviar_error(self):
        response = self.app.post('/mensajeria/enviar?mialias=alias_inexistente&aliasdestino=lmunoz&texto=hola')
        self.assertEqual(response.status_code, 404)

        #Esperamos que el app retorne correctamente el mensaje recibido
    def test_recibidos_exitoso(self):
        BD[0].mensajes.append(Mensaje("lmunoz", datetime.now(), "hola"))
        response = self.app.get('/mensajeria/recibidos?mialias=cpaz')
        self.assertEqual(response.status_code, 200)
        
        #Esperamos que el app falle al usando un url erroneo 
    def test_recibidos_error(self):
        response = self.app.get('/mensajeria/recibidos?mialias=alias_inexistente')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
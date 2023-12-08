class Usuario:
    def __init__(self, alias, nombre, contactos):
        self.alias = alias
        self.nombre = nombre
        self.contactos = contactos
        self.mensajes = []

class Mensaje:
    def __init__(self, alias_destino, fecha, texto):
        self.alias_destino = alias_destino
        self.fecha = fecha
        self.texto = texto
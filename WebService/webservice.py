__author__ = "G2"
__date__ = "$Ago 9, 2016 11:41:07 PM$"

from flask import Flask, session, request, render_template, jsonify, Response

app = Flask("AYD_PROYECTO")
#-----------------------------------------------CLASES QUE NO SON ESTRUCTURAS EMPIEZA
        
class Usuario():
    def __init__(self, password, correo, nombre):
        self.nombre = nombre
        self.password = password
        self.correo = correo
            
class UsuarioDrop():
    def __init__(self, password, correo):
        self.password = password
        self.correo = correo
        self.verificado = False
        self.root = ArbolB(None, None)
        self.archivosRoot = AVL()
#-----------------------------------------------CLASES QUE NO SON ESTRUCTURAS TERMINA
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
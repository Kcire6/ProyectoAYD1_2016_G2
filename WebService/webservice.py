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

class nodoListaB():
    
    def __init__(self, comparable):
        self.sig = None
        self.ant = None
        self.comparable = comparable
        
    def setAnt(self, an):
        self.ant = an
        
    def setSig(self, si):
        self.sig = si
        
    def getAnt(self):
        return self.ant
    
    def getSig(self):
        return self.sig    
    
class listaB():
    
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def insertar(self, comparable):
        if self.first == None:
            self.first = self.last = nodoListaB(comparable)
            self.len = self.len + 1;
        else:
            aux = self.last
            self.last = nodoListaB(comparable)
            self.last.setAnt(aux)
            aux.setSig(self.last)
            self.len = self.len + 1;
    
    def graphviz(self):
        self.codigo2 = None
        self.codigo2 = " "
        aux = self.first
        while (aux != None):
            if aux.sig != None:
                self.codigo2 = str(self.codigo2) + str(Relacion(aux.comparable, aux.sig.comparable).data)
                self.codigo2 = str(self.codigo2) + str(Relacion(aux.sig.comparable, aux.comparable).data)
            elif aux == self.first:
                self.codigo2 = Nodo(aux.comparable).data
            aux = aux.sig
        codigoTotal = str(self.codigo2)
        return codigoTotal
    
    def getAll(self):
        y = ""
        aux = self.first
        while (aux != None):
            y = str(y) + ",,," + str(aux.comparable)
            aux = aux.sig
        return y
            
    def buscar(self, comparable):
        aux = self.first
        while aux != None:
            if str(aux.comparable) == str(comparable):
                return aux
            else:
                aux = aux.sig
        return None
    
    def buscarIndex(self, dato):
        try:
            aux = self.first
            for x in range(0,1000):
                if str(aux.comparable) == str(dato):
                    return int(int(x)+1)
                else:
                    if aux.sig != None:
                        aux = aux.sig                   
        except:
            return -1
    
    def buscarConIndex(self, inde):
        index = -1
        index = int(inde)
        if index != -1:
            aux = self.first
            for x in range(0, (index - 1)):
                if aux != None:
                    aux = aux.getSig()
                else:
                    return None
            return aux
    
    def eliminar(self, inde):
        index = int(inde)
        if index != -1:
            aux = self.first
            for x in range(0, (index - 1)):
                aux = aux.getSig()
            if aux == self.first:
                self.first = aux.getSig()
                if self.first != None:
                    self.first.setAnt(None)
                else:
                    self.last = None
                self.len = self.len - 1;
            elif aux == self.last:
                self.last = aux.getAnt()
                self.last.setSig(None)
                self.len = self.len - 1;
            else:
                aux.getAnt().setSig(aux.getSig())
                aux.getSig().setAnt(aux.getAnt())
                self.len = self.len - 1;

    def getLast(self):
        return self.last
        
		
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
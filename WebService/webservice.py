__author__ = "Mac"
__date__ = "$Apr 9, 2015 11:41:07 PM$"

from flask import Flask, session, request, render_template, jsonify, Response

app = Flask("EDD_codigo_ejemplo_proyecto1")


#-----------------------------------------------GRAPHVIZ

class Nodo():
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.data = str(nombre) + str("[label = \"") + str(nombre) + "\"" + " ] \n"    
    
class Relacion():
    
    def __init__(self, nodo1, nodo2):
        self.data = "\"" + nodo1 + "\"" + " -> " + "\"" + nodo2 + "\"" + "\n"
        
#-----------------------------------------------GRAPHVIZ
        
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
        
#-----------------------------------------------LISTA SIMPLE EMPIEZA
class nodoListaSimple():

    def __init__(self, val, comparable):
        self.sig = None
        self.valor = valor
        self.comparable = comparable

class listaSimple():

    def __init__(self):
        self.first = None
        self.last = None

    def insertar(self, comparable, valor):
        if self.first == None:
            self.first = self.last = nodoListaSimple(valor, comparable)
        else:
            self.last = self.last.sig = nodoListaSimple(valor, comparable)

    def buscar(self, comparable):
        aux = self.first
        while(aux != None):
            if aux.comparable == comparable:
                return aux
            else:
                aux = aux.sig
        return None

    def eliminar(self, comparable):
        target = self.first
        targetAnt = None
        encontrado == False
        while(encontrado != True):
            if aux.comparable == comparable:
                encontrado = True
            else:
                targetAnt = target
                target = target.sig
        return None

        if target == self.first:
            if target.sig == None:
                self.first = self.last = None
            else:
                self.first = target.sig
        else:
            if target.sig == None:
                self.last = targetAnt
            else:
                targetAnt.sig = target.sig

    def toDot(self):
        self.codigo2 = None
        self.codigo2 = " "
        aux = self.first
        while (aux != None):
            if aux.sig != None:
                self.codigo2 = str(self.codigo2) + str(Relacion(aux.comparable, aux.sig.comparable).data)
            elif aux == self.first:
                self.codigo2 = Nodo(aux.comparable).data
            aux = aux.sig
        codigoTotal = str(self.codigo2)
        return codigoTotal

#-----------------------------------------------LISTA DOBLEMENTE ENLAZADA EMPIEZA
        
class nodoLista():
    
    def __init__(self, val, comparable):
        self.sig = None
        self.ant = None
        self.valor = val
        self.comparable = comparable
        self.senders = ABB()
        
    def setAnt(self, an):
        self.ant = an
        
    def setSig(self, si):
        self.sig = si
        
    def getAnt(self):
        return self.ant
    
    def getSig(self):
        return self.sig    
    
class lista():
    
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def insertar(self, valor, comparable):
        if self.first == None:
            self.first = self.last = nodoLista(valor, comparable)
            self.len = self.len + 1;
        else:
            aux = self.last
            self.last = nodoLista(valor, comparable)
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
                self.codigo2 = "\"" + str(aux.comparable) + "\""
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
                aux = aux.getSig()
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
        

#-----------------------------------------------LISTA DOBLEMENTE ENLAZADA TERMINA

#-----------------------------------------------MATRIZ DISPERSA EMPIEZA

class nodoContenido():


    def __init__(self, data, col, fila, adentro, afuera, izq, der, up, down, comparable):
        self.data = data
        self.col = col
        self.comparable = comparable
        self.fila = fila
        self.adentro = adentro #NodoContenido
        self.afuera = afuera #NodoContenido
        self.izquierda = izq #NodoContenido
        self.derecha = der #NodoContenido
        self.arriba = up #NodoContenido
        self.abajo = down #NodoContenido
        self.upHeader = None
        self.izqHeader = None
        self.correos = lista()
        self.correos.insertar("general", "general")
        
    def agregarCorreo(self, sender, text, categoria):
        self.correos.buscar(categoria).senders.insertar(sender, sender)
        self.correos.buscar(categoria).senders.buscar(sender).textos.insertar(text, text)
        
        
class nodoCabecera():

    def __init__(self, nombre, sig, ant, primero):
        self.nombre = nombre
        self.sig = sig
        self.ant = ant
        self.primero = primero

class matriz():
    
    def __init__(self):
        self.primeroFila = None #NodoCabecera
        self.primeroColumna = None #NodoCabecera
        
    def buscarConString(self, comparable):
        filaElegida = self.primeroFila
        
        while filaElegida != None:
            aux = filaElegida.primero
            while aux != None:
                if aux.comparable == comparable:
                    return aux
                else:
                    aux = aux.derecha
            filaElegida = filaElegida.sig
        
    def buscar(self, fila, columna, comparable):
        encontrado = False
        filaElegida = self.primeroFila
        columnaElegida = self.primeroColumna
        
        #FILAS
        
        while (encontrado != True and filaElegida != None):
            if (filaElegida.nombre == fila):
                encontrado = True
            else:
                filaElegida = filaElegida.sig
        if (filaElegida == None):
            return None
        
        #COLUMNAS
        
        encontrado = False
        while (encontrado != True and columnaElegida != None):
            if (columnaElegida.nombre == columna):
                encontrado = True
            else:
                columnaElegida = columnaElegida.sig
        if (columnaElegida == None):
            return None
        
        #ENCUENTRA NODO

        encontrado = False
        auxOriginal = filaElegida.primero
        while (encontrado == False and auxOriginal != None):
        
            aux = auxOriginal
            while (aux.upHeader == None):
            
                aux = aux.arriba
            
            if (aux.upHeader == columnaElegida):
                if auxOriginal.data == comparable:
                    return auxOriginal
                else:
                    if (auxOriginal.afuera != None):
                        aux = auxOriginal.afuera
                        while (aux != None):
                            if (aux.data == comparable):
                                return aux
                            else:
                                aux = aux.afuera
                        return None
                    else:
                        return None
            else:
                auxOriginal = auxOriginal.derecha
            
        

        return None
        
    def eliminar(self, target):
        if (target != None):
            #FILAS
            if (target.adentro == None and target.afuera == None):
                if (target.izqHeader != None):
                    if (target.derecha == None):
                        target.izqHeader.ant.sig = target.izqHeader.sig
                        if target.izqHeader.sig != None:   
                            target.izqHeader.sig.ant = target.izqHeader.ant.sig
                        target.izqHeader.primero = None
                        target.izqHeader = None
                    else:
                        target.derecha.izquierda = None
                        target.derecha.izqHeader = target.izqHeader
                        target.izqHeader.primero = target.derecha
                else:
                    if (target.derecha == None):
                        target.izquierda.derecha = None
                    else:
                        target.izquierda.derecha = target.derecha
                        target.derecha.izquierda = target.izquierda
                #COLUMNAS
                if (target.upHeader != None):
                    if (target.abajo == None):
                        target.upHeader.ant.sig = target.upHeader.sig
                        if target.upHeader.sig != None:
                            target.upHeader.sig.ant = target.upHeader.ant.sig
                        target.upHeader.primero = None
                        target.upHeader = None
                    else:
                        target.abajo.arriba = None
                        target.abajo.upHeader = target.upHeader
                        target.upHeader.primero = target.abajo
                else:
                    if (target.abajo == None):
                        target.arriba.abajo = None                    
                    else:                    
                        target.arriba.abajo = target.abajo
                        target.abajo.arriba = target.arrib      
            elif (target.adentro == None and target.afuera != None):
                if (target.izqHeader != None):
                    target.afuera.izqHeader = target.izqHeader
                    target.izqHeader.primero = target.afuera
                if (target.upHeader != None):
                    target.afuera.upHeader = target.upHeader
                    target.upHeader.primero = target.afuera
                if (target.izquierda != None):
                    target.afuera.izquierda = target.izquierda
                    target.izquierda.derecha = target.afuera
                if (target.derecha != None):
                    target.afuera.derecha = target.derecha
                    target.derecha.izquierda = target.afuera
                if (target.arriba != None):
                    target.afuera.arriba = target.arriba
                    target.arriba.abajo = target.afuera
                if (target.abajo != None):
                    target.afuera.abajo = target.abajo
                    target.abajo.arriba = target.afuera
            elif (target.afuera != None and target.adentro != None):
                target.adentro.afuera = target.afuera
                target.afuera.adentro = target.adentro
            elif (target.afuera == None and target.adentro != None):
                target.adentro.afuera = None
                target.adentro = None
        
    def getGraphviz(self):
        codigo2 = ""

        sizeDominios = len(listaDominios)
        if sizeDominios == 1:
            codigo2 = codigo2 + str(listaDominios[0])
        for x in range(1, sizeDominios):
            codigo2 = codigo2 + str((Relacion(listaDominios[x], listaDominios[x-1])).data)
            codigo2 = codigo2 + str((Relacion(listaDominios[x-1], listaDominios[x])).data)

        a = self.primeroColumna
        while(a != None):
            b = a.primero
            relTemp = Relacion("@" + str(a.nombre), str(b.data.nombre))
            codigo2 = codigo2 + str(relTemp.data)
            relTemp = Relacion(str(b.data.nombre), "@" + str(a.nombre))
            codigo2 = codigo2 + str(relTemp.data)
            while b != None:
                if b.abajo != None:
                    relTemp = Relacion(str(b.data.nombre),str(b.abajo.data.nombre))
                    codigo2 = codigo2 + str(relTemp.data)
                    relTemp = Relacion(str(b.abajo.data.nombre),str(b.data.nombre))
                    codigo2 = codigo2 + str(relTemp.data)
                b = b.abajo
            if a.sig != None:
                relTemp = Relacion("@" + str(a.nombre),"@" + str(a.sig.nombre))
                codigo2 = codigo2 + str(relTemp.data)
                relTemp = Relacion("@" + str(a.sig.nombre),"@" + str(a.nombre))
                codigo2 = codigo2 + str(relTemp.data)
            a = a.sig
        a = self.primeroFila  
        codigo2 = codigo2 + str(Relacion("a","b").data)
        codigo2 = codigo2 + str(Relacion("b","a").data)
        codigo2 = codigo2 + str(Relacion("b","c").data)
        codigo2 = codigo2 + str(Relacion("c","b").data)
        codigo2 = codigo2 + str(Relacion("c","d").data)
        codigo2 = codigo2 + str(Relacion("d","c").data)
        codigo2 = codigo2 + str(Relacion("d","e").data)
        codigo2 = codigo2 + str(Relacion("e","d").data)
        codigo2 = codigo2 + str(Relacion("e","f").data)
        codigo2 = codigo2 + str(Relacion("f","e").data)
        codigo2 = codigo2 + str(Relacion("f","g").data)
        codigo2 = codigo2 + str(Relacion("g","f").data)
        codigo2 = codigo2 + str(Relacion("g","h").data)
        codigo2 = codigo2 + str(Relacion("h","g").data)
        codigo2 = codigo2 + str(Relacion("h","i").data)
        codigo2 = codigo2 + str(Relacion("i","h").data)
        codigo2 = codigo2 + str(Relacion("i","j").data)
        codigo2 = codigo2 + str(Relacion("j","i").data)
        codigo2 = codigo2 + str(Relacion("j","k").data)
        codigo2 = codigo2 + str(Relacion("k","j").data)
        codigo2 = codigo2 + str(Relacion("k","l").data)
        codigo2 = codigo2 + str(Relacion("l","k").data)
        codigo2 = codigo2 + str(Relacion("l","m").data)
        codigo2 = codigo2 + str(Relacion("m","l").data)
        codigo2 = codigo2 + str(Relacion("m","n").data)
        codigo2 = codigo2 + str(Relacion("n","m").data)
        codigo2 = codigo2 + str(Relacion("n","o").data)
        codigo2 = codigo2 + str(Relacion("o","n").data)
        codigo2 = codigo2 + str(Relacion("o","p").data)
        codigo2 = codigo2 + str(Relacion("p","o").data)
        codigo2 = codigo2 + str(Relacion("p","q").data)
        codigo2 = codigo2 + str(Relacion("q","p").data)
        codigo2 = codigo2 + str(Relacion("q","r").data)
        codigo2 = codigo2 + str(Relacion("r","q").data)
        codigo2 = codigo2 + str(Relacion("r","s").data)
        codigo2 = codigo2 + str(Relacion("s","r").data)
        codigo2 = codigo2 + str(Relacion("s","t").data)
        codigo2 = codigo2 + str(Relacion("t","s").data)
        codigo2 = codigo2 + str(Relacion("t","u").data)
        codigo2 = codigo2 + str(Relacion("u","t").data)
        codigo2 = codigo2 + str(Relacion("u","v").data)
        codigo2 = codigo2 + str(Relacion("v","u").data)
        codigo2 = codigo2 + str(Relacion("v","w").data)
        codigo2 = codigo2 + str(Relacion("w","v").data)
        codigo2 = codigo2 + str(Relacion("w","x").data)
        codigo2 = codigo2 + str(Relacion("x","w").data)
        codigo2 = codigo2 + str(Relacion("x","y").data)
        codigo2 = codigo2 + str(Relacion("y","x").data)
        codigo2 = codigo2 + str(Relacion("y","z").data)
        codigo2 = codigo2 + str(Relacion("z","y").data)
        while (a != None):
            b = a.primero
            if b != None:
                relTemp = Relacion(str(a.nombre), str(b.data.nombre))
                codigo2 = codigo2 + str(relTemp.data)
                relTemp = Relacion(str(b.data.nombre), str(a.nombre))
                codigo2 = codigo2 + str(relTemp.data)
                while b != None:
                    if b.derecha != None:
                        relTemp = Relacion(str(b.data.nombre),str(b.abajo.data.nombre))
                        codigo2 = codigo2 + str(relTemp.data)
                        relTemp = Relacion(str(b.abajo.data.nombre),str(b.data.nombre))
                        codigo2 = codigo2 + str(relTemp.data)
                    b = b.derecha
            a = a.sig
        return (str(codigo2))
                    
    def buscarColumna(self, nodo, columna, nuevo):
        if nodo != None:
            if nodo.nombre == columna:
                return nodo
            elif nodo.nombre > columna:
                x = nodoCabecera(columna, self.primeroColumna, None, nuevo)
                nodo.ant = x
                self.primeroColumna = x
                nuevo.upHeader = x
                return x
            elif nodo.nombre < columna:
                if nodo.sig != None:
                    if nodo.sig.nombre > columna:
                        x = nodoCabecera(columna, nodo.sig, nodo, nuevo)
                        nodo.sig.ant = x
                        nodo.sig = x
                        x.primero = nuevo
                        nuevo.upHeader = x
                        return x
                    else:
                        return self.buscarColumna(nodo.sig, columna, nuevo)
                else:
                    x = nodoCabecera(columna, None, nodo, nuevo)
                    nodo.sig = x
                    nuevo.upHeader = x
                    return x
            return None
        
    
    def buscarFila(self, nodo, fila, nuevo):
        if nodo != None:
            if nodo.nombre == fila:
                return nodo
            elif nodo.nombre > fila:
                x = nodoCabecera(fila, self.primeroFila, None, nuevo)
                nodo.ant = x
                self.primeroFila = x
                nuevo.izqHeader = x
                return x
            elif nodo.nombre < fila:
                if nodo.sig != None:
                    if nodo.sig.nombre > fila:
                        x = nodoCabecera(fila, nodo.sig, nodo, nuevo)
                        nodo.sig.ant = x
                        nodo.sig = x
                        x.primero = nuevo
                        nuevo.izqHeader = x
                        return x
                    else:
                        return self.buscarFila(nodo.sig, fila, nuevo)
                else:
                    x = nodoCabecera(fila, None, nodo, nuevo)
                    nodo.sig = x
                    nuevo.izqHeader = x
                    return x
            return None
        
    def insertar(self, fila, columna, data, comparable):
        #m, gmail, marco, marco
        filaElegida = None #NodoCabecera
        columnaElegida = None #NodoCabecera
        nuevo = nodoContenido(data, columna, fila, None, None, None, None, None, None, comparable)
        if self.primeroFila == None:
            filaElegida = self.primeroFila = nodoCabecera(fila, None, None, nuevo)
            nuevo.izqHeader = self.primeroFila
        else:
            filaElegida = self.buscarFila(self.primeroFila, fila, nuevo)
        if self.primeroColumna == None:
            columnaElegida = self.primeroColumna = nodoCabecera(columna, None, None, nuevo)
            nuevo.upHeader = self.primeroColumna
        else:
            columnaElegida = self.buscarColumna(self.primeroColumna, columna, nuevo)

        if filaElegida.primero !=  nuevo:
            self.enlazarF(nuevo, filaElegida, columnaElegida)
        if columnaElegida.primero != nuevo:
            self.enlazarC(nuevo, filaElegida, columnaElegida)
            
            
    def enlazarF(self, nuevo, filaCabecera, columnaCabecera):
        encontrado = False
        auxOriginal = filaCabecera.primero
        while (encontrado == False):
            aux = auxOriginal
            while (aux.upHeader == None):
                aux = aux.arriba
            columnaCorres = aux.upHeader
            if columnaCorres.nombre < columnaCabecera.nombre:
                if auxOriginal.derecha == None:
                    auxOriginal.derecha = nuevo
                    nuevo.izquierda = auxOriginal
                    encontrado = True
                else:
                    auxOriginal = auxOriginal.derecha
            elif columnaCorres.nombre > columnaCabecera.nombre and auxOriginal == filaCabecera.primero:
                nuevo.izqHeader = filaCabecera
                nuevo.derecha = auxOriginal
                auxOriginal.izqHeader = None
                auxOriginal.izquierda = nuevo
                filaCabecera.primero = nuevo
                encontrado = True
            elif columnaCorres.nombre > columnaCabecera.nombre:
                nuevo.derecha = auxOriginal
                nuevo.izquierda = auxOriginal.izquierda
                auxOriginal.izquierda.derecha = nuevo
                auxOriginal.izquierda = nuevo
                encontrado = True
            elif columnaCorres.nombre == columnaCabecera.nombre:
                flag = False
                aux = auxOriginal
                while (aux.afuera != None and flag == False):

                    aux = aux.afuera
                    if (aux.comparable == nuevo.comparable):

                        flag = True


                if (flag != True):

                    aux.afuera = nuevo
                    nuevo.adentro = aux
                    encontrado = True
                    flag = True

                encontrado = True
                
                    
    def enlazarC(self, nuevo, filaCabecera, columnaCabecera):
        encontrado = False
        auxOriginal = columnaCabecera.primero
        aux = columnaCabecera.primero
        while (encontrado == False and auxOriginal != None):
            aux = auxOriginal
            while(aux.izqHeader == None):
                aux = aux.izquierda
            filaCorres = aux.izqHeader
            if filaCorres.nombre < filaCabecera.nombre:
                if auxOriginal.abajo == None:
                    auxOriginal.abajo = nuevo
                    nuevo.arriba = auxOriginal
                    encontrado = True
                else:
                    auxOriginal = auxOriginal.abajo
            elif filaCorres.nombre > filaCabecera.nombre and auxOriginal == columnaCabecera.primero:
                nuevo.upHeader = columnaCabecera
                nuevo.abajo = auxOriginal
                auxOriginal.arriba = nuevo
                auxOriginal.upHeader = None
                columnaCabecera.primero = nuevo
                encontrado = True
            elif filaCorres.nombre > filaCabecera.nombre:
                nuevo.abajo = auxOriginal
                nuevo.arriba = auxOriginal.arriba
                auxOriginal.arriba.abajo = nuevo
                auxOriginal.arriba = nuevo
                encontrado = True    
            elif filaCorres.nombre == filaCabecera.nombre:
                flag = False    
                aux = auxOriginal
                while (aux.afuera != None and flag == False):

                    aux = aux.afuera
                    if (aux.comparable == nuevo.comparable):
                        flag = True


                if (flag != True):

                    aux.afuera = nuevo
                    nuevo.adentro = aux
                    encontrado = True
                    flag = True

                encontrado = True
                
        
        
#-----------------------------------------------MATRIZ DISPERSA TERMINA

#-----------------------------------------------AVL EMPIEZA

class nodoAVL():

    def __init__(self, key, comparable):

            self.key = key
            self.valor = comparable
            self.izq = None
            self.der = None


class AVL():   
    
    def __init__(self):

        self.raiz = None
        self.altura = -1
        self.balance = 0
        self.codigo1 = " "
        self.codigo2 = " "
        self.postOrdenText = " "
        self.postOrdenText3 = " "
        
    def insertar(self, valor, comparable):

        n = nodoAVL(valor, comparable)
        if not self.raiz:
            self.raiz = n
            self.raiz.izq = AVL()
            self.raiz.der = AVL()
        elif comparable < self.raiz.valor:
            self.raiz.izq.insertar(valor,comparable)
        elif comparable > self.raiz.valor:
            self.raiz.der.insertar(valor,comparable)
            
        self.rebalancear()
        
    def buscar(self, dato):
        return self.buscarAux(dato, self.raiz)  
    
    def buscarAux(self, dato, raiz):
        if raiz == None:
            return None
        else:
            if str(raiz.valor) == str(dato):
                return raiz
            else:
                if str(raiz.valor) > str(dato):
                    return self.buscarAux(str(dato), raiz.izq.raiz)
                else:
                    return self.buscarAux(str(dato), raiz.der.raiz)
            
    def inorden(self, raiz, cont):  
        if raiz == None:
            return
        else:
            self.inorden(raiz.izq.raiz,cont)
            cont = cont + 1
            self.inorden(raiz.der.raiz,cont)
        return  
    
            
    def rebalancear(self):

        self.actAltura(recursive=False)
        self.actBalances(False)

        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:

                if self.raiz.izq.balance < 0:
                    self.raiz.izq.rotarIzq()
                    self.actAltura()
                    self.actBalances()
                self.rotarDer()
                self.actAltura()
                self.actBalances()
            
            if self.balance < -1:
                
                if self.raiz.der.balance > 0:
                    self.raiz.der.rotarDer() 
                    self.actAltura()
                    self.actBalances()

                self.rotarIzq()
                self.actAltura()
                self.actBalances() 
                
    def actAltura(self, recursive=True):
        if self.raiz: 
            if recursive: 
                if self.raiz.izq: 
                    self.raiz.izq.actAltura()
                if self.raiz.der:
                    self.raiz.der.actAltura()
            
            self.altura = 1 + max(self.raiz.izq.altura, self.raiz.der.altura)
        else: 
            self.altura = -1
            
    def actBalances(self, recursive=True):
        if self.raiz:
            if recursive:
                if self.raiz.izq:
                    self.raiz.izq.actBalances()
                if self.raiz.der:
                    self.raiz.der.actBalances()
 
            self.balance = self.raiz.izq.altura - self.raiz.der.altura
        else:
            self.balance = 0 
 
            
    def rotarDer(self):
        'Pasar el self como el derecho de su izquierdo'

        newRaiz = self.raiz.izq.raiz
        newIzqSub = newRaiz.der.raiz
        oldRaiz = self.raiz
 
        self.raiz = newRaiz
        oldRaiz.izq.raiz = newIzqSub
        newRaiz.der.raiz = oldRaiz 
        
    def rotarIzq(self):
        'Pasar el self como el izq del der'
        newRaiz = self.raiz.der.raiz
        newIzqSub = newRaiz.izq.raiz
        oldRaiz = self.raiz
 
        self.raiz = newRaiz
        oldRaiz.der.raiz = newIzqSub
        newRaiz.izq.raiz = oldRaiz 
        
    def getRaiz(self):
        return self.raiz
        
    def eliminar(self, valor):

        if self.raiz != None:
            if self.raiz.valor == valor:
                if not self.raiz.izq.raiz and not self.raiz.der.raiz:
                    self.raiz = None
                elif not self.raiz.izq.raiz:                
                    self.raiz = self.raiz.der.raiz
                elif not self.raiz.der.raiz:
                    self.raiz = self.raiz.izq.raiz
                else:
                    sig = self.raiz.der.raiz  
                    while sig and sig.izq.raiz:
                        sig = sig.izq.raiz
 
                    if sig:
                        self.raiz.valor = sig.valor
                        self.raiz.der.eliminar(sig.valor)
 
            elif valor < self.raiz.valor:
                self.raiz.izq.eliminar(valor)
 
            elif valor > self.raiz.valor:
                self.raiz.der.eliminar(valor)
            self.rebalancear()
        
    def postOrden(self, raiz):  
        if raiz == None:
            return
        else:
            self.postOrden(raiz.izq.raiz)
            self.postOrden(raiz.der.raiz)
            self.postOrdenText =  str(self.postOrdenText)  + "," +  str(raiz.valor)
            return
        
    def getPostOrden(self):
        self.postOrdenText = ""
        self.postOrden(self.raiz)
        return self.postOrdenText
            
    def toDotAux(self):
            self.codigo1 = " "
            self.codig2 = " "
            self.toDot(None, self.raiz)
            return str(str(self.codigo1) + str(self.codigo2))
            
    def toDot(self, raizAVL, ramaAVL):
        
         if ramaAVL != None and raizAVL != None:
            
            relaTemp = Relacion(raizAVL.valor, ramaAVL.valor)
            self.codigo2 = self.codigo2 + relaTemp.data
            self.toDot(ramaAVL, ramaAVL.izq.raiz);
            self.toDot(ramaAVL, ramaAVL.der.raiz);
        
         elif ramaAVL != None:
            
            nod =  Nodo(ramaAVL.valor)
            self.codigo1 = self.codigo1 + "\"" + ramaAVL.valor + "\" \n"
            self.toDot(ramaAVL, ramaAVL.izq.raiz)
            self.toDot(ramaAVL, ramaAVL.der.raiz)
            
#------------------------------------AVL TERMINA

#------------------------------------ABB EMPIEZA

class NodoABB:
    
    def __init__(self, data, comparable):
        self.data = data
        self.comparable = comparable
        self.izq = None
        self.der = None
        self.antTarget = None
        self.textos = lista()
    
class ABB:
    
    def __init__(self):
        self.codigo2 = " "
        self.inordenText = " "
        self.raiz = None
        
    def buscar(self, comparable):
        return self.buscarAux(comparable, self.raiz)
        
    def buscarAux(self, comparable, raiz):
        if raiz != None:
            if raiz.comparable == comparable:
                return raiz
            elif raiz.comparable > comparable:
                return self.buscarAux(comparable, raiz.izq)
            elif raiz.comparable < comparable:
                return self.buscarAux(comparable, raiz.der)
        else:
            return None
        
    def insertar(self, data, comparable):
    
        if (self.raiz == None):
            self.raiz = NodoABB(data, comparable)
        else:
            self.insertar2(data, comparable, self.raiz)
        
    def insertar2(self, data, comparable, raiz):
        if (comparable < raiz.comparable):
            if (raiz.izq == None):
                raiz.izq = NodoABB(data, comparable)
            else:
                self.insertar2(data, comparable, raiz.izq)
        elif (comparable > raiz.comparable):
            if (raiz.der == None):
                raiz.der = NodoABB(data, comparable)
            else:
                self.insertar2(data, comparable, raiz.der)

    def inorden(self):
        self.inordenText = " "
        self.inorden2(self.raiz)
        return self.inordenText
        
    def inorden2(self, raiz):
        if raiz != None:
            self.inorden2(raiz.izq)
            self.inordenText = str(self.inordenText) + "," + str(raiz.comparable)
            self.inorden2(raiz.der)
            
    def getGraphviz(self):
        self.codigo2 = ""
        self.getGraphvizAux(self.raiz)
        a = (str(self.codigo2))
        if a == "":
            if self.raiz != None:
                return ("\"" + str(self.raiz.comparable) + "\"")
        return a
        
    def getGraphvizAux(self, raiz):
        if raiz != None:
            self.getGraphvizAux(raiz.izq)
            
            if raiz.izq != None:
                self.codigo2 = self.codigo2 + str(Relacion(raiz.comparable, raiz.izq.comparable).data)
            if raiz.der != None:
                self.codigo2 = self.codigo2 + str(Relacion(raiz.comparable, raiz.der.comparable).data)
            self.getGraphvizAux(raiz.der)
            
    def eliminar(self, comparable):
        antTarget = None
        target = self.buscarEliminar(comparable, self.raiz)
        a = antTarget
        if (target != None):
        
            aux = None
            aux2 = None
            if (target.izq != None):
                aux = target.izq
                aux2 = target
                while (aux.der != None):
                    aux2 = aux
                    aux = aux.der
                if (aux2 == target):
                    aux.der = target.der
                    target.der = target.izq = None
                else:
                    aux2.der = aux.izq
                    aux.izq = target.izq
                    aux.der = target.der
                    target.der = target.izq = None
            elif (target.der != None):
                aux = target.der
                aux2 = target
                while (aux.izq != None):
                    aux2 = aux
                    aux = aux.izq
                if (aux2 == target):
                    aux.izq = target.izq
                    target.der = target.izq = None
                else:
                    aux2.izq = aux.der
                    aux.izq = target.izq
                    aux.der = target.der
                    target.der = target.izq = None
            if (self.antTarget != None):
                if (self.antTarget.comparable < aux.comparable):
            
                    self.antTarget.der = aux
                else:
                    self.antTarget.izq = aux
            else:
                self.raiz = aux
            

    def buscarEliminar(self, comparable, raiz):
        if (raiz != None):
            if (raiz.comparable == comparable):
                return raiz
            elif (raiz.comparable > comparable):
                self.antTarget = raiz
                return self.buscarEliminar(comparable, raiz.izq)
            elif (raiz.comparable < comparable):
                self.antTarget = raiz
                return self.buscarEliminar(comparable, raiz.der)
        else:
            self.antTarget = None
            return None
        self.antTarget = None
        return None
    
            
#------------------------------------ABB TERMINA
            
#------------------------------------ARBOL B EMPIEZA
         
class itemB:
    def __init__(self):
        self.carpetas = ArbolB(None, None)
        self.archivos = AVL()
            
class NodoB:
    def __init__(self, pk, pLlave, pDato):
        if pDato == None:
            self.mK = pk
            self.mB = 0
            self.mLlaves = [None for xs in range(2*pk+1)]
            self.mDatos = [None for xs in range(2*pk+1)]
            self.mPunteros = [None for xs in range(2*pk+2)]
            self.numeroDeNodoB = 1
        else:
            self.mK = pk
            self.mLlaves = [None for xs in range(2 * pk + 1)]
            self.mDatos = [None for xs in range(2 * pk + 1)]
            self.mPunteros = [None for xs in range((2 * pk) + 2)]
            self.mB = 1
            self.mLlaves[0] = pLlave
            self.mDatos[0] = pDato

    def getDotName(self):

        return str("NodoB" + str(id(self)))

    def toDot(self):


        b = ""

        b = b + str(self.getDotName())
        b = b + str("[label=\"<P0>")
        for i in range(0, self.mB):
            b = b + str("|" + str(self.mLlaves[i]))
            b = b + str("|<P" + str(i + 1) + ">")


        b = b + str("\"]\n")

        for i in range(0,(self.mB + 1)):

            if (self.mPunteros[i] != None):

                b = b + str(self.mPunteros[i].toDot())
                b = b + str(str(self.getDotName()) + ":P" + str(i) + " -> " + str(self.mPunteros[i].getDotName()) + "\n")
        return str(b)

    def setK(self, mK):

        self.mK = mK


    def getK(self):

        return self.mK
    
    


class SplitInt:

    def __init__(self, pPuntero, pLlave, pDato):

        self.mPuntero = pPuntero
        self.mLlave = pLlave 
        self.mDato = pDato


    def setPuntero(self, mPuntero):

        self.mPuntero = mPuntero


    def getPuntero(self):

        return self.mPuntero


    def setLlave(self, mLlave):

        self.mLlave = mLlave


    def getLlave(self):

        return self.mLlave


    def setDato(self, mDato):

        self.mDato = mDato


    def getDato(self):

        return self.mDato



class LlaveEntero:

    def LlaveEntero(self, pValor):

        self.mLlave = pValor


    def getKey():

        return self.mLlave


    def igualA(self, pObjeto):
        if (self.mLlave == (pObjeto.getKey())):
            return True
        else:
            return False


    def menorQue(self, pObjeto):
        if (self.mLlave < int(pObjeto.getKey())):
            
            return True
        else:
            return False


    def mayorQue(self, pObjeto):
        if (self.mLlave > int(pObjeto.getKey())):
            
            return True
        else:
            return False

    def menorOIgualQue(self, pObjeto):
        if (self.mLlave <= int(pObjeto.getKey())):
            
            return True
        else:
            return False


    def mayorOIgualQue(self, pObjeto):
        if (self.mLlave >= int(pObjeto.getKey())):
            
            return True
        else:
            return False
        
        
class ArbolB:
    
    def __init__(self, k, pRaiz):
        self.mRaiz = None
        self.mK = 2
        self.mAltura = 0
        if k != None:
            self.mk = k
        if pRaiz != None:
            self.mk = pRaiz.getK()
            self.mRaiz = pRaiz
            self.mAltura = 1
            
    def toDot(self):
        
            b = ""
            b = str(b) + str("digraph g { \n node [shape=record]\n")
            if self.mRaiz != None:
                b = str(b) + str(self.mRaiz.toDot())
            else:
                b = str(b) + str("\"Vacio\"")
            b = b + str("}")
            return str(b)
        
    def insert(self, key, obj):
        
            if (self.mAltura == 0):
            
                self.mRaiz = NodoB(self.mK, key, obj)
                self.mAltura = 1
                return
            

            splitted = self.insert2(self.mRaiz, key, obj, 1)

            if (splitted != None):
                ptr = self.mRaiz

                self.mRaiz = NodoB(self.mK, splitted.getLlave(), splitted.getDato())
                self.mRaiz.mPunteros[0] = ptr
                self.mRaiz.mPunteros[1] = splitted.getPuntero()
                self.mAltura = self.mAltura + 1
                
    def insert2(self, node, key, obj, level):
        
        splitted = None
        ptr = None

        i = 0
        while ((i < node.mB) and (key > (node.mLlaves[i]))):
            i = i + 1

        if ((i < node.mB) and key == (node.mLlaves[i])):

            node.mDatos[i] = obj
            return None


        if (level < self.mAltura):


            splitted = self.insert2(node.mPunteros[i], key, obj, level + 1)

            if (splitted == None):
                return None
            else:

                key = splitted.mLlave
                obj = splitted.mDato
                ptr = splitted.mPuntero



        i = node.mB - 1
        while ((i >= 0) and (node.mLlaves[i] == None or key < (node.mLlaves[i]))):

            node.mLlaves[i + 1] = node.mLlaves[i]
            node.mDatos[i + 1] = node.mDatos[i]
            node.mPunteros[i + 2] = node.mPunteros[i + 1]
            i = i - 1


        node.mLlaves[i + 1] = key
        node.mDatos[i + 1] = obj
        if (splitted != None):
            node.mPunteros[i + 2] = splitted.mPuntero
        node.mB = node.mB + 1

        if (node.mB > 2 * self.mK):


            newnode = NodoB(self.mK, None, None)
            newnode.mPunteros[self.mK] = node.mPunteros[node.mB]
            node.mPunteros[node.mB] = None
            node.mB = self.mK + 1
            for i in range (0, (self.mK)):
                
                newnode.mLlaves[i] = node.mLlaves[i + node.mB]
                node.mLlaves[i + node.mB] = None
                newnode.mDatos[i] = node.mDatos[i + node.mB]
                node.mDatos[i + node.mB] = None
                newnode.mPunteros[i] = node.mPunteros[i + node.mB]
                node.mPunteros[i + node.mB] = None

            node.mB -= 1

            splitted = SplitInt(newnode, node.mLlaves[node.mB], node.mDatos[node.mB])
            node.mLlaves[node.mB] = None
            node.mDatos[node.mB] = None
            newnode.mB = self.mK
            node.mB = self.mK

            return splitted


        return None
        
    def search(self, key):
        
            return self.search2(key, self.mRaiz)
        

    def search2(self, key, node):


        if ((node == None) or (node.mB < 1)):

            return None


        if (key < (node.mLlaves[0])):
            return self.search2(key, node.mPunteros[0])

        if (key > (node.mLlaves[node.mB - 1])):
            return self.search2(key, node.mPunteros[node.mB])

        i = 0
        while ((i < node.mB - 1) and (key > (node.mLlaves[i]))):
            i+=1

        if (key == (node.mLlaves[i])):
            return node.mDatos[i]

        return self.search2(key, node.mPunteros[i])

        

    def getAltura(self):

        return self.mAltura

    
#------------------------------------ARBOL B TERMINA

usuariosDropbox = lista()
bitaDrop = listaB()
bitaGM = listaB()
matrizGmail = matriz()
listaDominios = []
listaDominios.append("gmail.com")
userDropBox = Usuario("correogmail", "staff@gmail.com","staff")
matrizGmail.insertar("s", "gmail.com", userDropBox, "staff@gmail.com")
prueba = ABB()

#----------------------LOGINS
@app.route('/VDPU',methods=['POST']) 
def verifyDUser():
    correo = str(request.form['correo'])
    user = usuariosDropbox.buscar(correo)
    if user != None:
        return "True"
    return "False"

@app.route('/verifyVUser',methods=['POST']) 
def verifyVUser():
    correo = str(request.form['correo'])
    user = usuariosDropbox.buscar(correo)
    if user.valor.verificado == True:
        return "True"
    elif user.valor.verificado == False:
        return "False"

@app.route('/verifyUser',methods=['POST']) 
def verifyUser():
    correo = str(request.form['correo'])
    user = usuariosDropbox.buscar(correo)
    user.valor.verificado = True
    return "Validated"

@app.route('/UpArchivo',methods=['POST']) 
def UpArchivo():
    archivo = str(request.form['file'])
    archivoprueba = archivo
    return archivoprueba

@app.route('/AddBD',methods=['POST']) 
def AddBD():
    archivo = str(request.form['text'])
    bitaDrop.insertar(archivo)
    return archivo

@app.route('/AddBG',methods=['POST']) 
def AddBG():
    archivo1 = str(request.form['text'])
    bitaGM.insertar(archivo1)
    return archivo1

@app.route('/GetBitaG') 
def GetBitaG():
    bitacora1 = bitaGM.getAll()
    return bitacora1

@app.route('/GetBitaD') 
def GetBitaD():
    bitacora = bitaDrop.getAll()
    return bitacora


@app.route('/loginDrop',methods=['POST']) 
def loginDrop():
    correo = str(request.form['correo'])
    passw = str(request.form['password'])
    user = usuariosDropbox.buscar(correo)
    if user == None:
        return "False"
    else:
        if user.valor.verificado == True:
            if user.valor.password == passw:
                return "True"
            else:
                return "False"
        else:
             return "False"
    
@app.route('/loginGmail',methods=['POST']) 
def loginGmail():
    correo = str(request.form['correo'])
    passw = str(request.form['password'])
    a = matrizGmail.buscarConString(correo)
    if a == None:
        return "False"
    else:
        if a.data.password == passw:
            return "True"
        else:
            return "False"

#---------------------METODOS QUE AGREGAN

@app.route('/crearCarpeta',methods=['POST']) 
def crearCarpeta():
    use = str(request.form['user'])
    path = str(request.form['path'])
    nombre = str(request.form['nombre'])
    user = usuariosDropbox.buscar(use)
    dir = path.split("/")
    if user != None:
        arbolActual = user.valor.root
        for i in range(1, len(dir)):
            b = dir[i]
            if b != "":
                buscado = arbolActual.search(b)
                if buscado == None:
                    return "Error2" #No existe el directorio"
                else:
        
                    arbolActual = buscado.carpetas
        arbolActual.insert(nombre, itemB())
        receiver = matrizGmail.buscarConString(use)
        sender = matrizGmail.buscarConString("staff@dropbox.com")   
        receiver.agregarCorreo(sender.data.correo, "Se ha creado la carpeta: "+nombre +" en la ruta: "+path, "general")
        return "Exito"
    else:
        return "Error" #No existe el usuario
    
@app.route('/crearArchivo',methods=['POST']) 
def crearArchivo():
    use = str(request.form['user'])
    path = str(request.form['path'])
    nombre = str(request.form['nombre'])
    bytes = str(request.form['bytes'])
    user = usuariosDropbox.buscar(use)
    dir = path.split("/")
    if user != None:
        arbolActual = user.valor.root
        avl = None
        for i in range(1, len(dir)):
            b = dir[i]
            if b != "":
                buscado = arbolActual.search(b)
                if buscado == None:
                    return "Error2"#No existe el directorio"
                else:
                    arbolActual = buscado.carpetas
                    avl = buscado.archivos
        if avl != None:
            avl.insertar(bytes,nombre)
            receiver = matrizGmail.buscarConString(use)
            sender = matrizGmail.buscarConString("staff@dropbox.com")   
            receiver.agregarCorreo(sender.data.correo, "Se ha cargado el archivo: "+nombre, "general")

        else:
            avl = user.valor.archivosRoot
        return "Exito"
            
    else:
        return "Error" #No existe el usuario

@app.route('/addUserGmail',methods=['POST']) 
def addUserGmail():
    dominio = str(request.form['dominio'])
    inicial = str(request.form['inicial'])
    usuario = str(request.form['usuario'])
    password = str(request.form['password'])
    encontrado = False
    index = len(listaDominios)
    for x in range(0, (index)):        
        if listaDominios[x] == dominio:
            encontrado = True
            x = index + 100
    if encontrado == True:
        stringCorreo = str(usuario) + "@" + str(dominio)
        userX = Usuario(password, stringCorreo, usuario)
        matrizGmail.insertar(inicial, dominio, userX, stringCorreo)
        return matrizGmail.buscarConString(stringCorreo).data.correo
    else: 
        return "Error" #No existe el dominio

@app.route('/addCategoria',methods=['POST']) 
def addCategoria():
    user = str(request.form['user'])
    categoria = str(request.form['categoria'])
    receiver = matrizGmail.buscarConString(user)
    if receiver != None:
        matrizGmail.buscarConString(receiver.data.correo).correos.insertar(categoria, categoria)
        return str(matrizGmail.buscarConString(receiver.data.correo).correos.len);
    else:
        return "Error" #No existe el usuario

@app.route('/addUsuarioDrop',methods=['POST']) 
def addUsuarioDrop():
    correo = str(request.form['correo'])
    password = str(request.form['password'])
    
    userTemp = UsuarioDrop(password, correo)
    use = usuariosDropbox.buscar(correo)
    if use == None:
        usuariosDropbox.insertar(userTemp, correo)
        receiver = matrizGmail.buscarConString(correo)
        sender = matrizGmail.buscarConString("staff@dropbox.com")
        if sender != None and receiver != None:
            receiver.agregarCorreo(sender.data.correo, "Bienvenido a Dropbox. Verifica tu cuenta en el siguiente boton.", "general")
            return "Exito"
        return "Error2" #El correo no existe en la matriz
    else:
        return "Error" #El correo del usuario ya tiene una cuenta en dropbox

@app.route('/addDominio',methods=['POST']) 
def addDominio():
    p = str(request.form['dominio'])
    listaDominios.append(p)
    return "'" + str(listaDominios[len(listaDominios) - 1]) + "'"

@app.route('/ViewSender',methods=['POST']) 
def ViewSender():
    correo = str(request.form['correo'])
    a = matrizGmail.buscarConString(correo)
    if a == None:
        return "False"
    else:
        return "True"
#------------------------METODOS QUE OBTIENEN DATOS
@app.route('/SDomains') 
def SDomains():
    respuesta = listaDominios[0]
    for x in range(1, len(listaDominios)):
        respuesta = respuesta + "," + listaDominios[x] 
    return  respuesta

@app.route('/SizeD') 
def SizeD():
    respuesta = str(len(listaDominios))
    return  respuesta

    
@app.route('/getListaDeArchivos',methods=['POST']) 
def getListaDeArchivos():
    use = str(request.form['user'])
    path = str(request.form['path'])
    user = usuariosDropbox.buscar(use)
    dir = path.split("/")
    if user != None:
        arbolActual = user.valor.root
        avl = None
        for i in range(1, len(dir)):
            b = dir[i]
            if b != "":
                buscado = arbolActual.search(b)
                if buscado == None:
                    return "Error2" #No existe el directorio"
                else:
                    arbolActual = buscado.carpetas
                    avl = buscado.archivos
        return avl.getPostOrden()
    else:
        return "Error" #no existe el usuario de dropbox
    
@app.route('/getUnArchivo',methods=['POST']) 
def getUnArchivo():
    use = str(request.form['user'])
    path = str(request.form['path'])
    nombre = str(request.form['nombre'])
    user = usuariosDropbox.buscar(use)
    dir = path.split("/")
    if user != None:
        arbolActual = user.valor.root
        avl = None
        for i in range(1, len(dir)):
            b = dir[i]
            if b != "":
                buscado = arbolActual.search(b)
                if buscado == None:
                    return "Error2-" + str(b) #No existe el directorio"
                else:
                    arbolActual = buscado.carpetas
                    avl = buscado.archivos
        if avl != None:
           response = avl.buscar(nombre)
        else:
            response = user.valor.archivosRoot.buscar(nombre)
        if response != None:
            receiver = matrizGmail.buscarConString(use)
            sender = matrizGmail.buscarConString("staff@dropbox.com")   
            receiver.agregarCorreo(sender.data.correo, "Se ha descargado el archivo: "+nombre, "general")
            return response.key
            return "Exito"
        else:
            return "Error" #No existe el archivo
    else:
        return "Error" #No existe el usuario de dropbox

    
@app.route('/getTextosDeUnSender',methods=['POST']) 
def getTextosDeUnSender():
    send = str(request.form['sender'])
    receive = str(request.form['receiver'])
    cat = str(request.form['categoria'])
    sender = matrizGmail.buscarConString(send)
    receiver = matrizGmail.buscarConString(receive)
    if sender != None:
        a = matrizGmail.buscarConString(receiver.data.correo).correos.buscar(cat)
        if a != None:
            b = a.senders.buscar(sender.data.correo)
            if b != None:
                return b.textos.getAll()
            else:
                return "Error3" #El receiver no tiene correos del sender en esta categoria
        else:
            return "Error2" #El receiver no tiene una categoria que se llame como el parametro
    else:
        return "Error" #El correo sender no existe

@app.route('/DelGmail',methods=['POST']) 
def DelGmail():
    receive = str(request.form['receiver'])
    receiver = matrizGmail.buscarConString(receive)
    matrizGmail.eliminar(receiver);
    return "Exito"
    
@app.route('/GetCategorias',methods=['POST']) 
def getCategorias():
    receive = str(request.form['receiver'])
    receiver = matrizGmail.buscarConString(receive)
    a = matrizGmail.buscarConString(receiver.data.correo).correos.getAll()
    return a
    

@app.route('/getSenders',methods=['POST']) 
def getSenders():
    receive = str(request.form['receiver'])
    cat = str(request.form['cat'])
    receiver = matrizGmail.buscarConString(receive)    
    if receiver != None:
        a = matrizGmail.buscarConString(receiver.data.correo).correos.buscar(cat)
        if a != None:
            return a.senders.inorden()
        else:
            return "Error2" #No existe la categoria
    else:
        return "Error" #No existe el usuario

#--------------------------METODOS QUE MODIFICAN ESTRUCTURAS

@app.route('/eliminarUserDrop',methods=['POST']) 
def eliminarUserDrop():
    use = str(request.form['user'])
    user = usuariosDropbox.buscar(use)
    if user != None:
        usuariosDropbox.eliminar(usuariosDropbox.buscarIndex(use))
        return "Exito"
    else:
        return "Error" #No existe el usuario

@app.route('/moverCorreoDeCategoria', methods = ['POST'])
def moverCorreoDeCategoria():
    sender = str(request.form['sender'])
    cat1 = str(request.form['cat1']) #Categoria Original
    cat2 = str(request.form['cat2']) #Categoria Destino
    textoIndex = str(request.form['textoIndex'])
    user = str(request.form['user'])
    receiver = matrizGmail.buscarConString(user)
    if receiver != None and sender != None:
        a = receiver.correos.buscar(cat1) #Verifica si la primer categoria existe y la guarda en 'a'
        if a != None:
            b = receiver.correos.buscar(cat2) #Verifica si la segunda categoria existe y la guarda en 'b'
            if b != None:
                c = a.senders.buscar(sender) 
                if c != None:
                # a = nodo de la primer categoria
                # b = nodo de la segunda categoria
                # c = nodo del sender
                    d = c.textos.buscarConIndex(textoIndex)
                    # d = nodo del texto que se quiere mover
                    if d != None:
                        receiver.agregarCorreo(sender, d.valor, cat2)
                        c.textos.eliminar(textoIndex)
                        if c.textos.len == 0:
                            a.senders.eliminar(send)
                            return "Exito, hay que borrar el nodo"
                        return "Exito"
                    else:
                        return "Error5" #El index no existe
                    return "Exito"
                else:
                    return "Error4" #El sender no ha mandado correos al receiver
            else:
                return "Error3" #No existe la categoria de destino
        else:       
            return "Error2" #No existe la categoria de origen
    else:
        return "Error" #No existe alguno de los dos correos
    
    
    
@app.route('/mandarCorreo',methods=['POST']) 
def mandarCorreo():

    send = str(request.form['sender'])
    receive = str(request.form['receiver'])
    texto = str(request.form['texto'])
    sender = matrizGmail.buscarConString(send)
    receiver = matrizGmail.buscarConString(receive)
    if sender != None and receiver != None:
        receiver.agregarCorreo(sender.data.correo, texto, "general")
        return "Exito"
    else:
        return "Error" #El correo del recipiente no existe.

@app.route('/eliminarCorreo',methods=['POST']) 
def eliminarCorreo():
    send = str(request.form['sender'])
    categoria = str(request.form['categoria'])
    receive = str(request.form['receiver'])
    sender = matrizGmail.buscarConString(send)
    receiver = matrizGmail.buscarConString(receive)
    index = str(request.form['index'])
    
    if sender != None:
        a = matrizGmail.buscarConString(receiver.data.correo)
        if a != None:
            b = a.correos.buscar(categoria)
            if b != None:
                c = b.senders.buscar(sender.data.correo)
                if c != None:
                    c.textos.eliminar(index)
                    if c.textos.len == 0:
                        b.senders.eliminar(send)
                        return "Exito, hay que borrar el nodo."
                    return "Exito"
                else:
                    return "Error1" #El sender no ha mandado correos al receiver en esta categoria
            else:
                return "Error2" #El receiver no tiene la categoria escogida
        else:
            return "Error3" #El receiver no existe
    else:
        return "Error4" #El sender no existe

@app.route('/eliminarCategoria',methods=['POST']) 
def eliminarCategoria():
    use = str(request.form['user'])
    categoria = str(request.form['cat'])
    if categoria != "general":
        user = matrizGmail.buscarConString(use)
        if user != None:
            b = user.correos.buscar(categoria)
            w = user.correos.buscar("general")
            if b != None:
                inordenText = str(b.senders.inorden())
                correos = inordenText.split(",")
                for x in range(1,len(correos)):
                    a = correos[x]
                    senderActual = b.senders.buscar(correos[x])
                    cantCorreos = senderActual.textos.len
                    for xw in range(1,(cantCorreos+1)):
                        a = user.correos.buscar("general")
                        #b = user.corros.buscar(categoria)
                        #senderActual = el nodo del sender = c
                        #x = textoIndex
                        d = senderActual.textos.buscarConIndex(xw)
                        user.agregarCorreo(correos[x], d.valor, "general")
                    cantCorreos = senderActual.textos.len
                user.correos.eliminar(user.correos.buscarIndex(categoria))
                return "Exito"
            else:
                return "Error2" #La categoria seleccionada no existe
        else:
            return "Error1" #No existe el usuario
    else:        
        return "Error" #No se puede eliminar la categoria de general

#-------------------METODOS QUE GRAFICAN
    
@app.route('/graphAVLArchivos',methods=['POST']) 
def graphAVLArchivos():
    user = str(request.form['user'])
    path = str(request.form['path'])
    use = usuariosDropbox.buscar(user)
    
    dir = path.split("/")
    if use != None:
        avl = use.valor.archivosRoot
        arbolActual = use.valor.root
        for i in range(1, len(dir)):
            b = dir[i]
            if b != "":
                buscado = arbolActual.search(b)
                if buscado == None:
                    return "Error2" #No existe el directorio"
                else:
                    arbolActual = buscado.carpetas
                    avl = buscado.archivos
        return str(avl.toDotAux()) #Directorio encontrado
    
    else:
        return "Error" #No existe el usuario

@app.route('/graphArbolB',methods=['POST']) 
def graphArbolB():
    user = str(request.form['user'])
    path = str(request.form['path'])
    use = usuariosDropbox.buscar(user)
    dir = path.split("/")
    if use != None:
        arbolActual = use.valor.root
        for i in range(1, len(dir)):
            b = dir[i]
            if b != "":
                buscado = arbolActual.search(b)
                if buscado == None:
                    return "Error2" #No existe el directorio"
                else:
                    arbolActual = buscado.carpetas
        return str(arbolActual.toDot()) #Directorio encontrado
    else:
        return "Error" #No existe el usuario

    
@app.route('/graphCategorias',methods=['POST']) 
def graphCategorias():
    user = str(request.form['user'])
    receiver = matrizGmail.buscarConString(user)
    if receiver != None:
        return str(matrizGmail.buscarConString(receiver.data.correo).correos.graphviz());
    else:
        return "Error" #No existe el usuario
    
@app.route('/graphUsersDrop',methods=['POST']) 
def graphUsersDrop():
    param = str(request.form['param'])
    return str(usuariosDropbox.graphviz())    

@app.route('/graphMatriz') 
def graphMatriz():
    return matrizGmail.getGraphviz()

@app.route('/getGraphSenders',methods=['POST']) 
def getGraphABB():
    receive = str(request.form['receiver'])
    categoria = str(request.form['categoria'])
    receiver = matrizGmail.buscarConString(receive)    
    if receiver != None:
        try:
            response = matrizGmail.buscarConString(receiver.data.correo).correos.buscar(categoria).senders.getGraphviz()
        except:
            return "Error2"
        if response == "":
            return "VACIO"
        else:
            return response
    else:
        return "Error" #No existe el  usuario
    
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
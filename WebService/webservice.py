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
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
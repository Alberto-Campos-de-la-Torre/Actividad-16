from pprint import pprint, pformat
import json
from algoritmos import distanciaeuclidiana
from collections import deque

class Grafo:

    def __init__(self):
        self.__grafo = {}
        self.__2grafo = {}
 
    def __Add__(self,ox,oy,dx,dy):
   
        origen  = (ox,oy)
        destino = (dx,dy)

        o_d  = (destino)
        d_o  = (origen)

        if origen in self.__grafo:
            peso = distanciaeuclidiana(ox,oy,dx,dy)
            o_d = (destino,peso)
            self.__grafo[origen].append(o_d)
        else:
            peso = distanciaeuclidiana(ox,oy,dx,dy)
            o_d = (destino,peso)
            self.__grafo[origen] = [o_d]

        if destino in self.__grafo:
            peso = distanciaeuclidiana(ox,oy,dx,dy)
            d_o = (origen,peso)
            self.__grafo[destino].append(d_o)
        else:
            peso = distanciaeuclidiana(ox,oy,dx,dy)
            d_o = (origen,peso)
            self.__grafo[destino] = [d_o]
    
    def Mostrargrafo(self):
        str = pformat(self.__grafo, width=40, indent=1)
        print(str)

    @property
    def  Grafo(self):
        return self.__grafo
    
    def algoritmo_busqueda_profundidad(self,origen):

        visitados = deque()
        pila = deque()
        recorrido = deque()

        visitados.append(origen)
        pila.append(origen)

        while len(pila) > 0:
            vertice = pila[-1]
            recorrido.append(vertice)
            pila.pop()  

            adyacentes = self.__grafo[vertice]
            for i in adyacentes:
                ady = i[0]
                if ady not in visitados:
                    visitados.append(ady)
                    pila.append(ady)
        
        return recorrido

    def algoritmo_busqueda_Amplitud(self,origen):

        visitados = deque()
        cola = deque()
        recorrido = deque()

        visitados.append(origen)
        cola.append(origen)

        while len(cola) > 0:
            vertice = cola[0]
            recorrido.append(vertice)
            del cola[0]
                              
            adyacentes = self.__grafo[vertice]
            for i in adyacentes:
                ady = i[0]
                if ady not in visitados:
                    visitados.append(ady)
                    cola.append(ady)    
        
        return recorrido

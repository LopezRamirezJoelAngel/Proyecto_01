<<<<<<< HEAD
=======
from Productos import *
>>>>>>> 4e35af4 (Modificaciones Joel)
class ListaCircularDoble:
    class _Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.nodo_anterior = None
            self.nodo_siguiente = None
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0
    def __str__(self):
        # Muestra los elementos de la lista doblemnte ligada circular
        array = []
        nodo_actual = self.cabeza
        pivote = True
        contador = self.tamaño
<<<<<<< HEAD
=======
        i=0
>>>>>>> 4e35af4 (Modificaciones Joel)
        while contador != 0:
            if pivote != False or nodo_actual != self.cabeza:
                array.append(nodo_actual.valor)
                nodo_actual = nodo_actual.nodo_siguiente
                pivote = False
                contador -=1 
<<<<<<< HEAD
            else:
                break
        return str(array) + " Tamaño: " + str(self.tamaño)
    def prepend(self, valor):
        # Agrega un elemento al principio de la lista
=======
                print(array[i])
                i=i+1
            else:
                break
        return " Tamaño: " + str(self.tamaño)
    def prepend(self, valor):
        # Agrega un elemento al principio 
>>>>>>> 4e35af4 (Modificaciones Joel)
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
<<<<<<< HEAD
            self.cabeza.nodo_anterior = nuevo_nodo
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cola.nodo_siguiente = nuevo_nodo
            nuevo_nodo.nodo_anterior = self.cola
            self.cabeza = nuevo_nodo
        self.tamaño += 1
    def append(self, valor):
        # Agrega un elemento al final de la lista
=======
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cola.nodo_siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamaño += 1
    def append(self, valor):
        # Agrega un elemento al final
>>>>>>> 4e35af4 (Modificaciones Joel)
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.nodo_siguiente = nuevo_nodo
<<<<<<< HEAD
            nuevo_nodo.nodo_anterior = self.cola
            nuevo_nodo.nodo_siguiente = self.cabeza 
            self.cabeza.nodo_anterior = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño += 1
    def shift(self):
        # Saca el primer elemento de la lista
=======
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cola = nuevo_nodo
        self.tamaño += 1
    def shift(self):
        # Saca el primer elemento
>>>>>>> 4e35af4 (Modificaciones Joel)
        if self.tamaño == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_eliminado = self.cabeza
            self.cabeza = nodo_eliminado.nodo_siguiente
<<<<<<< HEAD
            self.cabeza.nodo_anterior = self.cola
            self.cola.nodo_siguiente = self.cabeza
            nodo_eliminado.nodo_anterior = None
            nodo_eliminado.nodo_siguiente = None
            self.tamaño -= 1
            return print(nodo_eliminado.valor)
    def pop(self):
        # Saca el ultimo elemento de la lista
=======
            self.cola.nodo_siguiente = self.cabeza
            nodo_eliminado.nodo_siguiente = None
            self.tamaño -= 1
    def pop(self):
        # Saca el ultimo elemento 
>>>>>>> 4e35af4 (Modificaciones Joel)
        if self.tamaño == 0:
            self.cabeza = None
            self.cola = None
        else:
<<<<<<< HEAD
            nodo_eliminado = self.cola
            self.cola = nodo_eliminado.nodo_anterior
            self.cola.nodo_siguiente = self.cabeza
            self.cabeza.nodo_anterior = self.cola
            nodo_eliminado.nodo_anterior = None
            nodo_eliminado.nodo_siguiente = None
            self.tamaño -= 1
            return print(nodo_eliminado.valor)
    def get(self, indice):
        # Obtiene un nodo dado un indice
        if indice == self.tamaño - 1:
            print(self.cola.valor)
            return self.cola
        elif indice == 0:
            print(self.cabeza.valor)
            return self.cabeza
        elif not (indice >= self.tamaño or indice < 0):
            indice_balanceado = int(self.tamaño / 2)
            if indice <= indice_balanceado:
                nodo_actual = self.cabeza
                contador = 0
                while contador != indice:
                    nodo_actual = nodo_actual.nodo_siguiente
                    contador += 1
                print(nodo_actual.valor)
                return nodo_actual
            else:
                nodo_actual = self.cola
                contador = self.tamaño - 1
                while contador != indice:
                    nodo_actual = nodo_actual.nodo_anterior
                    contador -= 1
                print(nodo_actual.valor)
                return nodo_actual
        else:
            return None
    def update(self, indice, valor):
        # Cambia el valor de un nodo dado el indice
=======
            nodo_actual = self.cabeza
            nueva_cola = nodo_actual
            contador = self.tamaño
            while contador != 0:
                if nodo_actual.nodo_siguiente != self.cabeza:
                    nueva_cola = nodo_actual
                    nodo_actual = nodo_actual.nodo_siguiente
                else:
                    break
            self.cola = nueva_cola
            self.cola.nodo_siguiente = self.cabeza
            self.tamaño -= 1
    def get(self, indice):
        # Obtiene un nodo dado un indice
        if indice == self.tamaño - 1:
            return self.cola
        elif indice == 0:
            return self.cabeza
        elif not (indice >= self.tamaño or indice < 0):
            nodo_actual = self.cabeza
            contador = 0
            while contador != indice:
                nodo_actual = nodo_actual.nodo_siguiente
                contador  += 1
            return nodo_actual
        else:
            return None
    def update(self,indice, valor):
        # Cambia el valor de un nodo dado un indice
>>>>>>> 4e35af4 (Modificaciones Joel)
        nodo_objetivo = self.get(indice)
        if nodo_objetivo != None:
            nodo_objetivo.valor = valor
        else:
            return None
    def insert(self, indice, valor):
<<<<<<< HEAD
        # Agrega un elemento en donde sea en la lista circular dado el indice
=======
        # Agrega un elemento dado el indice
>>>>>>> 4e35af4 (Modificaciones Joel)
        if indice == self.tamaño - 1:
            return self.append(valor)
        elif not (indice >= self.tamaño or indice < 0):
            nuevo_nodo = self._Nodo(valor)
            nodos_anteriores = self.get(indice)
            nodos_siguientes = nodos_anteriores.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nuevo_nodo
<<<<<<< HEAD
            nuevo_nodo.nodo_anterior = nodos_anteriores
            nuevo_nodo.nodo_siguiente = nodos_siguientes
            nodos_siguientes.nodo_anterior = nuevo_nodo
=======
            nuevo_nodo.nodo_siguiente = nodos_siguientes
>>>>>>> 4e35af4 (Modificaciones Joel)
            self.tamaño += 1
        else:
            return None
    def remove(self, indice):
<<<<<<< HEAD
        # Saca un elemento de donde sea de la lista circular dado un indice
=======
        # Saca un elemento dado el indice
>>>>>>> 4e35af4 (Modificaciones Joel)
        if indice == 0:
            return self.shift()
        elif indice == self.tamaño - 1:
            return self.pop()
        elif not (indice >= self.tamaño or indice < 0):
<<<<<<< HEAD
            nodo_removido = self.get(indice)
            nodos_anteriores = nodo_removido.nodo_anterior
            nodos_siguientes = nodo_removido.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nodos_siguientes
            nodos_siguientes.nodo_anterior  = nodos_anteriores
            nodo_removido.nodo_anterior = None
=======
            nodos_anteriores = self.get(indice - 1)
            nodo_removido = nodos_anteriores.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nodo_removido.nodo_siguiente
>>>>>>> 4e35af4 (Modificaciones Joel)
            nodo_removido.nodo_siguiente = None
            self.tamaño -= 1
            return nodo_removido
        else:
<<<<<<< HEAD
            return None
    def reverse(self):
        # Revierte los nodos (productos) de la lista
        nodos_revertidos = None
        self.cabeza.nodo_anterior = None
        self.cola.nodo_siguiente = None
        nodo_actual = self.cabeza
        self.cola = nodo_actual
        while nodo_actual != None:
            nodos_revertidos = nodo_actual.nodo_anterior
            nodo_actual.nodo_anterior = nodo_actual.nodo_siguiente
            nodo_actual.nodo_siguiente = nodos_revertidos
            nodo_actual = nodo_actual.nodo_anterior
        self.cabeza = nodos_revertidos.nodo_anterior
        self.cabeza.nodo_anterior = self.cola
        self.cola.nodo_siguiente = self.cabeza

cll = ListaCircularDoble()
=======
            return None
>>>>>>> 4e35af4 (Modificaciones Joel)

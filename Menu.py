"""La clase Menu se encarga de leer cada atributo de mis productos desde un csv.
Tambén distingue sus atributos y los imprime según su posición de fila"""
        
#Separa los atributos y los guarda en una lista que instancio con una clase
import csv
class Menu:
    def __init__(self, file_name):
        menu = Menu('listasProductos.csv') #Llamamos a nuestro documento csv

#Aquí definimos los atributos de cada producto
class Producto:
    def __init__(self, clave, nombre, marca, precio, existencias, tipo):
        self.clave = clave
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.existencias = existencias
        self.tipo = tipo

    def __str__(self):
        return f"Clave: {self.clave}\nNombre: {self.nombre}\nMarca: {self.marca}\nPrecio: ${self.precio}\nExistencias: {self.existencias}\nTipo: {self.tipo}"

#Aquí nuestro ciclo for va a asignar cada atributo según su posición
class Menu:
    def __init__(self, archivo):
        self.productos = []
        with open(archivo, "r") as archivo_csv:
            documento = csv.reader(archivo_csv)
            for fila in documento:
                clave = fila[0]
                nombre = fila[1]
                marca = fila[2]
                precio = fila[3]
                existencias = fila[4]
                tipo = fila[5]
                producto = Producto(clave, nombre, marca, precio, existencias, tipo)
                self.productos.append(producto)

    def seleccion(self):
        print("Bienvenido al menú:")
        for producto in self.productos:
            print(f"{producto.clave} - {producto.nombre} - {producto.marca} - {producto.precio} - {producto.existencias} - {producto.tipo}")
            
    def busqueda(self, clave):
        for producto in self.productos:
            if producto.clave == clave:
                return producto
        return None #Cuando no devuelve algún valor existente


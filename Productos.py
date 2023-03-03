class Producto():
    '''La clase Productos crea y define los parametros de un producto.
    
    Identifica el tipo (str) de un producto, entiendase esto como [agua, refresco, jugo,
    snacks, botana, dulce], recibe su nombre (str), su marca (str), su precio [float],
    la cantidad de ese producto[int] y su clave (str).

    Crea diccionarios con las listas de los productos.
    '''
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        self.tipo=tipo
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        self.cantidad=cantidad
        self.clave=clave

    def mostrarProducto(self):
        print(self.nombre)

class Snack(Producto):
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)

class Jugo(Producto):
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)

class Refresco(Producto):
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)

class Agua(Producto):
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)

class Dulce(Producto):
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)

class Botana(Producto):
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)

#Parte del código que me permite leer cada atributo de mis productos desde un csv
#separa los atributos y los guarda en una lista que instancio con una clase
listAux=[]
listaProductos=[]
with open('listasProductos.csv','r') as f:
    datosProductos=f.readlines()
    for linea in datosProductos:
        atributos=linea.split(',')
        listAux=atributos[:len(atributos)]
        print(listAux)
        #Realizo una lista de clases instanciadas->objetos
        nombreClases = listAux[5].rstrip('\n')
        listaProductos.append(globals()[nombreClases](listAux[0], listAux[1], listAux[2], listAux[3],listAux[4],listAux[5]))
    #print(listaProductos) #Parece que imprime la lista de objetos, pero pone la memoria y no sus atributos

#Tal cual un objeto puedo llamar a sus atributos de la lista y operar con él y sus métodos.
#Ejemplo:
print(listaProductos[1].nombre)

#Posibles errores, que pongan un enter o les falte un dato en la lista de productos, tenerlo en cuenta, o se pasen
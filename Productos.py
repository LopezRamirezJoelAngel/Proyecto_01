class Producto():
    '''La clase Productos crea y define los parametros de un producto.
    
    Identifica el tipo (str) de un producto, entiendase esto como [agua, refresco, jugo,
    snacks, botana, dulce], recibe su clave (str), su nombre (str), su marca (str), 
    su precio (float) y la cantidad de ese producto(int)

    Crea un objeto con una lista con los atributos de cada producto.
    '''
<<<<<<< HEAD
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
=======
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
>>>>>>> 4e35af4 (Modificaciones Joel)
        self.tipo=tipo
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        self.cantidad=cantidad
        self.clave=clave
<<<<<<< HEAD

=======
    #imprime
    def __str__(self):
        return '['+'Producto: '+str(self.nombre)+', '+'Tipo: '+str(self.tipo)+', '+'Precio: '+str(self.precio)+', '+'Cantidad: '+str(self.cantidad)+', '+'Clave: '+str(self.clave)+']'
>>>>>>> 4e35af4 (Modificaciones Joel)
    #Puedo llamar a la
    def mostrarNombre (self) -> str:
        print(self.nombre)

<<<<<<< HEAD
    # def __eq__(self:object, other:object) -> bool:
    #     if (self.nombre == other.nombre) and (self.marca == self.marca):
    #         return True
    #     else:
    #         return False
        
    # def __add__(self:object, other:object)->int:
    #     return self.cantidad + other.cantidad

class Snack(Producto):
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
=======
class Snack(Producto):
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
>>>>>>> 4e35af4 (Modificaciones Joel)
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)
    def mostrarNombre(self):
        super().mostrarNombre()
    
class Jugo(Producto):
<<<<<<< HEAD
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
=======
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
>>>>>>> 4e35af4 (Modificaciones Joel)
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)
    def mostrarNombre(self):
        super().mostrarNombre()

class Refresco(Producto):
<<<<<<< HEAD
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
=======
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
>>>>>>> 4e35af4 (Modificaciones Joel)
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)
    def mostrarNombre(self):
        super().mostrarNombre()

class Agua(Producto):
<<<<<<< HEAD
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
=======
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
>>>>>>> 4e35af4 (Modificaciones Joel)
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)
    def mostrarNombre(self):
        super().mostrarNombre()
    
class Dulce(Producto):
<<<<<<< HEAD
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
=======
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
>>>>>>> 4e35af4 (Modificaciones Joel)
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)
    def mostrarNombre(self):
        super().mostrarNombre()
    
class Botana(Producto):
<<<<<<< HEAD
    def __init__(self:object,clave:str,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
=======
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
>>>>>>> 4e35af4 (Modificaciones Joel)
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)
    def mostrarNombre(self):
        super().mostrarNombre()

<<<<<<< HEAD

#Parte del código que me permite leer cada atributo de mis productos desde un csv
#separa los atributos y los guarda en una lista que instancio con una clase
# listAux=[]
# listaProductos=[]
# with open('listasProductos.csv','r') as f:
#     datosProductos=f.readlines()
#     for linea in datosProductos:
#         atributos=linea.split(',')
#         listAux=atributos[:len(atributos)]
#         #Realizo una lista de clases instanciadas->objetos
#         nombreClases = listAux[5].rstrip('\n')
#         listaProductos.append(globals()[nombreClases](listAux[0], listAux[1], listAux[2], listAux[3],listAux[4],listAux[5]))

# #     #print(listaProductos) #Parece que imprime la lista de objetos, pero pone la memoria y no sus atributos

# # #Tal cual un objeto puedo llamar a sus atributos de la lista y operar con él y sus métodos.
# # #Ejemplo:
# # #print(listaProductos[1].nombre)
# for x in range(0,len(listaProductos)):
#     #print(f"CLAVE: {listaProductos[x].clave}, PRODUCTO: {listaProductos[x].nombre},{listaProductos[x].marca}, PRECIO: {listaProductos[x].precio}")
#     print(listaProductos[x].__str__)
# #Posibles errores, que pongan un enter o les falte un dato en la lista de productos, tenerlo en cuenta, o se pasen
=======
>>>>>>> 4e35af4 (Modificaciones Joel)

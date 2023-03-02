class Producto():
    '''La clase Productos crea y define los parametros de un producto.
    
    Identifica el tipo (str) de un producto, entiendase esto como [bebida, refrescos,
    snacks, comida, dulce], recibe su nombre (str), su marca (str), su precio [float],
    la cantidad de ese producto[int] y su clave (str).

    Crea diccionarios con las listas de los productos.
    '''
    def __init__(self:object,tipo:str,nombre:str,marca:str,precio:float,cantidad:int,clave:str) -> None:
        self.tipo=tipo
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        self.__cantidad=cantidad
        self.clave=clave

    def mostrarProducto(self):
        print(self.nombre)

    #def sumarRecaudación(self):




# diccionario={}
# listaAux=[]

# with open('prueba.csv','r') as f:
#     contenido=f.readlines()
#     for linea in contenido:
#         palabras=linea.split(',')
#         listaAux=palabras[:len(palabras)] #':' indica limites
#         diccionario[listaAux[0]]=listaAux[1:len(listaAux)]
#     print(diccionario)

#with open('prueba2.csv','w+') as f:
    #f.write('Hola Mundo\ndesde python')
class Producto():
    '''La clase Productos crea y define los parametros de un producto.
    
    Identifica el tipo (str) de un producto, entiendase esto como [agua, refresco, jugo,
    snacks, botana, dulce], recibe su clave (str), su nombre (str), su marca (str), 
    su precio (float) y la cantidad de ese producto(int)

    Imprime los atributos de cada producto.
    '''
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        self.tipo=tipo
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        self.cantidad=cantidad
        self.clave=clave

    #imprime la lista de atributos
    def __str__(self):
        return '['+'Producto: '+str(self.nombre)+', '+'Tipo: '+str(self.tipo)+', '+'Precio: '+str(self.precio)+', '+'Cantidad: '+str(self.cantidad)+', '+'Clave: '+str(self.clave)+']'

class Snack(Producto):
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)
    
class Jugo(Producto):
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)

class Refresco(Producto):
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)

class Agua(Producto):
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)
   
class Dulce(Producto):
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)
  
class Botana(Producto):
    def __init__(self:object,clave:int,nombre:str,marca:str,precio:float,cantidad:int,tipo:str) -> None:
        super().__init__(clave,nombre,marca,precio,cantidad,tipo)

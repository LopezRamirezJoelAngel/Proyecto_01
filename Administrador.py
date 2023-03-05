"""Ayúdame con una clase de administrador que solo
Ingrese y quite productos y retire el dinero """

"""La clase Administrador se encarga de agregar y eliminar productos de nuestro carrito de compra, también de debitar 
el dinero disponible en nuestra cuenta."""
"""Utiliza como base""" 
"""El producto si quieres solo decláralo así por ejemplo 
Método del administrador ocupa un producto pero solo déjalo decorado ya con lo de chema yo lo junto"""

class Administrador:

    def __init__(self, product: str, cost: float, quantity: int, balance: float):

        self.product = '' #Lee de un archivo solo los nombres de los productos
        self.cost = 0 #Lee de un archivo solo los precios de los productos
        self.quantity = 0
        self.balance = 0
    """def seleccionar_bebida(self, bebida):
        if bebida in self.bebidas:
            if self.total_recaudado >= self.bebidas[bebida]:
                self.total_recaudado -= self.bebidas[bebida]
                self.bebida_vendida = bebida
                print(f"Ha seleccionado {bebida}. ¡Gracias por su compra!")
            else:
                print(f"No tiene suficiente dinero para comprar {bebida}")
        else:
            print("La bebida seleccionada no está disponible")
        self.bebidas = {"Coca Cola": 2.5, "Sprite": 2.5, "Agua": 1.5}
        #YA"""

    
    def aviso(self):
        #Pedrile por teclado que ingrese el producto 
        return 'El producto {} tiene un costo de: {}'.format(self.product, self.cost)
        
    def add_money(self, money):
        self.balance = money
        #Pedirle que ingrese el dinero
        return 'Ha ingresado ${}'.format(self.balance)
    
    def add_2cart(self, resumen, prev):
        prev = (self.cost * self.quantity)
        resumen = (self.balance - prev)
        print ('Ha agregado a su carrito la cantidad de: {} de {}.\nEl total a pagar: ${}\nSu saldo actual es de: ${}'.format(self.quantity, self.product, prev, self.balance))
        while (1):
            if (self.balance - prev >= 0):
                return 'Su cambio: ${},\nGracias'.format(resumen)
                break
            else:
                return 'Efectivo insuficiente para el producto o cantidad seleccionados'
                continue
    
    def remove_fromcart(self):
        prev = ()

    """class MaquinaExpendedora:
    def __init__(self):
        self.bebidas = {"Coca Cola": 2.5, "Sprite": 2.5, "Agua": 1.5}
        self.moneda_aceptada = [1, 5, 10]
        self.total_recaudado = 0
        self.bebida_vendida = ""
         #YA

    def mostrar_bebidas(self):
        print("Bebidas disponibles:")
        for bebida, precio in self.bebidas.items():
            print(f"{bebida} - {precio} euros")
        #YA

    def insertar_moneda(self, moneda):
        if moneda in self.moneda_aceptada:
            self.total_recaudado += moneda / 100
            print(f"Moneda de {moneda / 100} euros insertada")
        else:
            print("La moneda insertada no es aceptada por la máquina expendedora")
        #YA
        
    def seleccionar_bebida(self, bebida):
        if bebida in self.bebidas:
            if self.total_recaudado >= self.bebidas[bebida]:
                self.total_recaudado -= self.bebidas[bebida]
                self.bebida_vendida = bebida
                print(f"Ha seleccionado {bebida}. ¡Gracias por su compra!")
            else:
                print(f"No tiene suficiente dinero para comprar {bebida}")
        else:
            print("La bebida seleccionada no está disponible")
        #YA

    def mostrar_cambio(self):
        if self.bebida_vendida:
            print(f"Su cambio es {self.total_recaudado} euros")
        else:
            print("No se ha realizado ninguna compra todavía")
        #YA

    def recaudacion_total(self):
        print(f"Total recaudado: {self.total_recaudado} euros")
"""


        



"""La clase Administrador se encarga de agregar y eliminar productos de nuestro carrito de compra, también de debitar 
el dinero disponible en nuestra cuenta."""

#Vamos a utlizar los métodos definidios de nuestra clase Producto
from Menu import Menu

class Administrador(Menu):

    #Alguno de estos atributos y métodos los definí en inglés para no confundirme
    def __init__(self, clave, nombre, precio, quantity: int, balance: float):
        super().__init__(clave, nombre, precio)

        self.quantity = quantity
        self.balance = balance
    
    def aviso(self):
        #Pedir por teclado que ingrese el producto 
        return 'El producto {} tiene un costo de: ${}'.format(super().nombre, super().precio)
        
    def add_money(self, money):
        self.balance = money
        #Pedirle que ingrese el dinero
        return 'Ha ingresado ${}'.format(self.balance)
    
    def add_2cart(self, resumen, prev):
        prev = (super().precio * self.quantity)
        resumen = (self.balance - prev)
        print ('Ha agregado a su carrito la cantidad de: {} de {}.\nEl total a pagar: ${}\nSu saldo actual es de: ${}'.format(self.quantity, super().nombre, prev, self.balance))
        while (1):
            if (self.balance - prev >= 0):
                return 'Su cambio: ${},\nGracias'.format(resumen)
                break
            else:
                return 'Efectivo insuficiente para el producto o cantidad seleccionados'
                continue
    
    def remove_fromcart(self):
        print('Vuelva pronto')
        return 0

"""def insertar_moneda(self, moneda):
        if moneda in self.moneda_aceptada:
            self.total_recaudado += moneda / 100
            print(f"Moneda de {moneda / 100} insertada")
        else:
            print("La moneda insertada no es aceptada por la máquina expendedora")
        #YA
"""
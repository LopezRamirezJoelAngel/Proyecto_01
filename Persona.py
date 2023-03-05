from Estrcutura_ListaDobleCircular import *
from Productos import *
from abc import ABC, abstractmethod

class Persona(ABC):
    '''La clase persona puede ser un administrador o usuario normal que realizara distintas tareas pero en esencia es una persona
    '''

    @abstractmethod
    def ModificarProducto(self:object,ListaCircularDoble:object):
        pass

    @abstractmethod
    def SacarDinero(self):
        pass

    @abstractmethod
    def Comprar(self:object,ListaCircularDoble:object):
        pass

class Administrador(Persona):

    """La clase Administrador se encarga de agregar y eliminar productos de nuestro carrito de compra, también de debitar 
    el dinero disponible en nuestra cuenta."""
    """Utiliza como base""" 
    """El producto si quieres solo decláralo así por ejemplo 
    Método del administrador ocupa un producto pero solo déjalo decorado ya con lo de chema yo lo junto"""


    def __init__(self:object,clave:int,nombre:str,):
        self.clave=clave
        self.nombre=nombre
    
    def quitarProducto(self,listaxd):
        x=int(input('Que producto deseas quitar?: '))
        x=x-1
        return listaxd.remove(x)
    def ModificarProducto(self,listaxd):
        op=int(input('Deseas agregar o aumentar productos?: '))
        if op == 1:
            if listaxd.tamaño<15:
                a=str(input('Clave del producto: '))
                b=str(input('Nombre del producto: '))
                c=str(input('Marca del producto: '))
                d=float(input('Precio del producto: '))
                e=int(input('Cantidad: '))

                print("1.Snack \n2.Jugo \n3.Refresco \n4.Agua \n5.Dulce \n6.Botana")
                var=int(input('Elige el tipo de producto de los 6 existentes: '))
                if var == 1:
                    p1=Snack(a,b,c,d,e,'Snack')
                    listaxd.append(p1)
                elif var== 2:
                    p2=Jugo(a,b,c,d,e,'Jugo')
                    listaxd.append(p2)
                elif var== 3:
                    p3=Refresco(a,b,c,d,e,'Refresco')
                    listaxd.append(p3)
                elif var== 4:
                    p4=Agua(a,b,c,d,e,'Agua')
                    listaxd.append(p4)
                elif var== 5:
                    p5=Dulce(a,b,c,d,e,'Dulce')
                    listaxd.append(p5)
                elif var== 6:
                    p6=Botana(a,b,c,d,e,'Botana')
                    listaxd.append(p6)
                else:
                    print('ERROR')
            else:
                print('La expendedora esta en su limite')
        elif op == 2:
            y=int(input('Que producto deseas aumentar?'))
            produc=listaxd.get(y)
            cant=int(input('Cuantos productos vas aumentar?'))
            produc.cantidad=cantidad+cant
            listaxd.update(y,produc)
        else:
            print('NO VALIDA')
    
    def SacarDinero(self):
        x=float(input('Cuanto dinero vas a sacar?: '))
        with open('dinero.txt') as f:
                lineas= f.readlines()
                for line in lineas:
                    dinerillo=float(line.rstrip())
                    break
        if x<dinerillo and dinerillo>=1000:
            dinerillo=dinerillo-x
            wrt= open("dinero.txt", "w")
            wrt.write(str(dinerillo))
            wrt.close()
        else:
            print('Nos dejaras en vanca rota')

    def Comprar(self:object,ListaCircularDoble:object):
        pass
    

class Usuario():
    def __init__(self,clave: float,nombre: str):
        super().__init__(clave,nombre)

    def Comprar(self,listaxd):
        y=int(input('ingresa tu dinero'))
        x=str(input('Clave del producto'))
        produc=listaxd.get(x)
        if y > produc.precio and produc.cantidad!=0:
            cambio = dinero - produc.precio
            produc.cantidad = produc.cantidad-1
            listaxd.update(x,produc)
            with open('dinero.txt') as f:
                lineas= f.readlines()
                for line in lineas:
                    dinerillo=float(line.rstrip())
                    dinerillo = dinero + produc.precio - cambio
                    break
            wrt= open("dinero.txt", "w")
            wrt.write(dinerillo)
            wrt.close()
        else:
            print('No te alcanza')
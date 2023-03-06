from Estrcutura_ListaDobleCircular import *
from Productos import *
from abc import ABC, abstractmethod

class Persona(ABC):
    '''La clase persona es una clase abstracta que define los métodos
    de lo que puede ser un administrador o usuario normal que realizara 
    las tareas de modificar, sacar dinero o comprar.
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

    """La clase Administrador se encarga de agregar y eliminar productos de nuestro carrito de compra, 
    también de debitar las trasacciones.
    Tiene como atributos la clave(str) y el nombre del admin (str).
    Analiza el dinero disponible en nuestra cuenta y perimte sacar el dinero siempre y cuando deje algo
    disponible para dar cambio.
    """
    def __init__(self:object,clave:str,nombre:str,):
        self.clave=clave
        self.nombre=nombre
    #
    def quitarProducto(self,listaxd):
        print(listaxd)
        x=int(input('Que producto deseas quitar?: '))
        x=x-1
        return listaxd.remove(x)
    
#Clase que agrega o aumenta la cantidad de productos hasta un limite de 16
    def ModificarProducto(self,listaxd):
        op=int(input('Deseas 1. agregar o 2. aumentar productos?: '))
#método para llenar de un producto la maquina, recibe sus 5 atributos base y seleciona el tipo
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
#Aumenta la cantidad de un producto en la maquina
        elif op == 2:
            print(listaxd)
            y=int(input('Que producto deseas aumentar?'))
            produc=listaxd.get(y)
            cant=int(input('Cuantos productos vas aumentar?'))
            produc.cantidad=produc.cantidad+cant
            listaxd.update(y,produc)
        else:
            print('NO VALIDA')
#Metodo para leer el dinero que se almacena despues de las compras, lo muestra y saca cuando es
    def SacarDinero(self):
        x=float(input('Cuanto dinero vas a sacar?: '))
        with open('dinero.txt') as f:
                lineas= f.readlines()
                for line in lineas:
                    dinerillo=float(line.rstrip())
                    break
#Condicion para que la maquina no esté vacia y pueda regresar cambio
        if x<dinerillo and dinerillo>=1000:
            dinerillo=dinerillo-x
#Abre el archivo donde se alamacena el dinero recaudado y modifica cuando sobra de lo que se retiró.
            wrt= open("dinero.txt", "w")
            wrt.write(str(dinerillo))
            wrt.close()
        else:
            print('Nos dejaras en banca rota')
    def Comprar(self:object,ListaCircularDoble:object):
        pass

class Usuario(Persona):
    '''La clase usuario hereda de Persona el método de comprar, donde hace
    una validación de ingreso de costos en la moneda Mexicana. Verifica que
    alcance el dineo para el producto seleccionado y regresa cambio. 
    Tiene los mismos atributos, la clave(str) del producto y un nombre(str).
    '''
    def __init__(self:object,clave:str,nombre:str,):
        self.clave=clave
        self.nombre=nombre
    
    def Comprar(self,listaxd: ListaCircularDoble):
        produc=listaxd.get(self.clave)
        print(produc.valor)
        sumapesos=0
        y=0
        while(sumapesos==0):
            m=int(input('ingresa tu dinero'))
            y=y+m
            sumapesos=int(input('Seguir ingresando dinero?: 0.SI 1.NO'))
        ProductoAux=produc.valor
        if y > ProductoAux.precio and ProductoAux.cantidad!=0:
            cambio =y- ProductoAux.precio
            ProductoAux.cantidad = ProductoAux.cantidad-1
            produc.valor=ProductoAux
            listaxd.update(self.clave,produc.valor)
            print(ProductoAux.precio)
            print(listaxd)
            dinerillo=0
            with open('dinero.txt') as f:
                lineas= f.readlines()
                for line in lineas:
                    dinerillo=float(line.rstrip())
                    print(dinerillo)
                    dinerillo = dinerillo+y+ ProductoAux.precio - cambio
                    break
            wrt= open("dinero.txt", "w")
            wrt.write(str(dinerillo))
            wrt.close()
        else:
            print('No te alcanza')

    def ModificarProducto(self:object,ListaCircularDoble:object):
        pass

    def SacarDinero(self):
        pass
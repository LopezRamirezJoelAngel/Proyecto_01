from Productos import *
from Persona import *
import os
import pickle

#funcion main
while(1):
    print("-------BIENVENIDO A LA EXPENDEDORA------\n",
    "¿Que desea hacer?\n",
    "1.Comprar(Usuario).\n",
    "2.Ingresar como administrador.\n",
    "3.Apagar.")
    opcion=int(input("Ingresa tu opcion: "))
    if(opcion==1):
        validacion= os.path.isfile('ListaProductos.pickle')
        if validacion == False:
            print('No hay productos')
        else:
            with open("ListaProductos.pickle", "rb") as f:
                ListaProductos = pickle.load(f)
                print(ListaProductos)
                opcionCompra=int(input('Ingresa el numero del producto: '))
                opcionCompra=opcionCompra-1
                usuario=Usuario(opcionCompra,'DEFAULT')
                usuario.Comprar(ListaProductos)
                with open("ListaProductos.pickle","wb") as f:
                    pickle.dump(ListaProductos,f)
        

    elif(opcion==2):
        #funciones de administrador
        #Ejemplos, ver cuanto dinero tiene la maquina
        #conteo de las ventas
        #agregar/eliminar productos
        contraseña=int(input("Bienvenido. Ingrese la contraseña para continuar: "))
        a=0
        with open('admin.txt') as f:
            lineas= f.readlines()
            for line in lineas:
                if a==0:
                    nombre=str(line.rstrip())
                    a=a+1
                elif a==1:
                    apellido=str(line.rstrip())
                    a=a+1
                elif a==2:
                    password=int(line.rstrip())
                    break
        nom=nombre + ' ' + apellido
        if contraseña == password:
            Adminxd=Administrador(password,nom)
            print(Adminxd.nombre)
            print(Adminxd.clave)
            print('1. Modificar expendedora\n2. Sacar dinero')
            x=int(input('Ingresa una opcion: '))
            if x==1:
                validacion= os.path.isfile('ListaProductos.pickle')
                if validacion == False:
                    print('Iniciando lista')
                    ListaProductos= ListaCircularDoble()
                    p=int(input('Quieres 1.eliminar o 2.agregar productos?: '))
                    if p==1:
                        ListaProductos=Adminxd.quitarProducto(ListaProductos)
                    elif p==2:
                        Adminxd.ModificarProducto(ListaProductos)
                    print(ListaProductos)
                    with open("ListaProductos.pickle","wb") as f:
                        pickle.dump(ListaProductos,f)
                else:
                    with open("ListaProductos.pickle", "rb") as f:
                        ListaProductos = pickle.load(f)
                        p=int(input('Quieres 1.eliminar 2.agregar productos?: '))
                        if p==1:
                            ListaProductos=Adminxd.quitarProducto(ListaProductos)
                        elif p==2:
                            Adminxd.ModificarProducto(ListaProductos)
                        print(ListaProductos)
                        with open("ListaProductos.pickle","wb") as f:
                            pickle.dump(ListaProductos,f)
            elif x==2:
                Adminxd.SacarDinero()
        else:
            print('No autorizado')

    elif(opcion==3):
        print("APAGANDO...")
        break
    else:
        print("No entiendo lo que trata de hacer...")
    

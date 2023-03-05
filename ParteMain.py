from Productos import *
<<<<<<< HEAD


#funcion main
while(1):
    print("-------BIENVENIDO A LA EXPENDEDORA------\n\
¿Que desea hacer?\n1.Comprar(Usuario).\n2.Ingresar como administrador.\n3.Apagar.")
=======
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
>>>>>>> 4e35af4 (Modificaciones Joel)
    opcion=int(input("Ingresa tu opcion: "))
    if(opcion==1):
        listAux=[]
        listaProductos=[]
        with open('listasProductos.csv','r') as f:
            datosProductos=f.readlines()
            for linea in datosProductos:
                atributos=linea.split(',')
                listAux=atributos[:len(atributos)]
                #Realizo una lista de clases instanciadas->objetos
                nombreClases = listAux[5].rstrip('\n')
                listaProductos.append(globals()[nombreClases](listAux[0], listAux[1], listAux[2], listAux[3],listAux[4],listAux[5]))

        #Imprime esos atributos de un objeto
        for x in range(0,len(listaProductos)):
            print(f"CLAVE: {listaProductos[x].clave}, PRODUCTO: {listaProductos[x].nombre},{listaProductos[x].marca}, PRECIO: {listaProductos[x].precio}")

        #Para sólo imprimir los de un tipo debería hacer lo de abajo pero con .tipo y el tipo que ingrese
        seleccion=str(input("¿Que productos, quiere comprar?. Ingrese la clave: "))
        for x in range(0,len(listaProductos)):
            if(listaProductos[x].clave==seleccion):  #Se puede poner una excepcion sobre sólo 2 caracteres por meter
                print("ingresa el monto del producto") #poner tal vez una función que sólo permita nuestras monedas y regrese el cambio
            #else:
                #print("No hay ningun producto con esa clave")   TENER CUIDADO, imprime muchos, considerar 1


    elif(opcion==2):
<<<<<<< HEAD
        print("Bienvenido. Ingrese la contraseña para continuar: ")
        #funciones de administrador
        #Ejemplos, ver cuanto dinero tiene la maquina
        #conteo de las ventas
        #agregar/eliminar productos
=======
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
                    p=int(input('Quieres agregar o eliminar productos?: '))
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
                        p=int(input('Quieres agregar o eliminar productos?: '))
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
>>>>>>> 4e35af4 (Modificaciones Joel)

    elif(opcion==3):
        print("APAGANDO...")
        break
    else:
        print("No entiendo lo que trata de hacer...")
    

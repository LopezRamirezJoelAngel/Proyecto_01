from Productos import *
from Persona import *
import os
import pickle
#numeros menu
def ingresaNumero(a:str):
    try:
        opcion=int(input(a))
    except:
        print('solo se ingresa numeros')
        opcion=ingresaNumero(a)
    else:
        print('Dato correcto')
    return opcion 

#str
def ingresaString(b:str):
    try:
        opcion=str(input(b))
    except:
        print('solo se ingresa caracteres')
        opcion=ingresaNumero(b)
    else:
        print('Dato correcto')
    return opcion 

#funcion main
while(1):
    print("-------BIENVENIDO A LA EXPENDEDORA------\n",
    "¿Que desea hacer?\n",
    "1.Comprar(Usuario).\n",
    "2.Ingresar como administrador.\n",
    "3.Apagar.\n",
    "4. Imprimir tipo de producto por tipo\n",)
    opcion=ingresaNumero("Ingresa tu opcion: ")
    if(opcion==1):
        validacion= os.path.isfile('ListaProductos.pickle')
        if validacion == False:
            print('No hay productos')
        else:
            with open("ListaProductos.pickle", "rb") as f:
                ListaProductos = pickle.load(f)
                print(ListaProductos)
                opcionCompra=ingresaNumero("Ingresa el numero del producto: ")
                opcionCompra=opcionCompra-1
                usuario=Usuario(opcionCompra,'DEFAULT')
                usuario.Comprar(ListaProductos)
                with open("ListaProductos.pickle","wb") as f:
                    pickle.dump(ListaProductos,f)
        

    elif(opcion==2):
        contraseña=ingresaNumero("Bienvenido. Ingrese la contraseña para continuar: ")
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
            x=ingresaNumero("Ingresa una opcion: ")
            if x==1:
                validacion= os.path.isfile('ListaProductos.pickle')
                if validacion == False:
                    print('Iniciando lista')
                    ListaProductos= ListaCircularDoble()
                    p=ingresaNumero("Quieres 1.eliminar o 2.agregar productos?: ")
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
                        p=ingresaNumero("Quieres 1.eliminar 2.agregar productos?: ")
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
    elif(opcion==4):
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]
        validacion= os.path.isfile('ListaProductos.pickle')
        if validacion == False:
            print('No hay productos')
        else:
            with open("ListaProductos.pickle", "rb") as f:
                ListaProductos = pickle.load(f)
                for i in range(0,ListaProductos.tamaño):
                    produc=ListaProductos.get(i)
                    ProductoAux=produc.valor
                    if ProductoAux.tipo == 'Snack':
                        list1.append(ProductoAux)
                    elif ProductoAux.tipo == 'Jugo':
                        list2.append(ProductoAux)
                    elif ProductoAux.tipo == 'Refresco':
                        list3.append(ProductoAux)
                    elif ProductoAux.tipo == 'Agua':
                        list4.append(ProductoAux)
                    elif ProductoAux.tipo == 'Dulce':
                        list5.append(ProductoAux)
                    elif ProductoAux.tipo == 'Botana':
                        list6.append(ProductoAux)
        print("1.Snack \n2.Jugo \n3.Refresco \n4.Agua \n5.Dulce \n6.Botana")
        tipoProducto=ingresaNumero("Ingresa el tipo de producto: ")
        if tipoProducto == 1:
            if len(list1) != 0:
                for i in list1:
                    print(i)
            else:
                print('No hay productos')
        if tipoProducto == 2:
            if len(list2) != 0:
                for i in list2:
                    print(i)
            else:
                print('No hay productos')
        if tipoProducto == 3:
            if len(list3) != 0:
                for i in list3:
                    print(i)
            else:
                print('No hay productos')
        if tipoProducto == 4:
            if len(list4) != 0:
                for i in list4:
                    print(i)
            else:
                print('No hay productos')
        if tipoProducto == 5:
            if len(list5) != 0:
                for i in list5:
                    print(i)
            else:
                print('No hay productos')
        if tipoProducto == 6:
            if len(list6) != 0:
                for i in list6:
                    print(i)
            else:
                print('No hay productos')
                
    else:
        print("No entiendo lo que trata de hacer...")
    

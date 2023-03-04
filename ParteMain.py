from Productos import *


#funcion main
while(1):
    print("-------BIENVENIDO A LA EXPENDEDORA------\n\
¿Que desea hacer?\n1.Comprar(Usuario).\n2.Ingresar como administrador.\n3.Apagar.")
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
        print("Bienvenido. Ingrese la contraseña para continuar: ")
        #funciones de administrador
        #Ejemplos, ver cuanto dinero tiene la maquina
        #conteo de las ventas
        #agregar/eliminar productos

    elif(opcion==3):
        print("APAGANDO...")
        break
    else:
        print("No entiendo lo que trata de hacer...")
    

from Menu import Menu

# Crea una instancia de la clase Menu con el archivo CSV que contiene el menú
menu = Menu('listasProductos.csv')


menu.seleccion()

clave = input("Ingrese la clave del producto que desea: ")
encontrado = menu.busqueda(clave)

while (1):
    if encontrado is not None:
        print(encontrado)
        break
    else:
        print(f"No se encontró el producto con clave {clave}")
        break
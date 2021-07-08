def guarda_producto(nombre, precio, archivo):
    info = "Producto:" + nombre + " Precio:" + str(precio) +"\n"
    archivo.write(info)


def caja():
    total = 0
    with open("recibo.txt", "w") as archivo:
        while True:
            nombre, precio = input("Ingrese nombre y precio del producto: ").split()
            precio = float(precio)
            total += precio
            guarda_producto(nombre, precio, archivo)
            ctrl = input("Desea agregar mas prodcutos: ").upper()
            if ctrl == 'NO':
                print("Gracias por su compra")
                info2 = "Total a pagar:" + str(total)
                archivo.write(info2)
                break




caja()

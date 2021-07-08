import os


def limpiarConsola():
    # definimos el comando a ejecutar en la consola
    command = 'clear'
    # ejecutamos el comando en consola
    os.system(command)


def arreglo(filas, columnas):
	matrix = []
	for i in range(filas):
		matrix.append([])
		for j in range(columnas):
			aux = int(input(f'ingrese dato el dato ([{i+1}] [{j+1}]): '))
			matrix[i].append(aux)
	return  matrix


def actividad2():
    # pedimos una matriz y la imprimimos
    fila, columna = input("ingrese las dinemsiones de la matris que desea (fila columna): ").split()
    fila    = int(fila)
    columna = int(columna)
    matriz  = arreglo(fila , columna)

    print("\nMatriz Ingresada")
    for i in range(len(matriz)):
        print(matriz[i])
    print("==="*6)

    # imprimimos la primera fila
    print("-Primera Fila")
    for i in range(len(matriz)):
        print(f"Posicion [{i+1}][1]:",matriz[i][0])
    print("==="*6)

    # imprimimos la primera columna
    print("-Primera Columna")
    for i in range(len(matriz)):
        print(f"Posicion [1][{i+1}]:", matriz[0][i])
    print("==="*6)

    # imprimimos una posicion en particular
    f,c = input('¿Que posicion desea imprimir? (fila columna) : ').split()
    f = int(f)
    c = int(c)
    # restamos 1 por si el usuario quiere ingresar directamente [3,3] o [1,1]
    print(f"El valor en la posicion [{f},{c}] es: ",matriz[f-1][c-1])


# linpiamos pantalla antes de ejecutar la actividad 2
limpiarConsola()
# corremos la actividad 2
actividad2()
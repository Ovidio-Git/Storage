import numpy as np


def Funtion(x):						
	return np.exp(x) + (x**3) - 5 # se define la funcion predefinidad para el problema


def Funtionderivate(x):
	return np.exp(x) + 3*(x**2)	  # derivada de la funcion anteriormente definida


def newton_raphson(e=None):       # implementacion del metodo Newthon Raphson
	y = 0
	
	if e == None:
		memory = []
		for i in range (100):     # implementacion de la primera parte, donde se debe usar un ciclo for
			x = y				  # para la implemetacion y = xi y x = xi-1
			y = x - (Funtion(x) / Funtionderivate(x)) 
			memory.append(y)
		print('=='*40)
		print(np.array(memory)) 
		print('=='*40)
	
	elif e != None:				  # implementacion de la segunda parte donde se debe usar un ciclo while
		i = 0
		while True:
			i += 1
			x = y
			y = x - (Funtion(x) / Funtionderivate(x))			
			if np.absolute(x-y) < e: # evaluacion de la condicion |Xi - Xi-1| < e 
				print(f'\n                Numero de interaciones (i) = {i}\n                Ultimo valor de xi = {y}')
				break


def run():
	menu = int(input("""
		¿Que modo desea utilizar?

		[1] For sin evaluar desigualdad |Xn - Xn-1| < e
		[2] While y evaluar la desigualdad

		--> """))

	if menu == 1:
		newton_raphson()
	elif menu == 2:
		e = float(input(' '*16+'Ingrese el valor de epciolon: '))
		newton_raphson(e)
	else:
		print(" "*16+"Opcion no permitida")


if __name__ == '__main__':
	run()

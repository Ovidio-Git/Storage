def average(total, cantidad):
	return total/cantidad


def standart_desviation(numeros, average, n):
	sum = 0
	for i in range(0,n):
		sum += (numeros[i]-average)**2
		print(f'{numeros[i]}-{average} ** 2 = {sum}')
	return (sum/(n-1))**1/2


def run():
	cantidadnum = int(input('Cuantos nuemeros desea ingresar: '))
	numeros = []
	total = 0
	for i in range(0,cantidadnum):
		n = int(input(f'Ingrese su dato numero {i+1} = '))
		total += n
		numeros.append(n)

	media = average(total, cantidadnum)
	print(f'La media de los valores ingresados es {media}')
	print(f'La desviacion estandar de los numeros ingresados es {standart_desviation(numeros,media,cantidadnum)}')


if __name__ == '__main__':
	run()

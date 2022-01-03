def triangle(a, b, c):
	if a == b and b == c:
		print('Su triangulo es equilatero')
		quit()  # funcion para terminar  el programa
	if a != b and b != c and c != a:
		print('Su triangulo es escaleno')
	if a == b or b == c or a == c:
		print('Su triangulo es isoceles') 


def run():
	print('Por favor ingrese los valores de los angulos de un triangulo')
	a = int(input('Angulo 1 -> '))
	b = int(input('Angulo 1 -> '))
	c = int(input('Angulo 1 -> '))
	if (a+b+c) == 180 :
		triangle(a,b,c)
	else:
		print('Error valor de angulo no permitido')

if __name__ == '__main__':
	run()

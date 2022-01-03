
def pi():

	a = 2
	b = 3
	c = 4
	dato = 3

	for i in range(1, 16):
		aprox = 4/(a*b*c)
		if i%2 == 0:
			dato -= aprox
		else:
			dato += aprox
		a += 2
		b += 2
		c += 2
		print(f'En la aproximacion numero {i} el valor de pi es: {dato}')


def run():
	pi()



if __name__ == '__main__':
	run()

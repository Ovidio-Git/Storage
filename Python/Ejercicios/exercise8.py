
# Escriba un programa que de cómo resultado un archivo de texto 
# que muestre todas las combinaciones de multiplicación de los
# número 1 hasta 10.

def run():

	with open('matriz_8.txt', 'w') as matrix:
		for i in range(1,11):
			matrix.write(f' {i}x1={i*1}\n {i}x2={i*2}\n {i}x3={i*3}\n {i}x4={i*4}\
			\n {i}x5={i*5}\n {i}x6={i*6}\n {i}x7={i*7}\n {i}x8={i*8}\n {i}x9={i*9}\
		    \n {i}x10={i*10}\n\n')




if __name__ == '__main__':
	run() 

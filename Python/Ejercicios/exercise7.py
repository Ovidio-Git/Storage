



def calendar(num,year):


	data = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'noviembre', 12:'Diciembre'}
	dias = {1:'31', 2:'28', 3:'31', 4:'30', 5:'31', 6:'30', 7:'31', 8:'31', 9:'30', 10:'31', 11:'30', 12:'31'}

	if (year%4 == 0 or year%400 ==0) and year%100 != 0:
		dias[2]='29'

	print(f'El mes ingresado corresponde a {data[num]} y tiene {dias[num]} dias')


def run ():

	print('Ingrese un mes y un año deseado')
	meses = int(input('Ingrese el mes (numero 1 al 12) -> '))
	year = int(input('Ingrese el año -> '))
	calendar(meses,year)




if __name__ == '__main__':
	run()

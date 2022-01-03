def decorador(hello):
	def auxiliar():
		correcta = 453
		while True:
			contrasena = int(input('Ingrese contraseña: '))
			if contrasena == correcta:
				return hello()
			else:
				print('¡Contraseña inconrrecta!')
	return auxiliar  # Segun el modelo de los decoradores
					 # siempre se retorna la funcion interna


@decorador  #esto es lo mismo que decorador(hola())
def hola():
	nom = input('Ingrese su nombre: ')
	print(f'¡Hola {nom}!')


def run():
	hola()


if __name__ == '__main__':
	run()

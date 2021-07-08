
def proceso(ayunas, glucosa):
    if (ayunas == 'si') and (glucosa < 0.44):
        print("hipoglusemia")
    elif (ayunas == 'si') and (0.44 > glucosa or glucosa < 0.61):
        print("normal")
    elif (ayunas == 'si') and (0.61 > glucosa or glucosa < 0.7):
        print("elevado")
    elif (ayunas == 'si') and (glucosa >= 0.7):
        print("diabetes")
    elif (ayunas == 'no') and (glucosa < 0.78):
        print("normal")
    elif (ayunas == 'no') and (0.78 > glucosa or glucosa < 1.1):
        print("elevado")
    elif (ayunas == 'no') and (glucosa > 1.1):
        print("diabetes")
    elif (ayunas != "si") or (ayunas != "no"):
        print("error en los datos")


def run():
    respuesta = input("¿En Ayunas?: ")
    nivel = float(input("Nivel de glucosa en sangre: "))
    proceso(respuesta, nivel)


if __name__=='__main__':
    run()
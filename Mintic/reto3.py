
def inputs():
    sucursales, pacientes = input().split()
    pacientes  = int(pacientes)
    sucursales = int(sucursales)

    # memory
    medicamentos = []
    natendido    = []
    ayunas       = []
    glucosas     = []

    while sucursales < 1:
        sucursales, pacientes = input().split()
        pacientes  = int(pacientes)
        sucursales = int(sucursales)

    for i in range(sucursales):
        medicamento = int(input())
        while medicamento < 1:
            medicamento = int(input())
        medicamentos.append(medicamento)

    for i in range(pacientes):
        atendido, ayuna, glucosa = input().split()
        atendido = int(atendido)
        glucosa  = float(glucosa)
        natendido.append(atendido)
        ayunas.append(ayuna)
        glucosas.append(glucosa)

    proceso(ayunas,glucosas,natendido, medicamentos, pacientes, sucursales)




def proceso(ayunas,glucosas,natendido, medicamentos, pacientes, sucursales):

    medicamentosinicio=medicamentos.copy()
    for i in range(pacientes):
        if   (ayunas[i] == 'si') and (glucosas[i] < 0.44):
            medicamentos[natendido[i]-1] -= 5
        elif (ayunas[i] == 'si') and (0.44 >= glucosas[i] or glucosas[i] < 0.61):
            pass
        elif (ayunas[i] == 'si') and (0.61 >= glucosas[i] or glucosas[i] < 0.7):
            medicamentos[natendido[i]-1] -= 4
        elif (ayunas[i] == 'si') and (glucosas[i] >= 0.7):
            medicamentos[natendido[i]-1] -= 9
        elif (ayunas[i] == 'no') and (glucosas[i] < 0.78):
            pass
        elif (ayunas[i] == 'no') and (0.78 >= glucosas[i] or glucosas[i] < 1.1):
            medicamentos[natendido[i]-1] -= 10
        elif (ayunas[i] == 'no') and (glucosas[i] >= 1.1):
            medicamentos[natendido[i]-1] -= 15
        elif (ayunas[i] != 'si') and (ayunas[i] != 'no') and (natendido[i]<1 or natendido[i]>sucursales):
            pass

    #Sucursal con menor numero de medicamentos y el numero de estos
    print(medicamentos.index(min(medicamentos)) + 1, min(medicamentos))
    #Sucursal con mayor numero de medicamentos y el numero de estos
    print(medicamentos.index(max(medicamentos)) + 1, max(medicamentos) )


    for i in range(sucursales):
        porcentage=float(medicamentos[i] / medicamentosinicio[i])
        data = 1 - porcentage
        print(i+1, "{:.2f}%".format(data*100))

def run():
    inputs()


if __name__=='__main__':
    run()


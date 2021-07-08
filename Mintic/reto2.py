
def inputs():
    medicamento1 = int(input())
    medicamento2 = int(input())
    proceso(medicamento1, medicamento2)


def proceso(medicamento1, medicamento2):

    pacientest = 0
    pacientes1 = 0
    pacientes2 = 0
    ctrl = 0

    while (medicamento2 > 0 and medicamento1 > 0):

        ayunas  = input()
        glucosa = float(input())


        if   (ayunas == 'si') and (glucosa < 0.44):
            pacientest += 1
            medicamento2 -= 5
            if medicamento2 >= 0:
                pacientes2 += 1
        elif (ayunas == 'si') and (0.44 >= glucosa or glucosa < 0.61):
            pacientest += 1
        elif (ayunas == 'si') and (0.61 >= glucosa or glucosa < 0.7):
            pacientest += 1
            medicamento1 -= 4
            pacientes1 += 1
        elif (ayunas == 'si') and (glucosa >= 0.7):
            pacientest += 1
            medicamento1 -= 9
            pacientes1 += 1
        elif (ayunas == 'no') and (glucosa < 0.78):
            pacientest += 1
        elif (ayunas == 'no') and (0.78 >= glucosa or glucosa < 1.1):
            pacientest += 1
            medicamento1 -= 10
            pacientes1 += 1
        elif (ayunas == 'no') and (glucosa >= 1.1):
            pacientest += 1
            medicamento1 -= 15
            pacientes1 += 1
        elif (ayunas != "si") or (ayunas != "no"):
            pacientest += 1
        ctrl = 1


    if ctrl == 1:
        result1=float(pacientes1 / pacientest)
        result2=float(pacientes2 / pacientest)
        print(pacientest)
        print(pacientes1, "{:.2f}%".format(result1*100))
        print(pacientes2, "{:.2f}%".format(result2*100))
    else:
        print(pacientest)
        print(pacientes1,"0.00%")
        print(pacientes2,"0.00%")


def run():
    inputs()


if __name__=='__main__':
    run()


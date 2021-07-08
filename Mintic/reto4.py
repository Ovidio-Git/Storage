def inputs():
    sucursales, medicamentos, pacientes = input().split()
    sucursales  = int(sucursales)
    medicamentos = int(medicamentos)
    while (sucursales < 1 or medicamentos < 1): 
        sucursales, medicamentos, pacientes = input().split()
        sucursales  = int(sucursales)
        medicamentos = int(medicamentos)
    pacientes   = int(pacientes)

    existencias=[]
    base=[]
    for i in range(sucursales):
        process = input().split()
        f = list(process)
        for m in range(len(process)):
            process[m]=int(process[m])
            f[m]=int(f[m])
        existencias.append(process)
        base.append(f)

    infopaciente = []
    for i in range(pacientes):
        nsucu, tipom, dosis, ayunas, glucosa = input().split()
        nsucu = int(nsucu)
        tipom = int(tipom)
        dosis = int(dosis)
        glucosa = float(glucosa)
        infopaciente.append([nsucu, tipom, dosis, ayunas, glucosa])
    proceso(sucursales, medicamentos, pacientes, infopaciente, existencias, base)


def proceso(sucursales, medicamentos, pacientes, db, existencias, original):


    pacientes_atendidos = []
    entregados = []
    prom = 0
    pacientescontar=[]
    cont = 0
    for i in range(sucursales):
        pacientescontar.append(0)

    for i in range(pacientes):
        if   (db[i][3] == 'si') and (db[i][4] < 0.44):
            existencias[db[i][0]-1][db[i][1]-1] -= db[i][2]
            pacientes_atendidos.append([db[i][0], db[i][2]])
            pacientescontar[db[i][0]-1] += 1
        elif (db[i][3] == 'si') and (0.44 >= db[i][4] or db[i][4] < 0.61):
            pacientescontar[db[i][0]-1] += 1

        elif (db[i][3] == 'si') and (0.61 >= db[i][4] or db[i][4] < 0.7):
            pacientescontar[db[i][0]-1] += 1
            existencias[db[i][0]-1][db[i][1]-1] -= db[i][2]
            pacientes_atendidos.append([db[i][0], db[i][2]])
        elif (db[i][3] == 'si') and (db[i][4] >= 0.7):
            pacientescontar[db[i][0]-1] += 1
            existencias[db[i][0]-1][db[i][1]-1] -= db[i][2]
            pacientes_atendidos.append([db[i][0], db[i][2]])
        elif (db[i][3] == 'no') and (db[i][4] < 0.78):
            pacientescontar[db[i][0]-1] += 1
        elif (db[i][3] == 'no') and (0.78 >= db[i][4] or db[i][4] < 1.1):
            pacientescontar[db[i][0]-1] += 1
            existencias[db[i][0]-1][db[i][1]-1] -= db[i][2]
            pacientes_atendidos.append([db[i][0], db[i][2]])
        elif (db[i][3] == 'no') and (db[i][4] >= 1.1):
            pacientescontar[db[i][0]-1] += 1
            existencias[db[i][0]-1][db[i][1]-1] -= db[i][2]
            pacientes_atendidos.append([db[i][0], db[i][2]])
        elif (((db[i][3] != 'si') and (db[i][3] != 'no')) or (db[i][0]<1 or db[i][0]>sucursales) or (db[i][1]<1 or db[i][1]>medicamentos) or (db[i][2]<0)):
            pass 
        
        



    for i in range(len(existencias)):
        entregados.append([])
        for j in range(len(existencias[i])):
            entregados[i].append(original[i][j]-existencias[i][j])

    
    programados=0
    ctrl = 0
    memory=[]
    for i in range(sucursales):
        print(i+1)
        memory.append(entregados[i][0])
        print(existencias[i].index(min(existencias[i])) + 1, min(existencias[i]))
        print(existencias[i].index(max(existencias[i])) + 1, max(existencias[i]))

        for sucursal in range(len(pacientes_atendidos)): 
            if pacientes_atendidos[sucursal][0]==i+1:
                programados += pacientes_atendidos[sucursal][1]
            
        prom = programados/medicamentos
        print("{:.2f}".format(min(entregados[i])),"{:.2f}".format(prom),"{:.2f}".format(max(entregados[i])) ) 

        programados = 0
        if pacientes_atendidos==[]:
            print("0.00")
        else:
            for sucursal in range(len(pacientes_atendidos)): 
                if pacientes_atendidos[sucursal][0]==i+1:
                    programados += pacientes_atendidos[sucursal][1]
                    ctrl += 1
            if programados == 0:
                print("0.00")
            else:
                print("{:.2f}".format(programados/pacientescontar[i]))
                print("Pacientes atendidos:", pacientescontar[i])
                print("Medicamentos programados", programados)
            programados = 0 
        ctrl = 0   

    print(memory.index(min(memory)) + 1, min(memory))
    print(memory.index(max(memory)) + 1, max(memory))


def run(): 
    inputs()


if __name__=='__main__':
    run()
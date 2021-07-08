def desvi(memory, media):
    suma = 0
    for i in range(len(memory)):
        suma += (memory[i]-media)**2
    return (suma/(len(memory)-1))**(1/2)

def inputs():
    target = []
    sucursales = input("Ingrese el umero de sucursales: ").split()
    ctrl = 0
    solicitados =[]
    male_2, male = [],[]
    female_2, female = [], []
    memory, memory_2 = [], []
    total = []
    pacientes_aentregar = []
    pacientes = []
    for i in range(len(sucursales)):
        male.append(0)
        male_2.append(0)
        female_2.append(0)
        female.append(0)
        solicitados.append(0)
        pacientes_aentregar.append(0)
        total.append(0)

    # ordenando los vectores ingresados 
    for i in range(len(sucursales)):
        sucursales[i]=int(sucursales[i])
    sucursales.sort()
    for i in range(len(sucursales)):
        sucursales[i]=str(sucursales[i])


    # abriendo el archivo csv
    with open("data.csv", 'r') as archivo:
        lineas = archivo.read().splitlines()
        lineas.pop(0)

        for j in range(len(sucursales)):
            target.append([])
            pacientes.append([])
            memory.append([])
            memory_2.append([])
            pacientes_aentregar.append([])
            for i in lineas:
                linea = i.split(',')
    
                if linea[5]==sucursales[j]:
                    target[j].append(linea)
                    aentregar = int(linea[7])
                    ayunas = linea[8]
                    glucosa = float(linea[9])
                    
                    if linea[2] == 'm':
                        male[j] += 1
                    elif linea[2] == 'f':
                        female[j] += 1
                    

                    if   (ayunas == 'si') and (glucosa < 0.44):
                        solicitados[j] += aentregar
                        memory[j].append(aentregar)
                        memory_2[j].append(aentregar)
                        pacientes[j].append(linea)
                        pacientes_aentregar[j] += aentregar
                        if linea[2] == 'm':
                            male_2[j] += 1
                        else:
                            female_2[j] += 1
                    elif (ayunas == 'si') and (0.44 >= glucosa or glucosa < 0.61):
                        solicitados[j] += aentregar
                        memory[j].append(aentregar)
                    elif (ayunas == 'si') and (0.61 >= glucosa or glucosa < 0.7):
                        solicitados[j] += aentregar
                        memory[j].append(aentregar)
                        memory_2[j].append(aentregar)
                        pacientes[j].append(linea)
                        pacientes_aentregar[j] += aentregar
                        if linea[2] == 'm':
                            male_2[j] += 1
                        else:
                            female_2[j] += 1
                    elif (ayunas == 'si') and (glucosa >= 0.7):
                        solicitados[j] += aentregar
                        memory[j].append(aentregar)
                        memory_2[j].append(aentregar)
                        pacientes[j].append(linea)
                        pacientes_aentregar[j] += aentregar
                        if linea[2] == 'm':
                            male_2[j] += 1
                        else:
                            female_2[j] += 1
                    elif (ayunas == 'no') and (glucosa < 0.78):
                        solicitados[j] += aentregar
                        memory[j].append(aentregar)
                    elif (ayunas == 'no') and (0.78 >= glucosa or glucosa < 1.1):
                        solicitados[j] += aentregar
                        memory[j].append(aentregar)
                        memory_2[j].append(aentregar)
                        pacientes[j].append(linea)
                        pacientes_aentregar[j] += aentregar
                        if linea[2] == 'm':
                            male_2[j] += 1
                        else:
                            female_2[j] += 1
                    elif (ayunas == 'no') and (glucosa >= 1.1):
                        solicitados[j] += aentregar
                        memory[j].append(aentregar)
                        memory_2[j].append(aentregar)
                        pacientes[j].append(linea)
                        pacientes_aentregar[j] += aentregar
                        if linea[2] == 'm':
                            male_2[j] += 1
                        else:
                            female_2[j] += 1
                    elif (ayunas != 'si') and (glucosa != 'no'):
                        pass
                    if ctrl == len(sucursales):
                        break
    

    for i in range(len(sucursales)):
        print(target[i][0][5], target[i][0][3], target[i][0][4])
        print("patients")
        print("male", male[i])
        print("female", female[i])
        print("total", male[i] + female[i])
        print("medicine quantity")
        media =  solicitados[i]/(male[i] + female[i])
        print("mean", "{:.2f}".format(media))
        print("std", "{:.2f}".format(desvi(memory[i], media)))
        print("min", min(memory[i]))
        print("max", max(memory[i]))
        print("total",  solicitados[i])
        print("scheduled patients")
        print("male", male_2[i])
        print("female",female_2[i])
        print("total", male_2[i] + female_2[i])
        print("scheduled medicine quantity")
        media_2 =  pacientes_aentregar[i]/(male_2[i] + female_2[i])
        print("mean", "{:.2f}".format(media_2))
        print("std", "{:.2f}".format(desvi(memory_2[i], media_2)))
        for j in range(len(pacientes[i])):
            if pacientes[i][j][7] == str(min(memory_2[i])):
                print("min", min(memory_2[i]),pacientes[i][j][0],pacientes[i][j][1],pacientes[i][j][2],pacientes[i][j][6])
                break
        for j in range(len(pacientes[i])):
            if pacientes[i][j][7] == str(max(memory_2[i])):
                print("max", max(memory_2[i]),pacientes[i][j][0],pacientes[i][j][1],pacientes[i][j][2],pacientes[i][j][6])
                break
        print("total", pacientes_aentregar[i])
    


def run(): 
    inputs()


if __name__=='__main__':
    run()
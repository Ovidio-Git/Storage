
def vector():
    n = int(input('Ingrese el tamaño del vector a digitar: '))
    memory = []
    for i in range(n):
        aux = int(input(f'Ingrese el dato numero {i+1} a su vector: '))
        memory.append(aux)
    print(f'\nEl vector ingresado fue: {memory}')
    return memory


def Bubble(vector):
    num = 0
    print('='*33+'Bubble sort'+'='*36)
    for j in range(len(vector)-1):
        for i in range (len(vector)-1):
            if vector[i] > vector [i+1]:
                num += 1
                aux = vector[i]
                vector[i] = vector[i+1]
                vector[i+1] = aux
                print(f'Iteracion numero {num} = {vector} ') 
    print('=='*40)
    print('Resultado vector ordenado: ', vector)

    
def run ():
    aux = vector()
    Bubble(aux)


if __name__ == '__main__':
    run()
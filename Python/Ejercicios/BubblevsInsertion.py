
from time import time

def Bubble(vector):
    num = 0
    global comparaciones2
    print('='*33+'Bubble sort'+'='*36)
    for j in range(len(vector)-1):
        for i in range (len(vector)-1):
            comparaciones2 += 1
            if vector[i] > vector [i+1]:
                num += 1
                aux = vector[i]
                vector[i] = vector[i+1]
                vector[i+1] = aux
                print(f'Iteracion numero {num} = {vector} ') 
   
    print('\nResultado vector ordenado Bubblesort: ', vector)


def selectionSort(vector):
    global comparaciones1
    n = len(vector)
    for i in range(n - 1):
        menor = i
        comparaciones1 += 1
        for j in range(i + 1, n):
            if vector[j] < vector[menor]:
                menor = j
        vector[i], vector[menor] = vector[menor], vector[i]


lista = [36, 1, 76, 21, 73, 9, 30, 40, 66, 10, 4]
comparaciones1 = 0
comparaciones2 = 0

t0 = time()
selectionSort(lista)
t1 = time()

t2 = time()
Bubble(lista)
t3 = time()

timea = t1 - t0
timeb = t3 - t2 
print (f'Tiempo: {timeb} segundos')
print ("Comparaciones:", comparaciones2)


print('='*33+'Selection sort'+'='*36)
print ("\nResultado vector ordenado Selectionsort:",lista)

print (f'Tiempo: {timea} segundos')
print ("Comparaciones:", comparaciones1)

print(f'\nDiferencia Tiempo: {timeb-timea}')
print(f'Diferencia Comparaciones: {comparaciones2-comparaciones1}')






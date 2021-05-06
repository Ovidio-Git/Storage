def comparacion(target):
    base = [i for i in range(101)]
    a = set(base)
    b = set(target)
    c = a.difference(b)
    d = {71,72,73,74,75,76,77,78,79,89,98,100,99,92}
    c = c.difference(d)
    c = list(c)
    print("\n Numeros faltantes")

    for i in range(0,len(c)):
        if c[i] <= 80:
            print(f'Hembra: {c[i]}')
        else: 
            print(f'Macho: {c[i]}')
    print("\n Numeros no puestos")
    print(d)
            
def selectionSort(vector):
    n = len(vector)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if vector[j] < vector[menor]:
                menor = j
        vector[i], vector[menor] = vector[menor], vector[i]


def readfile(file):
   with open(file,'r') as file1:
       aux = file1.read().split()
   new =  aux[0].replace(',',' ')
   aux = new.split()
   setdata = [int(aux[i]) for i in range(0,len(aux))]
   return setdata

 
def printf(data):
   print('\n')
   print(':::::::::::::::::::::::::::::::')
   print(f'Se contaron {len(data)} chivos')
   print(':::::::::::::::::::::::::::::::')
   count=[0,0]
   for i in range(0,len(data)):
       if data[i]<=80:
          count[0] += 1
       else:
          count[1] += 1
   print (f'Hembras: {count[0]}')
   print (f'Machos: {count[1]}') 
   print ('\n')      
   menu = int(input("""
Desea ver que numero de identificacion
Tienen los chivos contados?
[0] No
[1] Si
                                                                          
 --> """))
   if menu == 0:
       pass
   elif menu == 1:
       for i in range(0,len(data)):
          if data[i]<=80:
              print(f'Se conto la hembra numero: {data[i]}')
          else:
              print(f'Se conto el macho numero: {data[i]}')

def run():
   dataset = readfile("./chivos.txt")
   selectionSort(dataset)
   printf(dataset)
   comparacion(dataset)

if __name__=='__main__':
    run()


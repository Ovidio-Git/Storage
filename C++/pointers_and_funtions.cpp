
/* En c/c++ hay dos formas de pasar
argumentos en una funcion

por valor : que es  pasar el valor a la 
funcion, este metodo lo que hace es que
pasa una copia del valor asignado a la
funcion asi que cualquier tipo de 
operaciones que realices en la funcion 
no afectaran de ninguna forma  el valor
de la variable que asignamos como 
argumento

por referencia: es pasar como argumento
la direccion de la variable ingresada
lo que hace que cada operacion
que realicemos en este argumento
cuando termine de ejecutar la funcion
modificara el valor de la variable
ingresada como argumento*/



#include <iostream>

using namespace std;

int referencia(int *ref);

int main () {
   int x = 4;
   referencia(&x);
   cout << "El valor de x despues de referencia es" 
        << x;
}

int referencia(int *ref){
    *ref = 10 + *ref;
    return 0;
}



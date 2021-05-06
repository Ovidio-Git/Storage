
// con esto tiro comentarios bebe

#include <iostream>


using namespace std; 

int ovidio(int);

int main()
{
    int numero, numero2, sumatris, p;
    numero = numero2 = sumatris = p =0;
    cout<< "Desea iniciar el programa?\n"
        << "[1] Iniciar el programa\n"
        << "[2] No inciar ni mierda\n->";
    
    cin >> numero2;
    
    while (numero2 == 1)
    {
        cout << "[0] para finalizar el programa\n"
             << "Introdusca un numero: ";
        cin >> numero;

        if (numero > 100 && numero > 0)
        {
            cout << numero *2 
                 << '\n';
        } 
        else if (numero < 100 && numero > 0) 
        {
            for (int i = 0; i <= numero; i++)
            {
                cout << sumatris ++ << '\n';
            }
        } 
        else if (numero == 0)
        {
            break;
        }
        else
        { 
            ovidio(p); 
        }
    }
    return 0;
}


int ovidio(int numeris){
    cout << "testing " 
         << numeris ++
         << "\n";
}
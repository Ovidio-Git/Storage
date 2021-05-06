#include <iostream>
#include <cstdlib>
#include <ctime> 

using namespace std; 

int main (void) {

   cout << "time system value: "
        << time(0)
        << endl;

   srand(time(0));

   for(int i=0;i<=20;i++)
   {
     cout << "random number: "
          << (rand()%10) +1 
	  << endl;  
   }

    return 0;
}



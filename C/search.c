#include <stdio.h>
#include <string.h>

void search(char value1[],char value2[]){

    FILE *ptrfile;
    char cur = 0;

    // open POST request file
    ptrfile= fopen("stash.txt", "r");

    while(1){

        // extract user and password of POST request
        fscanf(ptrfile,"Username=%s Password=%s",value1, value2);
        fseek(ptrfile, cur, SEEK_END);
        cur +=7;

        // finish loop
        if (value1[0] != 0){
            break;
        }

    }
    //close file
    fclose(ptrfile);
    //delete post request file
    remove("stash.txt");
}


int main(){
    char value1[16]={0};
    char value2[16]={0};
    search(value1, value2);
    printf("value 1: %s \n\r", value1);
    printf("value 2: %s \n\r", value2);
}
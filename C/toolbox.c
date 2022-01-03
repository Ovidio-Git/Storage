#include "toolbox.h"


/** Render html template
 *
 *  char file[] -> filename html
 *  char socket[] -> socket for send information
 *  return -> -1 if html file not found
 */
char render(char file[], int socket){

    // Website templates files
    char *ptrContent = NULL;
    long filesize = 0;
    FILE* ptrfile = NULL;

    // Open file
    ptrfile = fopen(file, "r");
    if (ptrfile == NULL){
        printf("[ERROR] File not found\n\r");
        return (-1);
    }
    printf("[+] html found\n\r");

    //  File size
    fseek(ptrfile, 0L, SEEK_END); // go end file
    filesize = ftell(ptrfile);
    fseek(ptrfile, 0L, SEEK_SET); // go start file
    printf("[+] html size [%ld] bytes\n\r", filesize); // print file size

    ptrContent = (char*) malloc(filesize);    // reserving memory
    fread(ptrContent, 1, filesize, ptrfile);  // reading file content
    send(socket, ptrContent, filesize, 0);  // sending website file
    for(int i=0; i<100000000; i++); // delay for testing
    close(socket); // close client socket
    free(ptrContent);   // freeing memory
    fclose(ptrfile);    // close file
    return(0);
}

/** write a file.txt with buffer information
 *
 *  char buffer[] -> variable 1
 */
void write (char buffer[]){
    FILE *ptrfile;
    /* create the file for writing*/
    ptrfile = fopen ("stash.txt","w");
    /* write buffer information*/
    fprintf (ptrfile, buffer);
    /* close the file*/
    fclose (ptrfile);
}


/** Search varaibles in file.txt
 *
 *  char value1[] -> variable 1
 *  char value2[] -> variable 2
 *  Return -> value of variables
 */
void search(char value1[],char value2[]){

    FILE *ptrfile;
    char cur = 0;

    // clean data input
    for (int i = 0; i <= 10; i++)
    {
        value1[i]=0;
        value2[i]=0;
    }

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




/** Verfication username and password for login
 *
 *  Return -> 1 user correct
 *  Return -> 0 user incorrect
 */
char login(char username[], char password[]){

    FILE *database;
    char userdb[20], passdb[20];
    char cur=0;

    // open database file
    database= fopen("database.txt", "r");
    while(1){

        // extract user and password of database
        fscanf(database,"User:%s Password:%s",userdb,passdb);
        fseek(database, cur, SEEK_SET); // go end file

        // compare data with database
        if( (strcmp(username,userdb)==0) && (strcmp(password,passdb)==0) ){
            return 1;
        }
        else{
            cur += 27;
        }
        if (cur == fseek(database, cur, SEEK_END) ){
            return 0;
        }
    }
    //close database
    fclose(database);
    return(0);
}


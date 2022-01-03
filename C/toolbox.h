// compiler one time
#ifndef _TOOLBOX_H_
#define _TOOLBOX_H_

// call standart librarys
#include <stdio.h>
#include <string.h>


/** Render html template
 *
 *  char file[] -> filename html
 *  char socket[] -> socket for send information
 *  return -> -1 if html file not found
 */
char render(char file[], int socket);

/** Search varaibles in file.txt
 *
 *  char value1[] -> variable 1
 *  char value2[] -> variable 2
 *  Return -> value of variables
 */
void search(char value1[],char value2[]);

/** write a file.txt with buffer information
 *
 *  char buffer[] -> variable 1
 */
void write (char buffer[]);


/** Verfication username and password for login
 *
 *  Return -> 1 user correct
 *  Return -> 0 user incorrect
 */
char login(char username[], char password[]);

#include "toolbox.c"
#endif
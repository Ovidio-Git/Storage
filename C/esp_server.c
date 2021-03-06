#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h> // for socket(), connect(), and blind()
#include <string.h>     // for strncmp()
#include <netinet/in.h>
#include "toolbox.h"    // for render(), search()

#define  MAXPENDING 2  //  queue max connection permited

int main(){

    int port = 19904;
    // server variables
    int socket_server = 0;
    int socket_client = 0;
    int addr_length = 0;
    char Bind, Listen = 0;
    char aux = 8;
    char msg[] = "HTTP/1.1 200 OK\r\n\r\n";
    char buffer[100] ={0};
    char username[10]={0};
    char password[10]={0};
    struct sockaddr_in server_server;
    struct sockaddr_in server_client;

    printf("[+] PORT: %d\n\r", port);
    // create socket sever
    socket_server = socket(PF_INET, SOCK_STREAM, 0);
    if (socket_server < 0){
        perror("[ERROR] Socket");
        return(-1);
    }
    printf("[+] Socket\n\r");


    // Server parameters
    server_server.sin_family      = PF_INET ;  // protocol
    server_server.sin_addr.s_addr = INADDR_ANY; // server ip
    server_server.sin_port        = htons(port); // connection port
    // htons(port number) convert to 6 bit format


    // the funtion bind merge socket with serverr
    Bind = bind(socket_server, (struct sockaddr*)&server_server, sizeof(server_server));
    if (Bind < 0){
        perror("[ERROR] Bind");
        return (-1);
    }
    printf("[+] Bind\n\r");


    // Listen funtion
    Listen = listen(socket_server, MAXPENDING);
    if (Listen < 0){
        perror("[ERROR] Listen");
        return(-1);
    }
    printf("[+] Listen\n\r");


    while(1){

        // create socket client
        socket_client = accept(socket_server,(struct sockaddr*)&server_client, &addr_length);

        // send data
        while(recv(socket_client, buffer, sizeof(buffer),0) > 0){

            aux = 0;
            // send index.html
            if (strncmp("GET / ", buffer, 6) == 0){
                render("./index.html", socket_client);
            }
            // send main.css
            else if (strncmp("GET /main.css", buffer, 13) == 0){
                render("./main.css", socket_client);
            }
            //receive post request
            else if (strncmp("t-Encoding", buffer, 10) == 0){
                write(buffer);
                search(username,password);
                printf("\n\rUSER:%s",username);
                printf("\n\rNAME:%s",password);
                aux = login(username, password);
                printf("\n\rlogin value -> %d <-", aux);
                //send dashboard.html
                if (aux == 1){
                    render("./dashboard.html", socket_client);
                }
                else{
                    render("./index.html", socket_client);
                }
            }
            printf("==============\n\r%s\n\r==============\n\r",buffer);

        }
    }

    // closed sockets
    close(socket_server);
    close(socket_client);
    return(0);
}





/*

for this applicaction we need programmer a socket with 
protocol  TCP(or UDP) and IP 

¿What is sockets?

files write  host and reading for others host
point connection and comunication 
TCP = information important
UDP = information fast

*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h> //for socket(), connect(), send() and recv()
#include <netinet/in.h>

// SOCK_STREAM -> TCP 
// SOCK_DGRAM -> UDP

int main(){
    
    int connection = 0;
    int socket_id = 0;
    char msg[] ="Hello server!\n\r";
    char buffer[100]={0};
    socket_id = socket(PF_INET, SOCK_STREAM, 0);

    // Server parameters   AWS IP Public= 18.222.148.97
    struct sockaddr_in serverc;
    serverc.sin_family = AF_INET ;  // protocol
    serverc.sin_addr.s_addr = inet_addr("127.0.0.1"); // server ip
    serverc.sin_port = htons(19900); // connection port
    // htons(port number) convert to 6 bit format 
    
    
    // Make connection
    connection = connect(socket_id, (struct sockaddr*)&serverc, sizeof(serverc));
    if (connection < 0){
        perror("[ERROR] connection failed");
        return(-1);
    }
    printf("[CONNECTION SUCCESS]\r\n");


    if (send(socket_id, msg, sizeof(msg), 0) < 0){
        perror("[ERROR] Data send");
        return(-1);
    }
    printf("[DATA SEND]\r\n");
    
    
    if(recv(socket_id, buffer, sizeof(buffer),0) <0 ){
        perror("[ERROR] Data Reveice");
        return(-1);
    }
    printf("[DATA RECEIVE]\r\n");
    
    
    printf("%s", buffer);
    
    close(socket_id);
    return (0);
}
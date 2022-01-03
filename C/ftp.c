
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h> //for socket(), connect(), send() and recv()
#include <netinet/in.h>

// SOCK_STREAM -> TCP 
// SOCK_DGRAM -> UDP

int main(){
    
    int connection = 0;
    int socket_id = 0;
    char msg[] ="ftp\n\r";
    char buffer[30]={0};


    // Server parameters  IP-FTP = 167.114.65.195
    struct sockaddr_in serverftp;
    serverftp.sin_family = AF_INET ;// protocol
    serverftp.sin_addr.s_addr = inet_addr("164.58.253.11"); // server ip
    serverftp.sin_port = htons(5000); // ftp connection port


    socket_id = socket(PF_INET, SOCK_STREAM, 0); // TCP Protocol
    if (socket_id < 0){
        perror("[ERROR] Socket\r\n");
        return(-1);
    }
    printf("[+] Socket created\r\n");


    
    if (connect(socket_id, (struct sockaddr*)&serverftp, sizeof(serverftp)) < 0){
        perror("[ERROR] Connection\r\n");
        return(-1);
    }
    printf("[+] Successful connection\r\n");

    
    // if (send(socket_id, msg, sizeof(msg), 0) < 0){
    //     perror("[ERROR] Send \r\n");
    //     return(-1);
    // }
    // printf("[+] Data send\r\n");


    while (recv(socket_id,buffer,sizeof(buffer),0) > 0){
         printf("%s", buffer);
        return(-1);
    }
    printf("[+] Data receive\r\n");

    close(socket_id);
    return (0);
}




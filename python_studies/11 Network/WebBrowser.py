'''
    WEB BROWSER COM SOCKET
    imprime o texto que pegou no site
'''
import socket

mysock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
mysock.connect (('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd) #esteblece a conexao 

while True:
    data = mysock.recv(512) #recebe 512 chars por vez
    if (len(data) < 1): #0 chars = fim da string 
        break
    print(data.decode()) 
mysock.close()
'''
Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count
of the number of characters at the end of the document

sockets -> a conexao entre o meu pc e um site por exemplo 
    permite que a gente receba e envie dados 
'''
import socket #biblioteca de socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #eh uma socket que passa pela internet
mysock.connect (('data.pr4e.org', 80)) #host e porta que deseja conectar ao socket -> conecta com o host

#Faz o pedido de um doc (romeo.txt) para o servidor 
'''
    GET eh o tipo de request feito para acessar websites
'''
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #encode converte tudo que encontrar para UTF-8

mysock.send(cmd) #esteblece a conexao 



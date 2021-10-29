'''
Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.
'''

import socket

url = input("Enter URL - ")

try: 
    host=url.split('/')[2]
    mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect((host,80))
#cmd=f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    cmd=("GET " + url + " HTTP/1.0\r\n\r\n").encode()
    mysock.send(cmd)
except: 
    print("Invalid URL")
    exit()


count = 0
'''
P/ RESOLVER:
    loop ta infinito 
    count nao ta contando os chars direito
    nunca entra no if
'''
while True:
    print("entrei no while") 
    #recebe 512 chars por vez
    data = mysock.recv(512)
    print(count) 
    #percote cada bloco de 512 chars recebido
    for c in data:
        print("entrei no for") 
        count += 1 
        #se atingir o limite de char ou se os chars acabarem
        if count > 3000 or len(data) < 1: 
            print("ENTREI NO IFFFFFFFFFFFFFFF") 
            break   

#print(data.decode())
print(count)
mysock.close()
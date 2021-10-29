''' 
Adicione linhas de código no programa abaixo para identificar quem possui mais mensagens no arquivo. Após todo o dado ser
lido e todo o dicionário ser criado, procure no dicionário, utilizando um
laço máximo (Veja o capítulo 5: Laços máximo e mínimo), quem tem o
maior número de mensagens e mostre em tela quantas mensagens essa
pessoa tem.

'''

fname = input ("Nome do arquivo: ")

try:
    file = open (fname)
except:
    print ("Arquivo invalido")
    quit()
    
di = dict()

for line in file:
    if line.startswith ("From:"):
        words = line.split()
        for i in range(len(words)):
            if i == 1:
                di[words[i]] = di.get(words[i], 0) + 1

    
largest = -1 
for k,v in di.items():
    #print(k, v)
    if v > largest:
        largest = v
        email = k
        
        
print (email, largest)  
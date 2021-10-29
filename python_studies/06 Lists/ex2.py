''' 
fhand = open('mbox-short.txt')
contador = 0
for linha in fhand:
palavras = line.split()
# print 'Debug:', palavras
if len(palavras) == 0 : continue
if palavras[0] != 'De' : continue
print(palavras[2])


Descubra qual linha do programa acima não está devidamente protegida. Veja se você pode construir um arquivo de texto que causa falha no programa e depois modifique o programa para que a linha seja propriamente protegida e por fim, teste o programa para ter certeza que ele manipula corretamente o novo arquivo de texto. 

'''

fname = input('Digite o nome de um arquivo: ')

try:
    file = open(fname)
except:
    print('Arquivo invalido.')
    quit()
   

for line in file:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    #if words[0] == 'De':
    print(words[2])


'''
Exercício 1: Escreva um loop while que inicia no último caractere da
string e caminha para o primeiro caractere, imprimindo cada letra em
uma linha separada.

Exercício 2: Dado que fruta é uma string, qual o resultado de fruta[:]?
'''


fruta = 'banana'

indice = len(fruta)-1


print('While ao contratio')
while indice >= 0:
    print(fruta[indice])
    indice -= 1
    
    
print('\nfor')
for char in fruta:
    print(char)

print('\nslice')
print(fruta[:])
    

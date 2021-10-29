''' 
Reescreva o código guardião nos exemplos acima sem duas
declarações if. Em vez disso, use uma expressão lógica composta usando
o operador lógico or, com uma única declaração if
'''

fname = input('Digite o nome de um arquivo: ')

try:
    file = open(fname)
except:
    print('Arquivo invalido.')
    quit()
    
for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    print(words[2])
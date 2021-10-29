
''' 
Revise um programa anterior como é pedido: Leia e analise
as linhas com “From” e retire os endereços dessas linhas. Conte o número de mensagens de cada pessoa usando um dicionário. Depois de todos os dados serem lidos, mostre a pessoa com mais envios criando uma lista de tuplas (contagem, email) do dicionário. Então, ordene a lista em ordem reversa e mostre a pessoa na primeira posição

'''
fname = input ("Nome do arquivo: ")

try:
    file = open (fname)
except:
    print ("Arquivo invalido")
    quit()
    
di = dict()

for line in file:
    if line.startswith("From:"):
        words = line.split()
        for i in range(len(words)):
            if i == 1: #se for a palavra na pos 3
                di[words[i]] = di.get(words[i], 0) + 1

lst = sorted(  [ (v, k) for k,v in di.items() ], reverse = True)

for v, k in lst[:1]:
    print(k, v)
    
'''
Outra forma de fazer a linha 19

lst = list()

for k, v in di.items():
    newTuple = v, k
    lst.append(newTuple)
    print (v, k)

#lst = sorted(lst, reverse = True)
sortedList = sorted(lst, reverse = True)

for v, k in sortedList:
    print (k, v)

'''
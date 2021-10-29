import re

'''
terminado?
Exercício 2: Escreva um programa que procure por uma linha na forma:
Nova Revisão: 39772
Extraia o número de cada linha usando uma expressão regular e o método findall(). Compute o valor médio dos números e mostre-o.

'''

fname = input ("Digite o nome do arquivo:")

try:
    file = open (fname)
except:
    print ("Arquvo invalido")
    quit()
    
lst = list ()
count = 0
res = 0
x = 0
aux = 0

for line in file:
    if re.search ('^New Revision: ', line):
        numb = re.findall (r'\d+', line)
        count = count + 1
        for i in numb:
            aux += int(i)


print (aux/count)

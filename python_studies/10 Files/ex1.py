'''
EXERCICIO 1

Escreva um programa que leia um arquivo e mostre o conteúdo deste (linha por linha), completamente em caixa alta.

A execução
do programa deverá ser a seguinte:
python shout.py
Digite o nome de um arquivo: mbox-short.txt
'''

fname = input('Digite o nome de um arquivo: ')

try:
    file = open(fname)
except:
    print('Arquivo invalido')
    
for line in file:
    line = line.upper()
    
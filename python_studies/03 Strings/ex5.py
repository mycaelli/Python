'''
Exercício 5: Utilize o seguinte código em Python que guarda uma string:
str = 'X-DSPAM-Confidence:0.8475' Use a função find e o fatiamento de
strings para extrair a porção da string depois do sinal de dois pontos e
use a função float para converter a string extraída em um número de
ponto flutuante.
'''

str = 'X-DSPAM-Confidence:0.8475'

pos = str.find(':')

fatia = str[pos+1 : len(str)]

print(float(fatia))

'''
Quando encontrar uma linha que inicie com “X-DSPAM-Confidence:”
separe a linha do texto para extrair o número de ponto flutuante que
ela contém. Conte essas linhas e então compute o total de valores de
Confiança de Spam nelas. Quando chegar no fim do arquivo, mostre a
média de Confiança de Spam.

Digite o nome de um arquivo: mbox-short.txt
Média de spam: 0.750718518519

'''


fname = input('Digite o nome de um arquivo: ')

try:
    file = open(fname)
except:
    print('Arquivo invalido.')
    quit()

cont = 0
soma = 0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        posi = line.find(' ')
        posf = line.find('\n')
        data = float(line[posi:posf])
        cont += 1
        soma  += data

print('Media de spam: ', soma/cont)
        
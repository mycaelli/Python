'''
Escreva um programa que leia uma caixa de email, e quando você encontrar uma linha que comece com “De”, você vai separar a linha em palavras usando a função split. Nós estamos interessados em quem envia a mensagem, que é a segunda palavra na linha que começa com
From.

Você vai analisar a linha que começa com From e irá pôr para imprimir
na tela a segunda palavra (para cada linha do tipo), depois o programa
também deverá contar o número de linhas que começam com “De” e
imprimir em tela o valor final desse contador.
'''


fname = input('Digite o nome de um arquivo: ')

try:
    file = open(fname)
except:
    print('Arquivo invalido.')
    quit()
    
count = 0
for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    print(words[1])
    count = count + 1
    
print('There were ', count, 'lines in the file with From as the first word')
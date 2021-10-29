'''Escreva um programa que peça por uma pontuação entre
0.0 e 1.0. Se a pontuação for fora do intervalo, mostre uma mensagem
de erro. Se a pontuação estiver entre 0.0 e 1.0, mostre a respectiva nota
usando a seguinte tabela'''

p = input('Digite a pontuacao: ' )

try:
    fp = float(p)
except:
    print('Invalido. Por favor digite um valor numerico')
    quit()
    
if (fp > 1.0 or fp < 0.0):
    print('Pontuacao Invalida')
else:
    if (fp < 0.6):
        print('F')
    if (fp >= 0.6 and fp < 0.7):
        print('D')
    if (fp >= 0.7 and fp < 0.8):
        print('C')
    if (fp >= 0.8 and fp < 0.9):
        print('B')
    if (fp >= 0.9):
        print('A')


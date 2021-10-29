'''
Reescreva o programa de notas do capítulo anterior usando a função computarNotas que recebe a pontuação como parâmetro e
retorna a nota como uma string.
'''

p = input('Digite a pontuacao: ' )

try:
    fp = float(p)
except:
    print('Invalido. Por favor digite um valor numerico')
    quit()
    
def computarNotas(nota):
    print(nota)
    
if (fp > 1.0 or fp < 0.0):
    print('Pontuacao Invalida')
else:
    if (fp < 0.6):
        computarNotas('F')
    if (fp >= 0.6 and fp < 0.7):
        computarNotas('D')
    if (fp >= 0.7 and fp < 0.8):
        computarNotas('C')
    if (fp >= 0.8 and fp < 0.9):
        computarNotas('B')
    if (fp >= 0.9):
        computarNotas('A')
        



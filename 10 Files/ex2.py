'''
Escreva um programa que solicite um arquivo e então leia
ele e procure por linhas da forma:
X-DSPAM-Confidence: 0.8475

'''

fname = input('Digite o nome de um arquivo: ')

try:
    file = open(fname)
except:
    print('Arquivo invalido.')
    quit()

cont = 0
for line in file:
    if line.startswith('X-DSPAM-Confidence: 0.8475'):
        cont++
        print(line)
        
    

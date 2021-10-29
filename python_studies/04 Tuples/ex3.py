
''' 
Exercício 3: Escreva um programa que leia um arquivo e mostre
as letras em ordem decrescente de frequência. Seu programa deve converter todas as entradas para Caixa baixa e apenas contar as letras de a à z. Não conte espaços, dígitos, pontuações, ou qualquer coisa que não seja uma letra do alfabeto. 

'''

fname = input ("Nome do arquivo: ")

try:
    file = open (fname)
except:
    print ("Arquivo invalido")
    quit()


count = dict()
for line in file:
    words = line.split()
        #print(words)
    for letters in words:   
        letters = letters.lower()
        #print(letters)
        for let in letters:
            if let.isalpha():
                count[let] = count.get(let, 0) + 1
                #print(let)

lst = sorted ( [ (v, k) for k, v in count.items() ] )

for v, k in lst:
    print (k, v)
    
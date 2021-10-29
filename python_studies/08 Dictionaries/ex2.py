''' 
Escreva um programa que categorize cada mensagem de
e-mail de acordo com o dia em que a mensagem foi enviada. Para
isso, procure por linhas que comecem com “From”, depois procure pela terceira palavra e mantenha uma contagem de ocorrência para cada dia da semana. No final do programa, mostre em tela o conteúdo do seu dicionário (a ordem não interessa).

'''

fname = input ("Nome do arquivo: ")

try:
    file = open (fname)
except:
    print ("Arquivo invalido")
    quit()

di = dict()
#le as linhas do arquivo
for line in file:
    if line.startswith("From"):
        #separa as palavras da linha 
        words = line.split()
        #itera a lista de palavras por indice
        for i in range(len(words)):
            if i == 2: #se for a palavra na pos 3
                di[words[i]] = di.get(words[i], 0) + 1 #adc ao dicionario
               
print (di)
''' 

Escreva um programa que leia as palavras em words.txt e as armazena
como chaves em um dicionário. Não importa quais são os valores. Então,
você pode usar o operador in como uma maneira rápida de verificar se
uma string está no dicionário.

'''

fname = input ("Digite o nome do arquivo: ")

try:
    file = open (fname)
except:
    print("Arquivo invalido")
    quit()

dic = dict()

for words in file:
    dic[words] = words

print(dic)

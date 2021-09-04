''' 
Escreva um programa para abrir o arquivo chamado romeo.txt e leia-o linha por linha. Para cada linha, separe-a em uma lista de palavras usando a função split.
Para cada palavra, cheque se esta palavra já existe na lista. Caso não exista,
adicione ela. Quando o programa terminar de verificar, ordene e imprima estas
palavras em ordem alfabética.** '''


file = open('romeo.txt')

lista  = list()
newList = list()

#separa o texto em listas de palavras
for line in file:
  lista.append (line.split())

#tres listas em uma unica lista
for i in lista:
  newList.extend(i)

finalList = list()

#tira as palavras repetidas da lista
for word in newList:
  if word not in finalList:
    finalList.append(word) 

finalList = sorted(finalList)

print("Lista ordenada \n")
print(finalList)


    

        
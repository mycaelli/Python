
'''
Reescreva o programa que solicita o usuário uma lista de
números e prints e imprime em tela o maior número e o menor número
quando o usuário digitar a palavra “feito”. Escreva um programa para
armazenar as entradas do usuário em uma lista e use as funções max()
e min() para computar o número máximo e o mínimo depois que o laço
for completo
'''
lista = []

while True:
    data = input('digite um numero ')
    if data == 'Done':
        print('Maximo: ', max(lista))
        print('Minimo: ', min(lista))
        quit()
           
    try:
        number = int(data)
    except:
        print('Entrada invalida.')
        quit()
        
    lista.append(number) 
    print(lista)


  

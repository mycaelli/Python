''' 

palavra = 'banana'
contagem = 0
for letra in palavra:
if letra == 'a':
contagem = contagem + 1
print(contagem)


Exercício 3: Encapsule esse código em uma função chamada contagem,
e generalize para que ela aceite a string e a letra como argumentos.
'''

def contagem(s, letra):
    
    contagem = 0
    for letra in s:
        if letra == 'a':
            contagem = contagem + 1
    print(contagem)

contagem('banana', 'a')
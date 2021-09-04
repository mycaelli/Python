'''
Escreva um programa que lê repetitivamente números até
que o usuário digite “pronto”. Quando “pronto” for digitado, mostre a
soma total, a quantidade e a média dos números digitados. Se o usuário
digitar qualquer coisa que não seja um número, detecte o erro usando
o trye o except e mostre na tela uma mensagem de erro e pule para o
próximo número.
'''


soma = 0
i = 0

while True:
    numS = input('digite um numero: ')
    
    if numS == 'pronto':
       print('FIM')
       print(soma, i, media)  
       quit()
        
    try: 
       num = float(numS)
    except: 
        print ('Entrada Invalida')
        
    soma += num
    i += 1
    media = soma / i
    
    
    
    
        
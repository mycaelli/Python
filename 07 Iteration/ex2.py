'''
Escreva outro programa que pede por uma lista de números
como no exercicio anterior e mostra, no final, o máximo e o mínimo dos
números ao invés da média.
'''

v = [ ]
minimo = None
maximo = None

while True:
    numS = input('digite um numero: ')
    
    if numS == 'pronto':
       print('FIM')
       print (v)
       menor = min(v)
       maior = max (v)
       print('Min: ', menor, 'Max: ', maior)  
       quit()
    
    try: 
       num = float(numS)
    except: 
        print ('Entrada Invalida')
        
    v.append(num)
    
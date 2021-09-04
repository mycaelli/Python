''' Reescreva seu programa de pagamento utilizando try e
except, de forma que o programa consiga lidar com entradas não numéricas graciosamente, mostrando uma mensagem e saindo do programa. A
seguir é mostrado duas execuções do programa
'''

h = input("Horas: ")
s = input("Taxa/horas: ")

try:
    fh = float(h)
    fs = float(s)
except:
    print('Erro, por favor utilize entradas numericas')
    quit()
    
if fh > 40:
    t = (fh - 40.0) * (fs * 0.5)
    print ('Valor a ser pago: ', t + (fh * fs))
else:
    print ('Valor a ser pago: ', fh * fs)
''' 
Reescreva seu programa de cálculo de pagamento com um
1.5 o valor de hora de trabalho por hora extra, crie uma função chamada
calculoPagamento que aceita dois parâmetros(horas e TaxaHora)
'''

h = input("Horas: ")
s = input("Taxa/horas: ")

try:
    fh = float(h)
    fs = float(s)
except:
    print('Erro, por favor utilize entradas numericas')
    quit()

def calculoPagamento(horas, valor):

    if fh > 40:
        t = (fh - 40.0) * (fs * 0.5)
        print('Valor a ser pago: ', t + (fh * fs))
    else:
        print('Valor a ser pago: ', fh * fs)
        

calculoPagamento(h, s)

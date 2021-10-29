''' Reescreva seu programa de pagamento, para pagar ao funcionário 1.5 vezes o valor da taxa horária de pagamento pelo tempo
trabalhado acima de 40 horas '''

h = float(input("Horas: "))
r = float(input("Taxa/horas: "))

if h > 40:
    t = (h - 40.0) * (r * 0.5)
    print ('Valor a ser pago: ', t + (h * r))
else:
    print ('Valor a ser pago: ', h * r)

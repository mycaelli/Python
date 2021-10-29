'''
Esse programa conta a distribuição de horas no dia para
cada uma das mensagens. Você pode retirar a hora da linha com “From” achando a string de horário e então separando ela em partes usando o caractere “:” (dois pontos). Uma vez acumuladas as contagens para cada hora, mostre os valores, um por linha, ordenados por hora
'''

fname = input ("Nome do arquivo: ")

try:
    file = open (fname)
except:
    print ("Arquivo invalido")
    quit ()
    
di = dict()
for line in file:
    if line.startswith ("From"):
        words = line.split()
        if len (words) < 3:
            continue
        hours = words[5].split(":")
        di[hours[0]] = di.get(hours[0], 0) + 1

       
lst = sorted ( [  (k, v) for k,v in di.items() ] ) 

for k,v in lst:
    print (k, v)
            
'''
Às vezes, quando os programadores estão entediados ou
querem um pouco de diversão, eles adicionam um Easter Egg inofensivo
em seus programas. Modifique o programa que solicita um arquivo ao
usuário para que ele mostre uma mensagem engraçada quando o usuário
deigitar no nome do arquivo “na na boo boo”. O programa deve se
comportar normalmente para todos os outros arquivos que existem e
que não existem. Aqui está uma amostra da execução desse programa:

python egg.py
Digite o nome de um arquivo: mbox.txt
Há 1797 linhas de assunto em mbox.txt
python egg.py
Digite o nome de um arquivo: missing.tyxt
Arquivo não pôde ser aberto: missing.tyxt
python egg.py
Digite o nome de um arquivo: na na boo boo
NA NA BOO BOO PRA VOCÊ TAMBÉM!


PROGRAMA CONTA O NUMERO DE LINHAS DE UM ARQUIVO
'''

fname = input("Digite o nome de um arquivo: ")

palavra = 'na na boo boo'

try:
    file = open(fname)
except:
    if fname == 'na na boo boo':
        print('NA NA BOO PRA VOCE TAMBEM')
        quit()
    print('Arquivo invalido.')
    quit()

cont = 0
for line in file:
    cont += 1
    
print('Total de linhas do arquivo: ', cont)


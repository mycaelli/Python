'''
Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
each email address, and print the dictionary

'''

fname = input ("Nome do arquivo: ")

try:
    file = open (fname)
except:
    print ("Arquivo invalido")
    quit()
    
di = dict()

for line in file:
    if line.startswith("From:"):
        words = line.split()
        for i in range(len(words)):
            if i == 1: #se for a palavra na pos 3
                di[words[i]] = di.get(words[i], 0) + 1



        
       
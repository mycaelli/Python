''' 
Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression:

'''

import re

fname = input ("Digite o nome do arquivo: ")
rename = input ("Digite uma expressao regular: ")


try:
    file = open (fname)
except:
    print ("Arquivo invalido")
    quit()
    
count = 0
for line in file:
    if re.search(rename, line):
        print (line)
        count = count + 1

print (count)
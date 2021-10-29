 #web browser com urllib 
 #http://www.dr-chuck.com/page1.htm
 
import urllib.request, urllib.parse, urllib.error #importa a biblioteca urllib 
 
#fhand -> objeto  
fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm") #encode eh automatico, get eh automatico, conexao eh automatica etc etc 
 
for line in fhand:
    print(line.decode().strip()) #le cada linha do arquivo 
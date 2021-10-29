'''Programa que navega pelos links de webpages usando beautifulSoup

BeautifulSoup trata de todos os problemas que o html encontrado pode ter 
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input ("Enter - ") #recebe uma url
html = urllib.request.urlopen(url).read() #abre a url e le tudo 
soup = BeautifulSoup(html, 'html.parser') #pega o html recebido e devolve um objeto dele 

#devolve as tags anchor 'a'
tags = soup('a')
for tag in tags:
    print(tag.get('href', None)) #imprime o href da pag


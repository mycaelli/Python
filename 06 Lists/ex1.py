'''' 
Escreva uma função chamada corte que recebe uma lista e
a modifica, removendo o primeiro e o último elemento, e retorna None. Depois escreva uma função chamada meio que recebe uma lista e retorna uma nova lista que contém todos, menos o primeiro e o último elemento.
'''


listinha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def corte(lista): 
  del lista[9]
  del lista[0]
  return 
  
def meio(lista):
  remove = lista[slice(1, len(lista)-1)]
  return remove

corte(listinha)
print('copia lista: ', meio(listinha))

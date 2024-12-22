
#apresentação

from random import shuffle

n1 = input('Digite um nome: ')
n2 = input('Digite outro: ')
n3 = input('Digite outro: ')
n4 = input('Digite outro: ')
lista = [n1,n2,n3,n4]
shuffle(lista)

print('A ordem será: {}'.format(lista))




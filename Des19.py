
# Sorteamento

import random

n1 = input('Digite o nome do primeiro: ')
n2 = input('Digite o nome do segundo: ')
n3 = input('Digite o nome do terceiro: ')
n4 = input('Digite o nome do quarto: ')
nomes = [n1,n2,n3,n4]
sort = random.choice(nomes)


print(f'O nome dos participantes são: {n1}, {n2}, {n3}, {n4}\ne o sorteado foi: {sort}')

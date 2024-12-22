
#Nome

nome = input('Digite o seu nome completo: ').strip()
print(f'em maiúsculas: {nome.upper()}')
print(f'em minúsculas: {nome.lower()}')

res = (len(nome) - nome.count(' '))
res2 = nome.find(' ')
res3 = (len(nome[:res2]))
print(f'quantas letras: {res}')
print(f'quantas letras no primeiro nome: {res3}')



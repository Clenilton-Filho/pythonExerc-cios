numero = int(input('Digite um número para mostrar sua tabuada: '))
print('Início!')
for contador in range(1, 11):
    print(f'{numero} x {contador} = {numero*contador}')
print('Fim!')

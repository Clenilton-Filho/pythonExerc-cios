num = int(input('Digite um número inteiro: '))
resultado = 'é primo'
tot = 0
if num == 1 or num == 0:
    resultado = 'não é primo'
else:
    for contador in range(2, num // 2):
        if num % contador == 0:
            resultado = 'não é primo'
            tot += 1

print(f'O número {num} {resultado}, sendo divísível por {tot} número(s) além de 1 e ele mesmo.')

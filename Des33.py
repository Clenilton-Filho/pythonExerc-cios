# maior número

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número, diferente do primeiro: '))
num3 = int(input('Digite o terceiro número, diferente dos outros: '))

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num2:
    menor = num3

print(f'O maior dentre esses números é: {maior}', end='')
print(f', enquanto o menor é: {menor}')
num1 = int(input(f'Digite um número inteiro: '))
contador = 1
soma = media = maior = menor = num2 = num1
resp = input(f'Quer continuar? (S ou N): ')
while resp not in 'Nn':
    num2 = int(input('Digite um novo número: '))
    soma = soma + num2
    if num2 > num1:
        maior = num2
    if num2 < num1:
        menor = num2
    num1 = num2
    contador += 1
    media = soma / contador
    resp = input(f'Quer continuar? (S ou N): ')
print(f'''Foram digitados {contador} número(s). A média deles números é: {media}'
O maior deles é: {maior}, enquanto o menor é: {menor}''')

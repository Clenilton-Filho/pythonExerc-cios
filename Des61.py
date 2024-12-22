num = int(input('digite um número inteiro qualquer: '))
contador = num - 1
res = num

print(f'{num}! = {num} ', end='')
while contador >= 1:
    print(f'x {contador} ', end='')
    res = res * contador
    contador -= 1

print(f'= {res}')

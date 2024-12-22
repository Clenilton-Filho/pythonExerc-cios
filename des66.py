soma = 0
contador = 1
while True:
    num = int(input(f'digite um número: '))
    if num != 999:
        soma += num
        contador += 1
    else:
        break
print(f'Foram digitados {contador} números, e a soma deles é: {soma}')

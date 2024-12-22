num = 0
contador = 0
soma = 0
while num != 999:
    num = int(input(f'Digite um número (999 p/ encerrar): '))
    if num != 999:
        soma = soma + num
        contador += 1
if soma != 0:
    print(f'Foram digitados {contador} números. A soma deles números é: {soma}')


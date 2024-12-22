n = int(input('digite um número para a sequência: '))
contador = 1
valor1 = 0
valor2 = 1
while contador <= n:
    if contador == 1:
        print(f'{valor1} ', end='')
        contador += 1
    elif contador == 2:
        print(f'-> {valor2} ', end='')
        contador += 1
    else:
        seq = valor1 + valor2
        print(f'-> {seq} ', end='')
        contador += 1
        valor1 = valor2
        valor2 = seq


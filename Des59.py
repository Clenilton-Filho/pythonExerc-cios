operador = 4
res = 0
contador = 1
while operador == 4:
    if contador == 1:
        valor1 = int(input('digite um número: '))
        valor2 = int(input('digite outro: '))
        contador += 1
    operador = int(input('''digite uma das opções:
 [1] somar
 [2] multiplicar
 [3] maior
 [4] novos números
 [5] sair do programa
 '''))
    if operador == 1:
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
    elif operador == 2:
        print(f'{valor1} x {valor2} = {valor1 * valor2}')
    elif operador == 3:
        if valor1 > valor2:
            print(f'{valor1} é maior que {valor2}')
        else:
            print(f'{valor2} é maior que {valor1}')
    elif operador == 5:
        print(f'Até a próxima!')
        exit(0)
    operador = 4



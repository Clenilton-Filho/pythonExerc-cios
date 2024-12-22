from random import randint
player = contador = 0
while True:
    resp = input('par ou ímpar: ').lower().strip()
    player2 = int(input('digite um número de 0 a 10: '))
    com2 = randint(0, 10)
    if resp == 'par':
        player = 1
        com1 = 2
    else:
        player = 2
        com1 = 1
    print(f'Computador: {"par" if com1 == 1 else "ímpar"}, {com2}')
    if (player2 + com2) % 2 == 0 and player == 1 and com1 == 2:
        contador += 1
    elif (player2 + com2) % 2 == 0 and player == 2 and com1 == 1:
        break
    elif (player2 + com2) % 2 != 0 and player == 1 and com1 == 2:
        break
    elif (player2 + com2) % 2 != 0 and player == 2 and com1 == 1:
        contador += 1
    print(f'Você ganhou!')
print(f'Resultado: Você perdeu! Você ganhou {contador} rodadas consecutivas!')

valor = int(input('digite um valor a ser sacado: R$'))
ced50 = ced20 = ced10 = ced1 = 0
while True:
    if valor <= 0:
        break
    elif valor > 50:
        ced50 += 1
        valor -= 50
    elif valor > 20:
        ced20 += 1
        valor -= 20
    elif valor > 10:
        ced10 += 1
        valor -= 10
    else:
        ced1 += 1
        valor -= 1
print(f'''Cédulas de 50: {ced50}
Cédulas de 20: {ced20}
Cédulas de 10: {ced10}
Cédulas de 1: {ced1}''')

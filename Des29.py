# Multa de excedência

velocidade = float(input('Digite a velocidade em que o veículo passou, em km/h: '))
if velocidade >= 81:
    print(f'Multa de {int((velocidade-80)*7)},00R$! ')
else:
    print('Sem multa.')

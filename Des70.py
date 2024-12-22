mais1000 = total = 0
contador = 1
while True:
    nome = input('digite o nome do produto: ')
    preco = float(input('digite o preço do produto: R$'))
    if preco > 1000:
        mais1000 += 1
    total += preco
    if contador == 1 or preco < barato:
        barato = preco
        nomebarato = nome
    contador += 1
    while True:
        resp = input('quer continuar? (s ou n): ')
        if resp in 'SsNn':
            break
    if resp in 'Nn':
        break
print(f'''O total da compra foi: {total}
Foram comprados {mais1000} produtos com preço maior que R$1000.00
O produto mais barato comprado foi: {nomebarato}, de R${barato:.2f}''')


preco = int(input("Digite o preço do produto: "))
resp = input('''digite a forma de pagamento:
            [1] à vista
            [2] no cartão
            [3] 2x no cartão 
            [4] 3x ou mais no cartão
            ''')
if resp == '1':
    preco = preco * .9
    totparcelas = 1
elif resp == '2':
    preco = preco * .95
    totparcelas = 1
elif resp == '3':
    totparcelas = 2
elif resp == '4':
    totparcelas = int(input('Quantas parcelas? '))
    preco = preco * 1.2
elif resp != '3' != '1' != '2' != '4':
    print("Digite uma opção válida!")
    exit(0)
parcela = preco / totparcelas
print(f'O preço do produto será de R${preco:.2f} em {totparcelas} parcela(s) de R${parcela:.2f}')

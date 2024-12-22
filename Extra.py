
#à vista ou a prazo

valor = float(input('Digite o valor do produto: '))
print('O preço à vista do produto será de {:.2f} R$, enquanto a prazo o preço será de {:.2f} R$'.format(valor-(valor * 10 / 100),valor+(valor * 10 / 100)))


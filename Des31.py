# Passagem

distância = float(input('Digite uma distância para uma viagem: '))
if distância <= 200:
    print(f'O valor da passagem ficará: {0.5*distância:.2f}R$')
else:
    print(f'O valor da passagem ficará: {0.45*distância:.2f}R$')


#Aluguel de carro

dias = int(input('Digite a quantidade de dias que se passaram no aluguel do carro: '))
km = float(input('Digite a quantidade de quilômetros rodados durante o aluguel: '))
print(f'O valor final do aluguel será de: {(60 * dias) + (0.15 * km) :.2f} R$')

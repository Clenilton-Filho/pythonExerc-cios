
# Aumento de salário

salário = float(input('Digite o salário atual (sem pontos): R$'))

if salário <= 1250 :
    salário = salário * 1.15
else:
    salário = salário * 1.10

print(f'O novo valor do salário com o aumento será de: R${salário:.2f}')

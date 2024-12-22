maior = 0
menor = 500

for contador in range(1, 6):
    peso = int(input(f'Digite o peso da {contador}ª pessoa: Kg '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior foi: {maior} Kg, enquanto o menor foi: {menor} Kg')

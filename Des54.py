from datetime import date
data = date.today()
ano = data.year
contador2 = 0
contador3 = 0
for contador in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {contador}ª pessoa: '))
    if ano - nasc < 18:
        contador2 += 1
    else:
        contador3 += 1
print(f'Maiores de idade: {contador3}. Menores de idade: {contador2}')

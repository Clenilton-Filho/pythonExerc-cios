media = 0
nomevelho = ''
velho = 0
soma = 0
menos20 = 0
for contador in range(1,5):
    nome = input(f'Digite o nome da {contador}ª pessoa: ')
    idade = int(input(f'Digite a idade da {contador}ª pessoa: '))
    sexo = input(f'Digite o sexo da {contador}ª pessoa (F ou M): ')

    soma += idade

    if sexo == 'F' and idade < 20:
        menos20 += 1

    if sexo == 'M' and velho < idade:
        velho = idade
        nomevelho = nome

media = soma / 4

print(f'A média de idade é: {media:.0f} anos, o nome do homem mais velho é: {nomevelho} e temos {menos20} mulheres abaixo de 20 anos')

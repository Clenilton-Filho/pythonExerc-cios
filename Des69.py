maiores = homens = mulheres20 = 0
contador = 1
while True:
    idade = int(input(f'digite a idade da {contador}ª pessoa: '))
    while True:
        sexo = input(f'digite o sexo dessa pessoa (F ou M): ')
        if sexo in 'FfMm':
            break
    contador += 1
    if sexo in 'Mm':
        homens += 1
    if idade > 18:
        maiores += 1
    if sexo in 'Ff' and idade < 20:
        mulheres20 += 1
    resp = input('Quer continuar cadastrando?: (s ou n)')
    if resp not in 'Ss':
        break
print(f'''Foram cadastradas {maiores} pessoas com mais de 18, {homens} homem(s)
e {mulheres20} mulher(es) com menos de 20 anos''')

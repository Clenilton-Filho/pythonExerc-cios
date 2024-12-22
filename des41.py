from datetime import date

nasc = int(input("digite seu ano de nascimento: "))
idade = date.today().year - nasc
categoria = 'eai'
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f"Você tem {idade} anos! A sua categoria é: {categoria}!")

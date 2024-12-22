from datetime import date

nascimento = int(input("Digite o seu ano de nascimento: "))
data = date.today()
ano = data.year
idade = ano - nascimento

if idade < 18:
    print(f"Ainda vai chegar a sua hora de se alistar! ")
    print(f"Ainda faltam {18-idade} anos para isso")
elif idade == 18:
    print(f"Já é hora de se alistar!")
else:
    print(f"Você já passou da idade de se alistar!")
    if idade == 19:
        print("Já se passou 1 ano desde a sua idade para alistamento!")
    else:
        print(f"Já se passaram {idade-18} anos desde o ano estabelecido!")

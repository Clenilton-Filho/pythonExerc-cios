nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

print(f"Sua média é: {media}")
if media < 5:
    print(f"reprovado!")
elif 7 > media >= 5:
    print(f"Recuperação!")
else:
    print(f"Aprovado!")

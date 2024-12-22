peso = float(input("digite seu peso em kg: "))
altura = float(input("digite sua altura em metros: "))

imc = peso/(altura**2)

print(f"Seu IMC é de {imc:.2f}.")
if imc < 18.5:
    print("Abaixo do peso!")
elif 25 > imc >= 18.5:
    print("Peso ideal!")
elif 30 > imc >= 25:
    print("Sobrepeso!")
elif 25 > imc >= 40:
    print("Obesidade!")
else:
    print("Obesidade mórbida!")

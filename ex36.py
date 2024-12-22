valor = int(input("digite o valor da casa: "))
salario = int(input("digite o seu salário: "))
anos = int(input("digite em quantos anos será pago: "))

prestacao = valor / (anos * 12)

if prestacao > salario * .3:
    print(f"A prestação (R${prestacao:.2f}) seria maior que 30% do salário (R${salario*.3}). Negado!")
else:
    print(f"O valor da prestação será de: R${prestacao:.2f}")

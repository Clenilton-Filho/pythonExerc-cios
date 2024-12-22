int1 = int(input("digite um número inteiro: "))
int2 = int(input("digite outro inteiro: "))

if int1 > int2:
    print(f"O primeiro valor ({int1}) é o maior")
elif int2 > int1:
    print(f"O segundo valor ({int2}) é o maior")
else:
    print(f"Nenhum dos dois é maior, pois são iguais.")

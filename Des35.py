# Triângulo
lado1 = float(input('Digite o comprimento um dos lados: '))
lado2 = float(input('Digite  comprimento de outro: '))
lado3 = float(input('Digite comprimento do último: '))


if lado1+lado2 > lado3 and lado1+lado3 > lado2 and lado2+lado3 > lado1:
    print(f'Os lados podem formar um triângulo ', end='')
    if lado1 == lado2 == lado3:
        print("equilátero")
#    elif lado1 == lado2 and lado1 != lado3:
#        print("isósceles")
#    elif lado2 == lado3 and lado2 != lado1:
#        print("isósceles")
#    elif lado1 == lado3 and lado1 != lado2:
#        print("isósceles")
#    else:
#        print("O triângulo é escaleno")
    elif lado1 != lado2 != lado3 != lado1:
        print("escaleno")
    else:
        print("isósceles")
else:
    print(f'Os lados não podem formar um triângulo')

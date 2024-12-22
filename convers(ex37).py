valor = int(input("digite um inteiro para converter: "))
resp = int(input('''digite uma das 3 opções a seguir:
 [1] - Binário
 [2] - Octal
 [3] - Hexadecimal
 resposta: '''))
binario = 0
octal = 0
hexadecimal = 0
if resp == 1:
    binario = bin(valor)
    print(f"O binário desse valor é: {binario[2:]}")
elif resp == 2:
    octal = oct(valor)
    print(f"O octal desse valor é: {octal[2:]}")
elif resp == 3:
    hexadecimal = hex(valor)
    print(f"O hexadecimal desse valor é: {hexadecimal[2:]}")
else:
    print(f"O valor digitado ({valor}) é inválido!")
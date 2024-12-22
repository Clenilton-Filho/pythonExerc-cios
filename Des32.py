# Bissexto

ano = int(input('Digite um ano qualquer: '))
num1 = str(ano+10000)[4]
num2 = str(ano+10000)[3]
num3 = int(num2 + num1)
print(f'{num1} {num2} {num3}')
if num3 % 4 == 0 and num3 != 00:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')

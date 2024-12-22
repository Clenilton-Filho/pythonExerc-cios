n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
média = (n1+n2)/2
print(f'A sua média foi igual a: {média:.1f} ',end='')
if média >=6:
    print(f'e ela está acima do desejado')
else:
    print(f'e ela está abaixo do desejado')

frase = input('Digite uma frase: ').replace(' ', '').strip().upper()
#inverso = ''.join(reversed(frase))
#if frase == inverso:
#    print(f'A frase é um palíndromo')
#else:
#    print(f'A frase não é um #palíndromo')
letra = ''
reverso = ''
for contador in range(len(frase)-1, -1, -1):
    letra = frase[contador]
    reverso = reverso + letra
if reverso == frase:
    print(f'A frase é um palíndromo')
elif reverso != frase:
    print(f'A frase não é um palíndromo')
else:
    print(f'Digite algo válido!')

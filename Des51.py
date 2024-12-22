termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
contador2 = 10
resp = 10
while resp != 0:
    while contador <= contador2:
        print(f'{contador}º termo = {termo}')
        termo += razao
        contador += 1
    resp = int(input('você quer mostrar mais quantos termos?: '))
    contador2 += resp
print(f'Ok. Encerrando!')
exit(0)

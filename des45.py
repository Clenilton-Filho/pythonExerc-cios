import random

resp = input("Vamos jogar jokenpô! Digite 'pedra', 'papel' ou 'tesoura'!")
lista = ['pedra','papel','tesoura']
com = random.choice(lista)
resultado = ''
if resp == 'pedra' and com == 'papel':
    resultado = 'eu ganhei'
elif resp == 'pedra' and com == 'tesoura':
    resultado = 'eu perdi'
elif resp == 'pedra' and com == 'pedra':
    resultado = 'nós empatamos'

elif resp == 'papel' and com == 'papel':
    resultado = 'nós empatamos'
elif resp == 'papel' and com == 'tesoura':
    resultado = 'eu ganhei'
elif resp == 'papel' and com == 'pedra':
    resultado = 'eu perdi'

elif resp == 'tesoura' and com == 'papel':
    resultado = 'eu perdi'
elif resp == 'tesoura' and com == 'tesoura':
    resultado = 'nós empatamos'
else:
    resultado = 'eu ganhei'

print(f"Eu escolhi {com} e {resultado}! =)")

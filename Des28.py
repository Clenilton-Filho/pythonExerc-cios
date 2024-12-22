# Adivinhação
import random
num = int(random.randrange(0, 11))
num2 = int(input('Digite um número para verificar se é o certo, de 0 a 10: '))
contador = 1
while num2 != num:
    if num2 > num:
        num2 = int(input('Menos... Tente novamente!: '))
        contador += 1
    elif num2 < num:
        num2 = int(input(f'Mais... Tente novamente!: '))
        contador += 1
    else:
        print(f'''O número escolhido é o correto. Parabéns!
Foram necessárias {contador} tentativas.''')

print(f'''O número escolhido é o correto. Parabéns!
Foram necessárias {contador} tentativas.''')






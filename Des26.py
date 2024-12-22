
#Pesquisa

frase = input('Digite uma frase: ').strip().lower()

contagem1 = frase.count('a')
contagem2 = frase.find('a')
contagem3 = frase[contagem1]
print(f'A letra A em maíusculo aparece {contagem1} vez(es) durante a frase, enquanto ela aparece pela primeira vez na posição {contagem2} e pela última vez em {contagem3}')


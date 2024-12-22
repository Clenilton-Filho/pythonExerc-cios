
#santo

frase = input('Digite uma frase: ').strip().lower()

pesquisa = str(frase.find('santo'))
contagem1 = pesquisa.replace('0','sim').replace('-1','não')

print(f'Começa com a palavra "santo"?: {contagem1}')

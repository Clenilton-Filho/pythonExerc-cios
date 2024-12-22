
#Silva

nome = input('Digite um nome: ').strip().lower()
contagem = str('silva' in nome).replace('True','sim').replace('False','não')
print(f'O nome digitado possui "Silva"?: {contagem}')

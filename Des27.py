#Primeiro e último nomes

nome = str(input('Digite um nome completo: ')).strip().lower()
find1 = nome.find(' ')
find2 = nome.rfind(' ')
primeiro = nome[:find1]
último = nome[find2:]
print(f'o primeiro nome é: {primeiro}, enquanto o último é: {último}'.format(find1,find2))

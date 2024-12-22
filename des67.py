while True:
    num = int(input('digite um número: '))
    if num >= 0:
        for c in range(1,11):
            print(f'{num} x {c} = {num * c}')
    else:
        print(f'{num} é negativo. Encerrando...')
        break



D= int(input('Digite a distancia da viagem : '))

if D <= 200 :
    Valor = D * 0.50
    print(f'O valor da viagem ficou R${Valor:.2f}')
else:
    Valor = D * 0.45
    print(f'O valor da viagem ficou R${Valor:.2f}')
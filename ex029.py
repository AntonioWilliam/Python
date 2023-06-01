
from time import sleep
V= int(input('Digite a velocidade do carro em KM/h: \n'))
print('-' * 15)
print('PROCESSANDO...')
print('-' * 15)
sleep(3)
if V > 80:
    print('MULTADO -- >GERANDO MULTA')
    sleep(3)
    multa = (V-80) * 7
    print(f'A multa ficou no valor de : R${multa:.2f}')
print('Tenha um bom dia! Dirija com cuidado')
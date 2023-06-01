

import random
from time import sleep #Importando o modulo time da biblioteca sleep para que tenha um tempo de espera

num = random.randint(0,5) # Gerou a number aleatoio
n=int(input('Try to guess the number I thought from 0 to 5 : \n'))
print('PROCESSANDO...')
sleep(3)
if n == num:
    print('Congratulations, you hit')
else:
    print(f'GAME OVER, I not thought on {n} and yes on {num} ')
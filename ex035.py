#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario
# se elas podem ou não formar um triângulo


# sempre que a
# soma das medidas dos segmentos que estão sendo girados for maior que a medida do terceiro segmento,
# é possível construir um triângulo.

r1 =float(input('Digite um valor para o lado do triângulo : '))
r2 =float(input('Digite um valor para o lado do triângulo : '))
r3 =float(input('Digite um valor para o lado do triângulo : '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')






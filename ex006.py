#Crie um algoritmo
# que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Type it a number : '))
double = num * 2
triple = num * 3
SquareRoot = num **(1/2)

print(f'The number chosen was {num}\n'
      f'Your double is : {double}\n'
      f'Your triple is : {triple}\n'
      f'Your square root is : {SquareRoot:.0f}')
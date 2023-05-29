#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

#Make a program that reads the lengths of the opposite and adjacent
# slides of a right-angled triangle, calculates and displays the length of the hypotenuse

cO = float(input("Enter value lengths opposite : \n"))
cA = float(input("Enter value lengths adjacent : \n"))
hy= (cO ** 2 + cA ** 2 ) ** (1/2)
#Formula para descobrir a hipotenusa, eleva os catetos ao quadrado e soma, após isso tira a raiz
print(f'The length hypotenuse is : {hy:.2f}')

##With library math

import math
Co=float(input("Enter a value leg opposite : \n"))
Ca=float(input("Enter a value leg adjacent : \n"))
hY = math.hypot(Co,Ca)
print(f'The length hypotenuse is : {hY:.2f} ')
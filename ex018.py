#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno
#cosseno e tangente desse angulo

#Make a program that reads any angle and displays the value of  sine, cosine and tangent that angle in screen

import math
Angle = float(input("Enter a value Angle : \n"))
#Convert  para radiano
Sine = math.sin(math.radians(Angle))
print(f'The sine of the Angle is : {Sine:.2f}')
Consine = math.cos(math.radians(Angle))
print(f'The cosine of the Angle is : {Consine:.2f}')
Tangent = math.tan(math.radians(Angle))
print(f'The tangent of the Angle is : {Tangent:.2f}')
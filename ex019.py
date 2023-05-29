#Um professor quer sortear um dos seus alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

# A teacher wants to draw one of his students to erase the blackboard.
# MAke a program that helps him, reading their names and writing the chosen name


import random
# Essa biblioteca serve para selecionar um valor aleatorio
a1 = input("Enter first Student name : \n ")
a2 = input("Enter second Student name : \n ")
a3 = input("Enter third Student name : \n ")
a4 = input("Enter fourth Student name : \n ")
#Create a List para armazenar o conteudo
list=[a1,a2,a3,a4]
chosen = random.choice(list)
print(f'The Student chosen to erase the blackboard he was : {chosen} ')

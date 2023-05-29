#O mesmo professor do desafio anterior quer sortear a ordem de
# apresentações de trabalhos dos alunos.
# faça um programa que leia onome dos quatros alunos e mostres a ordem sorteada

# The same teacher from  the previous challenge wants to draw lots for the order of student's
# presentations. Create a program that reads the names of the four students and displays the drawn
# order

import random
a1 = input("Enter first Student name : \n ")
a2 = input("Enter second Student name : \n ")
a3 = input("Enter third Student name : \n ")
a4 = input("Enter fourth Student name : \n ")
sortList = [a1,a2,a3,a4]
random.shuffle(sortList)
#Sorteia as posições dos conteudos da lista
print("the order of presentation will be : \n")
print(sortList)
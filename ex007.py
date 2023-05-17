#Desenvolva um programa que leia as duas notas de um aluno
# e calcule e mostre sua média

name = input('Type it a name : ')
n1=float(input('Type it your first note : '))
n2=float(input('Type it your second note : '))
media= (n1 + n2) / 2
print(f'Media of student :{name} he has {media:.1f} ')
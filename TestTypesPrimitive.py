# Descobrir o type da variable utilizamos the comand
n = input('Digite um valor')
print(n.isnumeric())

#Alfabeto
n = input('Digite um valor')
print(n.isalpha())

#Alfanumerico
n = input('Digite um valor')
print(n.isalnum())

#Letras maiusculas
n = input('Digite um valor')
print(n.isupper())

n1 = int(input('Type it a number : '))
n2 = int(input('Type it a number : '))
SumInt = n1 + n2
print('Sun is : {} '.format(SumInt) )

#n1 = float(input('Type it a number : '))
#n2 = float(input('Type it a number : '))
#SumFloat = n1 + n2
#print('Sun is : {} '.format(SumFloat) )

n1 = float(input('Type it a number : '))
n2 = float(input('Type it a number : '))
SumFloat = n1 + n2
#print('Sun in between', n1 , 'e', n2, ' vale {}'.format(SumFloat) )
print('Sum in between {} and {} is equals {}'.format(n1,n2,SumFloat))
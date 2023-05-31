

frase= 'Curso em Video Python'

 #Saber quantos caracteres existem na frase
print(len(frase))

#Contar quantas letras 'o' aparece na 'frase'
print(frase.count('o'))

#Mostra onde encontrou a sequencia 'deo'
print(frase.find('deo'))

#Operador in
print('Curso' in frase)

#Tranformação de caracteres
print(frase.replace('Python','Android'))

#Upper Tranforma em letra Maiuscula
print(frase.upper())

#Lower Transforma em letra minuscula
print(frase.lower())

#Capitalize
print(frase.capitalize())

#Title
print(frase.title())

fraseNEW = '   Aprendendo Python   '

print(fraseNEW)

#Strip --> tira espaço desnecessarios
print(fraseNEW.strip())

#StripR --> tira espaços do lado direito
print(fraseNEW.rstrip())

#StripL --> tira espaços do lado Esquerdo
print(fraseNEW.lstrip())

#Split --> Gera uma lista em cada palavra
print(frase.split())

#'-'.join --> junta as palvras pelo '-'
print('-'.join(frase))
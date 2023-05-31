#Create a program that read name of a city and
# say whether or not it starts with the word 'Santo'

city = input('Type in the name of a city : \n').strip() #Tirando espaços

#Nesse print ocorre que, ele encontra a palavra santo em qualquer posição
print('Santo' in city)

#A forma correta de fazer é :
print(city[:5] == 'Santo')

#Correção de mais um erro, acontece que se digitar com letras maiusculasou minusculas, vai dar errado ...
print(city[:5].upper() == 'SANTO')
#ou
print(city[:5].lower() == 'santo')

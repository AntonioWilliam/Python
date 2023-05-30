#

Name = input('Enter your name complete : \n')
print('Analyzing name...')


print('Your name in upper letters is : ')
print(Name.upper())

print('Your name in lower letters is : ')
print(Name.lower())

print('Your name at all : ', len(Name.replace(" ","")),' letters')
#Aqui usamos o replate para trocarmos os espaços " " por ""

List= Name.split()
print('Your first name is ', List[0], ' and at ', len(List[0]), "letters")


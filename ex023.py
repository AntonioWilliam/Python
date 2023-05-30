
n=int(input('Type it a number: '))
u= n // 1 % 10
d= n // 10 % 10
c= n // 100 % 10
m= n // 1000 % 10

#print('Unit : ', n[3])
#print('Ten : ', n[2])
#print('Hundred : ', n[1])
#print('Thousent : ', n[0])

print(f'Unit : {u}')
print(f'Ten : {d}')
print(f'Hundred : {c}')
print(f'Thousent : {m}')


#Veja os exemplos abaixo.
#Divisão: 1234 / 10 = 123,4
#Divisão inteira: 1234 //10 = 123
#Módulo: 1234 % 10 = 4
#Pra  descobrir a centena faz isso:
#Faz a divisão inteira por 100: 1234 // 100 = 12
#Depois pega o resultado e dividi por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2
#Ou seja, a centena é 2.
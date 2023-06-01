
n1= int(input('Digite um número'))
n2= int(input('Digite um número'))
n3= int(input('Digite um número'))

menor = n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3

maior = n3
if n1 > n3 and  n1>n2:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2

print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')


#Outra maneira de resolver é utilizando o .sorte(), que organiza a lista em ordem crescente

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite um último número: '))
#cria uma lista chamada l
l = [a, b, c]
#utiliza o metodo .sort com a lista(l)
l.sort()
print(f'O maior número é {l[2]} e o menor é {l[0]}')

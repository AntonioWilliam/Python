#Faça um algoritmo que leia o preço de um produto e
#mostre seu novo preço, com 5% de desconto

p=float(input('Type it price of product:\n'))
des= p - p*0.05
print(f'Value product is R${p}, but with discont of 5% it was left R${des:.2f}')
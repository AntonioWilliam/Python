#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar

wallet = float(input('How much do you have in your wallet : \n'))
Dollar = float(input('What is the current of dollar exchange rate : \n'))
con= wallet / Dollar
print(f'You can buy U${con:.2f} dollars')
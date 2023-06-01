# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Pra salários supeiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

Salario = float(input('Digite seu salário para calcularmos seu aumento : '))

if Salario <= 1250.0:
    Aumento = Salario + (Salario * 0.15)
else:
    Aumento = Salario + (Salario * 0.10)

print(f'O novo salário é : R${Aumento:.2f}' )
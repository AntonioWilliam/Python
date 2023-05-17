# Write a program that to ask amount of KM
# traveled per a car rented and amount days for which it was rented
# Calculate the price pay, knowing that car cust R$60 day and R$0.15 per kKM driven

days = int(input('Per how many days the car was rented :\n'))
KM =  float(input('Type it how much KM were driven :\n'))
calc = (60 * days) + (0.15 * KM)
print(f'Value of rent is : R${calc}')
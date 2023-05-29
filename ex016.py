# Create a program that write any Real number
# using the keyboard and display its entire part on the screen
import math

number = float(input("Enter a Real  number : "))
print(f'Its entire part is {number:.0f} ')


from math import trunc
numberM = float(input("Enter a Real  number : "))
print(f'Its entire part is {math.trunc(number)} ')

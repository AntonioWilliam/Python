#Escreva um programa que leia um valor em metros
# e exiba convertido em centimetros e milimetros

vMeters = float(input('Type it value from vMeters : '))
dm= vMeters * 10
centimeter = vMeters * 100
millimeter = vMeters * 1000

dam = vMeters / 10
hm = vMeters / 100
kilometer = vMeters / 1000


print(f'vMeters = {vMeters}\n'
      f'in Dm = {dm:.0f}dm\n'
      f'in Centimeter = {centimeter:.0f}cm\n'
      f'in Millimeter = {millimeter:.0f}mm\n'
      f'in dam = {dam:.3f}dam\n'
      f'in hm = {hm:.3f}hm\n'
      f'in Kilometer = {kilometer}km')

width=float(input('Type it width wall:\n'))
heigth=float(input('Type it heigth wall:\n'))
d= width*heigth
print(f'The dimensions wall is : \n'
      f'{width}x{heigth}={d}m²\n'
      #Para cada 2m² é utilizado 1 litro de tinta
      f'Para pintar essa parede sera utilizado {d/2}l de tinta')
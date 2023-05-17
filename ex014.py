# Write a program that converts a temperature typed in °C for °F and °K.

temperatureC = float(input('Type it temperature in Celsius: \n'))
print(f'{temperatureC}°C')
temperatureK = temperatureC + 273
print(f'Temperature converted in Kevin is : {temperatureK}°K')
temperatureF= 1.8 * temperatureC + 32
print(f'Temperature converted in Fahrenheit is : {temperatureF}°F')
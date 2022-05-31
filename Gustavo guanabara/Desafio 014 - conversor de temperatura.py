import os
os.system("clear") or None

# Conversor de temperaturas

# Escreva um programa que converta uma temperatura de Celsius (°C) para Fahrenheit (°F)

Celsius =  float(input('Temperatura em Celsius (°C): '))

Fahrenheit = Celsius * 1.8 + 32

print(f'{Celsius}°C convertidos para Fahrenheit fica {Fahrenheit}°F')

import os
os.system("clear") or None

# Faça um programa que leia a largura e a altura de uma parede em metros, Calcule a sua area e a quantidade de tinta nescessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m2.

largura = float(input('Digite a largura em mt: '))
altura = float(input('Digite a altura em mt: '))

area = largura * altura

resultado = area / 2

print(f'Para cobrir {area} metros de area de pintura, Será nescessário {resultado} litros de tinta para fazer toda a pintura')

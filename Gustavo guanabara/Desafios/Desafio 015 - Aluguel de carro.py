import os
os.system("clear") or None

# Aluguel de Carros

# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado, e a quantidade de dias pelos quais ele ficou alugado.Calcule o preço a pagar, Sabendo que o carro custa R$ 60.00 por dia e R$ 0,15 por Km rodado

km = float(input('Quantos Km Percorreu?: '))
Dias = int(input('Quantidade de dias alugado?: '))

pagamento = (km * 0.15) + (Dias * 60)
print()
print(f'O valor total a pagar será de {pagamento:.2f} reais')
print()

# Aluguel de Carros

# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado, e a quantidade de dias pelos quais ele ficou alugado.Calcule o preço a pagar, Sabendo que o carro custa R$ 60.00 por dia e R$ 0,15 por Km rodado

km = float(input('Km Percorridos?: '))
Dias = int(input('Alugado por quantos Dias?: '))

pagamento = (km * 0.15) + (Dias * 60)

print('O valor total a pagar será de {:.2f}'.format(pagamento))

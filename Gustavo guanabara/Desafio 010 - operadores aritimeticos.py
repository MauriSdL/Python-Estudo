
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

cotacao = float(input('Qual a cotação do dollar hoje?: '))
reais = float(input('Quantos reais voçê tem em carteira? '))

dollar = cotacao
resultado = reais / 5.13

print('Você cosegui comprar {:.2f} dollar com {} reais'.format(resultado, reais))

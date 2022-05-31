import os
os.system('clear') or None

# faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Produto = (input('Produto: '))
valor_total = float(input('Valor do produto: '))
porcentagem = int(input('Desconto em porcentagem: '))

desconto = (porcentagem * valor_total) / 100
valor_a_cobrar = valor_total - desconto

print(f'O produto {Produto} com {porcentagem}% de desconto custará {valor_a_cobrar:.2f} reais')

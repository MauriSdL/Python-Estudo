
# faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Produto = (input('Produto: '))
valor_total = float(input('Valor do produto: '))
porcentagem = int(input('Desconto em porcentagem: '))

desconto = (porcentagem * valor_total) / 100
valor_a_cobrar = valor_total - desconto

print('O produto {} com {}% de desconto custará {:.2f} reais'.format(Produto, porcentagem, valor_a_cobrar))

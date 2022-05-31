import os
os.system("clear") or None

# Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de almento.
print()
print('Aumento de salario')
print()
salario = float(input('Salario atual?: '))
porcentagem = float(input('Adicione a (%) de aumento: '))

calculo = ( salario * porcentagem) /100
aumento = salario + calculo
print()
print(f'O Salário de {salario:.2f} reais, Passará a ter o valor de {aumento:.2f} reais, tendo um aumento de {calculo:.2f} de reais a mais, em seu novo Salário.')
print()
print()

# Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de almento.
print()
print('Calculo aumento de salario')
print()
salario = float(input('Salario atual?: '))
porcentagem = float(input('Adicione a (%) de aumento: '))

calculo = ( salario * porcentagem) /100
aumento = salario + calculo
print()
print('O Salário de {:.2f} reais, Passará a ter o valor de {:.2f} reais, tendo um aumento de {:.2f} de reais a mais, em seu novo Salário.'.format(salario, aumento, calculo))
print()
print()
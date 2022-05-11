
# Escreva um programa que leia um valor em metros e o exiba covertido em centimetros e milimetros.

metros = float(input('Digite uma metragem: '))
cm = metros * 100
mm = metros * 1000
print('{} metro covertidos em centimetros fica {} cm'.format(metros,  cm))
print('{} metro ou centimetro convertidos em milimetros fica {} mm'.format(metros, mm))

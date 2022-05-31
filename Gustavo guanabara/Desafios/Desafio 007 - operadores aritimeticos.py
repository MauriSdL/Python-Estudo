import os
os.system('clear') or None

# Desenvolva um programa que leia as duas notas de um aluno, Calcule e mostre a sua media

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print('A media do aluno foi', media)

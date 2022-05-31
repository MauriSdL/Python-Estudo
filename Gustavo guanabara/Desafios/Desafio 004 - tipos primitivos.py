import os
os.system('clear') or None

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

Digitado = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(Digitado))
print('É apenas numero? ', Digitado.isnumeric())
print('Esta tudo em minusculo? ', Digitado.islower())
print('Está tudo em maisculo? ', Digitado.isupper())
print('Pode ser impresso? ', Digitado.isprintable())
print('É alfanumerico(é numero e letras)? ', Digitado.isalnum())
print('É alfabetico(é apenas letra)? ', Digitado.isalpha())
print('Só tem espaços digitados(sem letra ou numero apenas espaços)? ', Digitado.isspace())
print('Esta capitalizada? ', Digitado.istitle())
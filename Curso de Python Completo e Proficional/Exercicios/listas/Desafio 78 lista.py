import os
os.system("clear") or None

# Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o maior valor digitado e as suas respectivas posiçoes no lista.

lista = []
maiorValor = 0
menorValor = 0

for c in range(0, 5):
    lista.append(int(input("Digite um valor para a Posição {}: ".format(c))))
    if c ==0:
        maiorValor = menorValor = lista[c]
    else:
        if lista[c] > maiorValor:
            maiorValor = lista[c]
        if lista[c] < menorValor:
            menorValor = lista[c]




print('=-' * 22)
print("Voçe digitou os valores {}".format(lista))

print("O maior valor digitado foi {} na posiçao".format(maiorValor), end='')
for i, v in enumerate(lista):
    if v == maiorValor:
        print(". {} ...".format(i))


print("O menor valor digitado foi {} na posiçao".format(menorValor), end='')
for i, v in enumerate(lista):
    if v == menorValor:
        print(". {} ...".format(i))
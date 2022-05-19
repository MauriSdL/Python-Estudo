import os
os.system("clear") or None
# listas

# O primeiro indice de uma lista é 0 depois 1 depois 2 assim por diante
# sempre que quiser mostrar um item da lista coloque um numero maior porque o ultimo nao é mostrado
# listas criadas usanso []
# As listas sao separados por indices  de forma ordenada que vao do 0, 1, 2, 3,por diante
# As lista sao mutaveis que significa que pode ser add ou retirado qualquer item da lista
# --> todos os itens adcionados vao para u ultimo indice da lista
# As lista permitem add item que ja tem na lista, ob: isso acontece porque os itens da lista sao identificados pelos seus indices e naom pelo nome.

lista = ["maça", "bana", "cereja", "maça", "CEREJA"]
print(lista)
print(len(lista)) # len mostra a quantidade de itens na lista
lista2 = [1, 5, 7, 9, 3]

lista3 = [True, False, False]
lista4 = ["Mauri", 1975, True]
print(type(lista))

# usando funçao contrutora de lista
# A função contrutora de lista é composta de list((  ))

lista5 = list(("carro", "moto", "caminhao"))
print(lista5)

# Acessar itens  da lista
lista5 = list(("Mauri", "Nara", "Zilda", "Deise", "Pedro", "Iracy", "Kerlly", "Sandra"))
print(lista5[2])
print(lista5[-2]) # sinal negativo faz a contagem começar de traz ate o inicio da lista
print(lista5[2:5])# mostra do 2 ao 5 item da lista
print(lista5[:4])
print(lista5[3:])
print(lista5[-4:-1])
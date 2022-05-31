
# Remover itens da lista

import os
os.system("clear") or None

nomes = ["Gabriel", "Danny", "Arthur"]
nomes2 = ["Lucas", "Flavio", "Gustavo", "Adriano", "Daiana"]

# remove ==> Remove item da lista pelo seu nome
#nomes.remove("Danny")

# pop ==> Remove um iten da lista pelo seu indice
#nomes.pop(0)

# pop para remover apenas o ultimo item da lista(tem duas formas de fazer isso)
#nomes.pop(2)
#nomes2.pop()

# Metodo del ==> Remove um item da lista atraves de seu indice
#del nomes[1]

# Remover a lista inteira
# OBS: Se usar del para remover a lista inteira vai aparecer um erro (isso é normal ja que toda a lista foi apagada por completo acusa que nao existe uma variavel com a lista para poder apagar)
#del nomes

# Remover todos os itens da lista sem apagar a variavel
nomes.clear()


print()
print()
print()
print(nomes)
print(nomes2)
print()
print()
print()
print()

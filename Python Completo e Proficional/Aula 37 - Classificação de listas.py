import os
os.system("clear") or None

# Classificação de listas tem prioridade Primeiro letras Maiusculas de pois minusculas

nomes = ['Gabriel', 'danny', 'Arthur', 'Joao', 'Beatriz']
numeros = [100, 50, 65, 82, 23]

# sort ==> Organizar lista de forma acedente(crecente, ordem alfabetica)
#nomes.sort()
#numeros.sort()

# Classificação de listas em ordem crecente sem prioridade de Maisusculas e minusculas
#nomes.sort(key = str.lower)

# Organizar lista de forma descedente (do maior ao menor )(alfabeto de traz para frente)
#nomes.sort(reverse = True)
#numeros.sort(reverse = True)

# Definir lista atraves de uma funcao com a palavra chave key
# Coloca a lista em ordem de acordo com o valor mais proximo do valor key

'''
def myfunction(n):
    return abs(n - 50)
numeros.sort(key = myfunction)
'''

# Inverter a ordem de sentido da lista (muda os valores de traz colocando-os na frente)
nomes.reverse()
numeros.reverse()

print(nomes)
print(numeros)

import os

os.system("clear") or None # se nao colocar or none o terminal retorna um valor inteiro


# imprimir apenas uma letra de uma palavra
nome = 'Mauri'
print(nome[2])
print()
# no Python a contagem sempre começa com zero

# imprimir cada letra de uma palavra
for nome in "Mauri":
    print(nome)
print()

# contar a quantidade de caractere de uma palavra (OBS: Os espaços tambem são contados)
nome = 'Mauri Sebastiao da Luz'
print(len(nome))
print()

# verificar se uma palavra esta em uma frase
txt = "Seja bem vindo ao curso de Python."
x = "vindo" in txt
print(x)
print("carro" in txt)
print()

# Escrita em tudo em minusculo e maiusculo
nome = "   Mauri Sebastiao da Luz   "
print(nome.lower()) # tudo em minusculo
print(nome.upper()) # tudo em maiusculo
print(nome.replace("Sebastiao", "Lindao")) # replace fa a subistituçao de uma coisa pela outra
print(">" + nome.strip() + "<") # Remove o espaços do começo e fim deixando só os espaços entre as palavras

# separar criando uma lista com split
a = "carro, moto, caminhão"
print(a.split(","))
print()

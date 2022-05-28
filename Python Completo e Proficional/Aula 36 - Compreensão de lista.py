import os
os.system("clear") or None

nomes = ["Gabriel", "Danny", "Arthur", "Joao", "Lucas", "Paula"]
novaLista = []
'''
# Ex: sem Compreensão de lista
for x in nomes:
    if "u" in x:
        novaLista.append(x)

print(novaLista)
print()
'''

# Compreensão de lista
#novaLista = [x for x in nomes if "u" in x]
#novaLista = [x for x in nomes if x != "Danny"]
#novaLista = [x for x in nomes]
#novaLista = [x for x in range(10)]
#novaLista = [x for x in range(10) if x % 2 == 0]
#novaLista = [x for x in range(10) if x % 2 != 0]
novaLista = [x if x != "Danny" else "Danielle" for x in nomes]
print(novaLista)

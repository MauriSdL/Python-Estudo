
import os
os.system("clear") or None

nomes = ["Gabriel", "Danny", "Arthur"]

# Iterando com loop nas listas
'''
for x in nomes:
    print(x)
'''

# Interando com loop nas listas por indice
"""
for i in range(len(nomes)):
    print(nomes[1])
"""

# Interando com loop while
'''
i = 0
while i < 3:
    print(nomes[i])
    i += 1
'''

# Compreenção de lista
[print(x) for x in nomes]
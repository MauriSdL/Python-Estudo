import os
os.system("clear") or None

# Juntar Listas
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
#list3 = list1 + list2

# Adicionar item por item de uma lista a outra
'''
for x in list2:
    list1.append(x)
print(list1)
'''
# segunda forma de juntar listas
list1.extend(list2)
print(list1)

print()
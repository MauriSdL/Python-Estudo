
# Operadores de identidade
# serve para compara objetos não somente se eles sao iguais , mas sim se estao no mesmo local de memoria(na mesma variavel)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) 
print(x is y)
print(x == y)

print(x is not z)
print(x is not y)
print(x != y)
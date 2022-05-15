import random
# Tipos de Dados em Python

# Tipos de texto:     str
# Tipos de numéricos: int, float, complex
# Tipos de seguencia: list, tuple, range
# Tipo de mapeamento: dict
# Tipos de conjuntos: set, frozenset
# Tipo booleano:      bool
# Tipos binários:     bytes, bytearray, memoriyview


# Definir tipos de dados

# str        --> var = 'hello word'
# int        --> var = 20
# float      --> var = 20.5
# complex    --> var = 1j
# list       --> var = ["apple", "banana", "cherry"]
# tuple      --> var = ("apple", "banana", "cherry")
# range      --> var = range(6)
# dict       --> var = {"name" : "john", "age" : 36}
# set        --> var = {"apple", "banana", "cherry"}
# frozenset  --> var = frozenset({"apple", "banana", "cherry"})
# bool       --> var = true
# bytes      --> var = b"hello"
# bytearray  --> var = bytearray(5)
# memoryview --> var = memoryview(bytes(5))


# fazendo casting(definir)

# str
x = "20"
print(type(x))

# int
x = int("20")
print(type(x))

# complex
varA = 3+5j
varB = 5j
varC = -5j
print(type(varA))
print(type(varB))
print(type(varC))


# numeros aleatorios
# import random
num = random.randrange(1, 10)
print(num)
print(random.randrange(1, 10))

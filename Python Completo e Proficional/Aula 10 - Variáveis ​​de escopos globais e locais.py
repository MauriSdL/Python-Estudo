
# Alterando Variáveis globais e locais
# Para importar uma variavel global dentro de uma função, Deve usar a palavra global seguido do nome da variavel dentro da funçao 

from re import X

x = 'incriveis'

def myFunc():
    global  X
    x = 'inacretitavel'
    y = 'fantastico'
    global z
    z = 'Bem vindo ao curso'
    print('Python é ' + x + ' e ' + y)
    print(z)

myFunc()

print('==============================')
print('Voçê é ' + x)
print(z)

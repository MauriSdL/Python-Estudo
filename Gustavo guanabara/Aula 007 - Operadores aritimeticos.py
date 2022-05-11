# Operadores aritimeticos
# + soma
# - subtração
# * multiplicação
# / divisão
# ** exponenciação
# // divisão inteira
# % resto da divisão
# == igual (apenas 1 sinal = é recebe, 2 sinal == é igual)ex: 5 == 5 resposta true

# 5 + 2 == 7
# 5 - 2 == 3
# 5 * 2 == 10
# 5 / 2 == 2.5
# 5 ** 2 == 25
# 5 // 2 == 2
# 5 % 2 == 1

# Ordem de precedencia
# 1 ()
# 2 **
# 3 * / // %
# 4 + -

 # Operador de Potência
 # 4 ** 3 == 64 sem Operador de Potência
 # pow(4, 3) == 64 com Operador de Potência Obs: com Operador de Potência vc perde a ordem de precedencia

 # multiplicar str
 # 'oi' * 5 == oioioioioi
 # '=' * 10 == ===========

 # Determinando quantidade de espaços e Preenchimento de espaços e centralizar dentro do espaço

# {:9}8 quantidade de espaços
# {:>9} alinhado a direita
# {:<9} alinhado a esquerda
# {:^9} alinhado ao centro
# {:=^9} (Obs: sem espaço depois do sinal de =)alinhado ao centro no meio do sinal de igual mas pode ser qualquer outra coisa no lugar do sinal igual

'''
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:9}!'.format(nome))
print('Prazer em te conhecer {:>9}!'.format(nome))
print('Prazer em te conhecer {:<9}!'.format(nome))
print('Prazer em te conhecer {:^9}!'.format(nome))
print('Prazer em te conhecer {:=^9}!'.format(nome))
'''

# Quantidade de casa depois da virgula ou ponto
# {:.3f} Sempre depois dos : colocar . Quantidade de casa e f fignifica formatar Ex:
gasto = float(input('Digite um valor extenço: '))
print('voce gastou \n{:.4f}'.format(gasto), end=' ')
print('valor real', {gasto})

# comando para não quebrar a linha
# no fim coloque isso , end='' (aspas vazias ou com um espaço para nao ficar grudado)

# comando para quebrar(pular) linha
# \n

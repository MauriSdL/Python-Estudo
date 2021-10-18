
# Desafio 028     Jogo da Adivinhaçao V.1.0
#                     condiçoes if else

# Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5
# e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador
# O programa devera escrever na tela se o usuario venceu ou se perdeu.

from random import randint
from time import sleep
computador = randint(0, 10) #Faz o computador 'pensar' em um numero aleatorio dentro dos valores
# Que estao entre parentezes
print()
print(' -*- ' * 15)
print('                                    Jogo de Adivinhaçao')
print()
print('     Estou pensando em um Numero de 0 a 10. Tente Adivinhar.')
print(' -*- ' * 15)
print('')
jogador = int(input('     Em que numero eu estou Pensando de 0 a 10 ?: ')) # jogador tenta Adivinhar
print('PROCESSANDO...') # Simula que o computrador esta processando eu carregando a informaçao
sleep(0.5) # O valor colocado dentro do parentezes é o tempo informado para espera
# Do print de processamento

#Estrutura condicional if e else
if jogador == computador: # OBS: A instrutura de condiçao nao funciona
# Se vc nao colocar os (:) depois do if e else
    print('')
    print('Surpreendente PARABENS')
    print('Um Humano conseguiu me Vencer!')
    print('')
    print('Que tal Melhor de 3 ?')
else:
    print('GANHEI ! kkk')
    print('')
    print('Eu Pensei em {}, Você escolheu o numero {}.'.format(computador, jogador))
    #print('Eu Pensei no numero', computador)
    #print('Você escolheu o Numero', jogador,)
    print('')
    print('Uma nova tentativa aumenta as chances de acertar.')

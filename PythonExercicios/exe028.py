#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
num = random.randrange(6)
user_num = int(input('O computador irá "pensar" em um número entre 0 e 5, digite '
                     '\no número que você acha que o computador pensou: '))
if user_num == num:
    print('Parabéns você GANHOU ao usar o número {}, e o computador pensou este número: {}.'.format(user_num, num))
else:
    print('Você PERDEU ao usar o número {}, o computador pensou no número: {}!'.format(user_num,num))

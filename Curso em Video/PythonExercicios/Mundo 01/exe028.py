__author__ = 'pablosoaresz'

#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
num = random.randrange(6)
#Ou
#from random import randint
#comput = randint(0, 5)

user_num = int(input('Vou pensar em um número entre 0 e 5. Em que número eu pensei? '))

print('Processando...')
sleep(3)

print('-=-' * 25)
if user_num == num:
    print('Parabéns você GANHOU ao usar o número {}, eu pensei nele mesmo! ^_~'.format(user_num, num))
else:
    print('Você PERDEU ao usar o número {}, eu pensei no número: {}! Muhauhuahuahauha'.format(user_num,num))
print('-=-' * 25)

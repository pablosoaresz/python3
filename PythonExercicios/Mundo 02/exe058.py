__author__ = 'pablosoaresz'

# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinar até acertar, mostrando no final quantos palpites foram necessários para vencer.


# import random
# erros = 0
# numero = random.randrange(11)
# usuario = int(input('Pensei em um número entre 0 e 10. \nAdvinhe qual número eu pensei! '))
# while usuario != numero:
#    erros += 1
#    usuario = int(input('Errou! Digite novamente: '))
# print('Você errou {} vezes até acertar.'.format(erros))
# print('Pensei no número {}.'.format(numero))

# Ou

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

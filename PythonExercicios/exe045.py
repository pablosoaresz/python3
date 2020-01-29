__autor__ = 'pablosoaresz'
# Crie um programa que faça o computador jogar Jokenpô(Pedra, Papel, Tesoura) com você.

'''
import random
computer = random.randrange(3)
# Computer == 0 = Pedra;
# Computer == 1 = Papel;
# Computer == 2 = Tesoura;

Regras do jogo:
Pedra ganha de tesoura
Tesoura ganha de papel
Papel ganha de pedra

player = int(input('Digite =1= para Pedra, =2= para Papel e =3= para Tesoura: '))

pickedComputer = ''
if computer == 0:
    pickedComputer = 'Pedra'
elif computer == 1:
    pickedComputer = 'Papel'
elif computer == 2:
    pickedComputer = 'Tesoura'

pickedPlayer = ''
if player == 1:
    pickedPlayer = 'Pedra'
elif player == 2:
    pickedPlayer = 'Papel'
elif player == 3:
    pickedPlayer = 'Tesoura'
print('-=-' * 15)
print('Computador jogou com: {}.'.format(pickedComputer))
print('-=-' * 15)
print('Jogador jogou com: {}'.format(pickedPlayer))
print('-=-' * 15)
print('')
print('-*-' * 15)

# Jogador joga com 'Pedra':

if computer == 0 and player == 1:
    print('Empate! {} empata com {}.'.format(pickedPlayer, pickedComputer))
elif computer == 1 and player == 1:
    print('Você perdeu! {} ganha de {}'.format(pickedPlayer, pickedComputer))
elif computer == 2 and player == 1:
    print('Você ganhou! {} ganha de {}'.format(pickedPlayer, pickedComputer))

# Jogador joga com 'Papel':

elif computer == 0 and player == 2:
    print('Você ganhou! {} ganha de {}.'.format(pickedPlayer, pickedComputer))
elif computer == 1 and player == 2:
    print('Empate! {} empata com {}.'.format(pickedPlayer, pickedComputer))
elif computer == 2 and player == 2:
    print('Você perdeu! {} perde de {}.'.format(pickedPlayer, pickedComputer))

# Jogador joga com 'Tesoura':

elif computer == 0 and player == 3:
    print('Você perdeu! {} perde de {}.'.format(pickedPlayer, pickedComputer))
elif computer == 1 and player == 3:
    print('Você ganhou! {} ganha de {}.'.format(pickedPlayer, pickedComputer))
elif computer == 2 and player == 3:
    print('Empate! {} empata com {}.'.format(pickedPlayer, pickedComputer))
print('-*-' * 15)

'''
from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA.')

elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    if jogador == 1:
        print('COMPUTADOR VENCE')
    if jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

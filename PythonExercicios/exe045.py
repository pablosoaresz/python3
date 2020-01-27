__autor__= 'pablosoaresz'
# Crie um programa que faça o computador jogar Jokenpô(Pedra, Papel, Tesoura) com você.

import random
computer = random.randrange(3)
# Computer == 0 = Pedra;
# Computer == 1 = Papel;
# Computer == 2 = Tesoura;
'''Regras do jogo:
Pedra ganha de tesoura
Tesoura ganha de papel
Papel ganha de pedra'''

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

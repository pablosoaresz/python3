#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

nomes = ('José', 'Maria', 'João', 'Augusto')
print(random.sample(nomes, k=4))

#Um professor quer sortear um dos seus quatro alunos para apagar o quadr.
#Faça um programa que ajude ele lendo o nome deles, e escrevendo o nome escolhido.

import random
nomes = ('a','b','c','d')

print(random.sample(nomes, k=1))

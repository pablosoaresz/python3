#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print(nomes)

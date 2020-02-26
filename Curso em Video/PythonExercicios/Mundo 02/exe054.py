__author__ = 'pablosoaresz'

# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade(21 anos) e quantas já são maiores.

from datetime import date
maior_idade = 0
menor_idade = 0
for c in range(1, 8):
    n = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade_hoje = date.today().year - n
    if idade_hoje < 21:
        menor_idade += 1
    else:
        maior_idade += 1
print('São {} maiores de idade, e {} menores de idade'.format(maior_idade, menor_idade))

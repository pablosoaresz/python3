# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior; - O segundo valor é maior; - Não existe valor maior, os dois são iguais.

n1 = int(input('Digite um número Inteiro: '))
n2 = int(input('Ditite outro número Inteiro: '))
if n1 > n2:
    print('{} é maior que {}.'.format(n1, n2))
elif n1 < n2:
    print('{} é maior que {}.'.format(n2, n1))
elif n1 == n2:
    print('{} e {} são iguais.'.format(n1, n2))

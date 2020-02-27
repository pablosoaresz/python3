__author__ = 'pablosoaresz'

# Crie um programa que leia vários números interos pelo teclado. O programa só vai parar quando o usuário digitar o valor
# 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (descon-
# siderando o flag 999).

n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Foi digitado {} números e a soma entre eles foi {}!'.format(cont, soma))

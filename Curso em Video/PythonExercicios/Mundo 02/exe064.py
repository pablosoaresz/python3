__author__= 'pablosoaresz'

# Crie um programa que leia vários números interos pelo teclado. O programa só vai parar quando o usuário digitar o valor
# 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (descon-
# siderando o flag 999).

numero = int(input('Digite um número diferente de 999: '))
while numero != 999:
    numero += numero

__author__ = 'pablosoaresz'

# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digi-
# tado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
    else:
            print('Número digitado é ímpar!')
print('Foi digitado {} números PARES e a soma deles é {}.'.format(cont, soma))

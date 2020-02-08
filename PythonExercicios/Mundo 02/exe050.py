__author__ = 'pablosoaresz'

# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digi-
# tado for ímpar, desconsidere-o.

s = 0
for c in range(1, 7, +1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
    else:
            print('Número digitado é ímpar!')
print(s)

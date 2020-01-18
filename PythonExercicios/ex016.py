# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.
# Use a biblioteca 'math.

#import math
from math import trunc
num = float(input('Digite um número Real: '))
print('O número digitado foi {}, e sua parte inteira é {}.'.format(num, trunc(num)))
print('O número digitado foi {}, e a sua parte inteira é {} impresso usando "int".'.format(num, int(num)))

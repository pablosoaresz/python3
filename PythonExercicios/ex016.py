#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.
#Use a biblioteca 'math'.

import math
num = float(input('Digite um número Real: '))
print(math.trunc(num))
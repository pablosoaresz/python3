# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule
# e mostre o comprimento da hipotenusa

#import math
from math import hypot
catop = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
#hipot = math.hypot(catop, catadj)
hipot = hypot(catop, catadj)
hipote = (catop ** 2 + catadj ** 2) ** (1/2)
print(
    'Usando a importação do método "hypot" do módulo "math" a hipotenusa vai medir {:.2f}.'.format(hipot))
print(
    'Usando o método matemático, a hipotenusa irá medir {:.2f}.'.format(hipote))

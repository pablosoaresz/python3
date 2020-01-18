# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse ângulo

#import math
from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
#print(math.sin(angulo), math.cos(angulo), math.tan(angulo))
#print('O seno é {}, o coseno é {}, e a tangente é {}.'.format(math.sin(angulo), math.cos(angulo), math.tan(angulo)))
#print('O seno é {}, o coseno é {} e a tangente é {}'.format(sin(angulo), cos(angulo), tan(angulo)))
print('O angulo {} tem o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}'.format(
    angulo, seno, cosseno, tangente))

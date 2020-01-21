__autor__= 'pablosoaresz'
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos apresentados FORMAM um triângulo.')
else:
    print('Os segmentos apresentados NÃO formam um triangulo.')

#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule
# e mostre o comprimento da hipotenusa

import math

catop = float(input('Digite o valor do Cateto Oposto: '))
catadj = float(input('Digite o valo do Cateto Adjacente: '))
hipot = math.hypot(catop, catadj)
print(hipot)
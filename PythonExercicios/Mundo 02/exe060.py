__author__= 'pablosoaresz'

# Faça um programa que leia um número qualquer e mostre o seu fatorial:
# Ex: 5! = 5x4x3x2x1=120

numero = int(input('Digite um número: '))

while numero != 1:
    fatorial = numero * (numero -1)

print(fatorial)

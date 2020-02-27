__author__ = 'pablosoaresz'

# Faça um programa que leia um número qualquer e mostre o seu fatorial usando 'for':
# Ex: 5! = 5x4x3x2x1=120

n = int(input('Digite um número: '))
cont = n
fatorial = 1
for cont in range(cont, 1, -1):
    fatorial *= cont
    cont -= 1
print(fatorial)

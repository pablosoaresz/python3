__author__ = 'pablosoaresz'

# Faça um programa que leia um número qualquer e mostre o seu fatorial:
# Ex: 5! = 5x4x3x2x1=120

num = int(input('Digite um número: '))
cont = num
fatorial = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))

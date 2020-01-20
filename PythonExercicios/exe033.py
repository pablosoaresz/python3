__autor__= 'pablosoaresz'
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

lista = (n1, n2, n3)

print('O maior número apresentado foi o {}, e o menor foi o {}.'.format(max(lista), min(lista)))

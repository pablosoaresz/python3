#Faça um programa que leia o número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Ex: Digite um número: 1834
#Unidade: 3
#Dezena: 3
#Centena: 8
#Milhar: 1

num = int(input('Digite um número entre 0 a 9999: '))
n = str(num)
print( 'Analisando o número {}...' .format(num) )
print( 'Unidade: {}.'.format(n[3]) , '\nDezena: {}.' .format(n[2]) ,
        '\nCentena: {}' .format(n[1]) , '\nMilhar: {}.' .format(n[0]) )
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('===' * 8)
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

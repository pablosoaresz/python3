#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou íMPAR.
__autor__= 'pablosoaresz'
num = int(input('Digite um número: '))
resto = num % 2
print(resto)
if resto == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))

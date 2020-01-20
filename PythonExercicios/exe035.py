__autor__= 'pablosoaresz'
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
if (n1 + n2 <= n3) and (n1 + n3 <= n2) and (n2 + n3 <= n1):
    print('Os valores apresentados podem formar um triângulo.')
else:
    print('Os valores apresentados não formam um triangulo.')

__author__ = 'pablosoaresz'

# Faça um programa que calcule a soma entre todos os números ímpares que são multiploes de três e que se encontram no
# intervalo de 1 até 500.
s = 0
for c in range(1, 501, +1):
    if c % 3 == 0:
        s += c
print(s)

# Resposta correta abaixo
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # Números ímpares divisíveis por 3
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))

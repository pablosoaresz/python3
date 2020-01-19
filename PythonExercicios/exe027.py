#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza

nome = str(input('Digite seu nome: ').strip())
dividido = nome.split()
print('O primeiro nome é: {}, e o ultimo nome é: {}.'.format(dividido[0], dividido[-1]))
# OU
print('O primeiro nome é: {}, e o último nome é: {}.'.format(dividido[0], dividido[len(dividido)-1]))

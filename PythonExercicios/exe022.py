#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1- O nome com todas as letras maiúsculas
#2- O nome com todas minúsculas
#3- Quantas letras ao todo (sem considerar espaços)
#4- Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome, usando letras maiúsculas e minúsculas: ')).strip()
print('Analisando...')
print('Seu nome é {} em letras maiúsculas.'.format(nome.upper()))
print('Seu nome é {} em letras minúsculas.'.format(nome.lower()))
print('Seu nome completo possui {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {}, e possui {} letras.'.format(separa[0].capitalize(), len(separa[0])))

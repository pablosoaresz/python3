#Faça um programa que leia uma frase pelo teclado e mostre:
#1- Quantas vezes aparece a letra "A".
#2- Em que posição ela aparece a primeira vez
#3- Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
print('Existem {} letras A na frase digitada.'.format(frase.count('A')))
print('A posição onde a letra A apareceu pela primeira vez foi na: {}.'.format(frase.find('A')+1))
print('A ultima posição onde a letra A apareceu foi: {}.'.format(frase.rfind('A')+1))

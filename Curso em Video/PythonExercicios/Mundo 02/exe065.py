__author__ = 'pablosoaresz'

# Crie um programa que leia varios numeros do teclado. No final da execução, mostre a média entre todos os valores e o
# maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maio = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Continua? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Foi digitado {} e a média foi {}.'.format(quant, media))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))

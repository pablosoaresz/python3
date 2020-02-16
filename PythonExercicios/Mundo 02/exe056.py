__author__ = 'pablosoaresz'

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo;
# Qual é o nome do homem mais velho;
# Quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_masc = 0
nome_velho = 0
total_mulher_20 = 0
for cont in range(1, 5):
    print('-------{}ª PESSOA-------'.format(cont))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo? [M/F]: ')).strip()
    soma_idade += idade
    if cont == 1 and sexo in 'Mm':
        maior_idade_masc = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_masc:
        maior_idade_masc = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1
media_idade = soma_idade / cont
print('A média de idade deste grupo é de {:.0f} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_masc, nome_velho))
print('Temos {} mulheres com menos de 20 anos.'.format(total_mulher_20))

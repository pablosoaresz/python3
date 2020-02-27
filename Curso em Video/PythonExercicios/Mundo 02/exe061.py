__author__ = 'pablosoaresz'

# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura WHILE.

print('Gerador de Progressão Aritmética!')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da Pa: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim!')

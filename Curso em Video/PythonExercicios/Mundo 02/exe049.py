__author__ = 'pablosoaresz'

# Refaça o exercicio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço 'for'.

n = int(input('Digite um número: '))
for c in range(1, 11):
    print('Taboada: {} x {} = {}'.format(n, c, n * c))

__author__ = 'pablosoaresz'

# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(1, 51, +1):
    print('.', end='')
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou!')

# Ou (abaixo possui menores interações.

for count in range(2, 51, 2):
    print('.', end='')
    print(count, end=' ')
print('Finished!')

'''cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
print('fim')

n = s = 0
while n != 999:
     n = int(input('Digite um número: '))
     if n == 999:
         break
     s += n
# print('A soma vale {}.'.format(s))
print(f'A soma vale {s}')
'''

nome = 'Pablo'
idade = 35
salario = 1000.1
print(f'O {nome} tem {idade} anos.') # Python 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # Python 3
print('O %s tem %d anos.'% (nome, idade)) # Python 2
print(f'O {nome} tem {idade} e recebe R${salario:.2f}')
print(f'{nome:20}.')
print(f'{nome:^20}.')
print(f'{nome:-^20}.')
print(f'{nome:->20}.')
print(f'{nome:-<20}.')

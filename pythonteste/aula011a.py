'''
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m
'''

print('\033[4;30;45m Olá, Mundo!\033[m')
print('\033[7;30m Olá, Mundo!\033[m')
print('\033[0;33;44m Olá, Mundo!\033[m')
print('\033[7;33;44m Olá, Mundo"\033[m')

a = 3
b = 5
print('Os valores são \033[33;45m{}\033[m e \033[30;45m{}\033[m!!!'.format(a, b))
nome = 'Pablo'
print('Olá! Muito prazer em te conhecer {}{}{}!'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('Olá! Muito prazer em te conhecer {}{}{}, agora usando "lista de cores em um dicionário"!'.format(cores['azul'], nome, cores['limpa']))
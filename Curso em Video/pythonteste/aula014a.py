'''while not apple:
    if chao:
        pega
    if buraco:
        pula
    if moeda:
        pega
pega
'''

'''for c in range(1, 10):
    print(c)
print('Fim')
'''
'''c = 1
while c < 10:
    print(c)
    c += 1
print("fim!")
'''
'''
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim!')
'''
'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim!')
'''

n = 1
par = impar = 0
c = 0
while n != 0:
    c += 1
    n = int(input('Digite o {}º valor: '.format(c)))
    if n != 0: #Para ignorar a verificação de par ou ímpar do número 0, visto que pode ser considerado um número nulo!
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares, e {} números ímpares!!!'.format(par, impar))

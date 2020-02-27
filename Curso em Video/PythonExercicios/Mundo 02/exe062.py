__author__ = 'pablosoaresz'

# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
# disser que quer mostrar 0 termos.

print('Gerador de Progressão Aritmética!')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da Pa: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

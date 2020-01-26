# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar; - Se é a hora de se alistar; - Se já passou do tempo do alistamento.
# Seu programa deverá mostrar o tempo que falta ou que passou do prazo.


import datetime
ano_nasci = int(input('Digite o seu ano de nascimento: '))
hoje_ano = datetime.datetime.now()
idade = hoje_ano.year - ano_nasci
idade_alist = 18

if idade_alist == hoje_ano.year - ano_nasci:
    print('Está na hora de alistar')
elif hoje_ano.year - ano_nasci <= idade_alist:
    print('Está quase na hora de se alistar. Faltando apenas {} anos.'.format(hoje_ano.year - ano_nasci - idade_alist))
elif hoje_ano.year - ano_nasci > idade_alist:
    print('Já passou da hora do alistamento. Passaram-se {} anos.'.format(hoje_ano.year - ano_nasci - idade_alist))

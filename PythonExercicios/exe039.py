__autor__= 'pablosoaresz'
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar; - Se é a hora de se alistar; - Se já passou do tempo do alistamento.
# Seu programa deverá mostrar o tempo que falta ou que passou do prazo.

'''
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
'''

from datetime import date
ano_atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = int(input('Digite =1= se você for homem e =2= para mulher: '))
idade = ano_atual - nasc
if sexo == 1:
    print('Hoje no ano de {}, quem nasceu em {}, terá {} anos de idade.'.format(ano_atual, nasc, idade))
    if idade == 18:
        print('Alistamento IMEDIATO!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = ano_atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você deveria ter se alistado há {} anos.'.format(saldo))
        ano = ano_atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
elif sexo == 2:
    print('Você não tem obrigação no serviço militar.')
else:
    print('Opção inválida.')

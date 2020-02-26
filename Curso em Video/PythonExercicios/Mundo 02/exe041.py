__autor__= 'pablosoaresz'
# A Confereção Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com sua idade:
# - Até 9 anos: MIRIM; - Até 14 anos: INFANTIL; - Até 19 anos: JUNIOR; - Até 20 anos: SÊNIOR; - Acima: MASTER

'''import datetime
ano_nascimento = int(input('Qual o ano de seu nascimento: '))
ano_hoje = datetime.datetime.now()
print(ano_hoje.year)
idade = ano_hoje.year - ano_nascimento
if idade <= 9:
    print('Você tem {} anos, sua categoria é MIRIM.'.format(idade))
elif idade >= 10 and idade <= 14:
    print('Você tem {} anos, sua categoria é INFANTIL.'.format(idade))
elif idade >= 15 and idade <= 19:
    print('Você tem {} anos, sua categoria é JUNIOR.'.format(idade))
elif idade == 20:
    print('Você tem {} anos, sua categoria é SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos, sua categoria é MASTER.'.format(idade))
'''

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação MIRIM.')
elif idade <= 14:
    print('Classificação INFANTIL.')
elif idade <= 19:
    print('Classificação JUNIOR.')
elif idade <= 25:
    print('Classificação SENIOR.')
else:
    print('Classificação MASTER.')

__autor__= 'pablosoaresz'
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from calendar import isleap
from datetime import date
ano = int(input('Digite um ano com 4 dígitos (Ex.:1999)? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('O ano digitado, {} é Bissexto.'.format(ano))
    print('O ano {} é Bissesto (usando library "calendar")'.format(ano, isleap(ano)))
else:
    print('O ano ditigado {} não é Bissexto.'.format(ano))
    print('O ano {} não é Bissesto (usando library "calendar")'.format(ano, isleap(ano)))

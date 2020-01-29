__autor__= 'pablosoaresz'
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# -À vista dinheiro/cheque: 10% de desconto;
# -À vista no cartão: 5% de desconto;
# -Em até 2x no cartão: preço normal;
# -3x ou mais no cartão: 20% de juros.
'''
price = float(input('Digite o preço do produto: R$'))
parcelas = int(input('Digite a quantidade de parcelas: '))
isCard = int(input('Pagamento via cartão? 1- Sim; 2- Não'))
vista = price - (price * 10 / 100)
vista_cartao = price  - (price * 5 / 100)
juros = (price / parcelas) * 20 / 100
final_price = price / parcelas + juros
print('{:=^40}'.format(' LOJAS NINHO '))
if parcelas == 1 and isCard == 2:
    print('10% de desconto, de R${:.2f}, pagará R${:.2f}.'.format(price, vista))
elif parcelas == 2 and isCard == 1:
    print('Produto parcelado e sem desconto, R${:.2f}.'.format(price))
elif parcelas >=3 and isCard == 1:
    print('Parcelamento em 3x ou mais, juros de 20% ao mês. Ficando de R${:.2f} em {}x de R${:.2f}'.format(price, parcelas, final_price))
'''
print('{:=^40}'.format(' LOJINHA DO PEBLO '))
valor = float(input('Digite o valor das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão débito/crédito
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
forma_pagto = int(input('Qual a forma de pagamento? '))

if forma_pagto == 1:
    total = valor - (valor * 10 /100)
elif forma_pagto == 2:
    total = valor - (valor * 5 /100)
elif forma_pagto == 3:
    total = valor
    parcela = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif forma_pagto == 4:
    total = valor + (valor * 20 / 100)
    totparcelas = int(input('Quantas parcelas: '))
    parcela = total / totparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparcelas, parcela))
else:
    total = 0
    print('Opção inválida de pagamento. Tente novamente.')
print('Sua compra deu R${:.2f} e irá custar R${:.2f} no final.'.format(valor, total))

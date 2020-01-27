__autor__= 'pablosoaresz'
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# -À vista dinheiro/cheque: 10% de desconto;
# -À vista no cartão: 5% de desconto;
# -Em até 2x no cartão: preço normal;
# -3x ou mais no cartão: 20% de juros.

price = float(input('Digite o preço do produto: R$'))
parcelas = int(input('Digite a quantidade de parcelas: '))
isCard = int(input('Pagamento via cartão? 1- Sim; 2- Não'))
vista = price - (price * 10 / 100)
vista_cartao = price - (price * 5 / 100)
juros = (price / parcelas) * 20 / 100
final_price = price / parcelas + juros
if parcelas == 1 and isCard == 2:
    print('10% de desconto, de R${:.2f}, pagará R${:.2f}.'.format(price, vista))
elif parcelas == 2 and isCard == 1:
    print('Produto parcelado e sem desconto, R${:.2f}.'.format(price))
elif parcelas >=3 and isCard == 1:
    print('Parcelamento em 3x ou mais, juros de 20% ao mês. Ficando de R${:.2f} em {}x de R${:.2f}'.format(price, parcelas, final_price))

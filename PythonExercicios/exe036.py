# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Valor do imóvel: R$'))
salario = float(input('Salário do comprador: R$'))
parcelas = int(input('x parcelas: '))
prestacao = valor / parcelas
margem = salario * 30 / 100
print('Mapa de cálculo: '
      '\nfinanciamento: R${:.2f}'
      '\nSalário: R${:.2f}'
      '\nParcelas: {}x'
      '\nMargem: R${:.2f}'
      '\nPrestação: R${:.2f}'.format(valor, salario, parcelas, margem, prestacao))
if prestacao > margem:
    print('Empréstimo negado! Sinto muito.')
else:
    print('Parabéns, empréstimo aprovado!')

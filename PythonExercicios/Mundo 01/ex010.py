__autor__= 'pablosoaresz'
valor_real = float(3.27)
n1 = float(input('Digite o valor a ser comprado: '))
print('Para comprar {} dólares, o custo será de {:.2f} Reais, com a cotação atual de {} Reais por Dólar'.format(n1, n1 * valor_real, valor_real))

real = float(input('Quanto dinhero você tem na carteira? R$'))
dolar = real / 3.27
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))

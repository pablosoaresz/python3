#Escreva um programa que pergunta a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.

km = float(input('Qual a KM rodada: '))
dia = int(input('Quantos dias ficou alugado: '))

total = (km * 0.15) + (dia * 60.00)
print('O total a ser pago será de R${:.2f}'.format(total))

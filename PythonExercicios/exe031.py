__autor__= 'pablosoaresz'
#Desenvolva um programa que pergunta a distancia de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.

dist = float(input('Digite a distância percorrida: '))
if dist > 200.00:
    print('O valor da passagem será de R${:.2f} para percorrer os {:.0f} Kms indicados.'.format(dist * 0.45, dist))
else:
    print('O valor da passagem será de R${:.2f} para percorrer os {:.0f} Kms indicados.'.format(dist * 0.50, dist))

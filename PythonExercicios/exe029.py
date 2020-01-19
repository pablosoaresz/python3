__autor__= 'pablosoaresz'
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada KM/h acima do limite.
velocidade = float(input('Digite a velocidade aferida: '))
if velocidade > 80.0:
    print('Você foi multado ao ultrapassar o limite de velocidade que é 80km/h. Sua velocidade aferida foi de: {:.2f}km/h,\n e sua multa será de R${:.2f} Reais.'
          .format(velocidade, ((velocidade - 80.00) * 7.00)))
else:
    print('Segue a vida...')

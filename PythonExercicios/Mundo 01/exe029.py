__autor__= 'pablosoaresz'
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada KM/h acima do limite.
velocidade = float(input('Digite a velocidade aferida: '))
if velocidade > 80:
    print('Você foi MULTADO ao ultrapassar o limite de velocidade de 80km/h. '
          '\nSua velocidade aferida foi de: {:.2f}km/h,e sua multa será de R${:.2f} Reais.'
          .format(velocidade, (velocidade - 80) * 7.00))
print('Tenha um bom dia! Dirija com segurança!')

#Escreva um programa que converta uma temperatura digitada em ºC ára ºF
c = float(input('Digite a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {:.2f}ºC será {:.2f}ºF.'.format(c, f))

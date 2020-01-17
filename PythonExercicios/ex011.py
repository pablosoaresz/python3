#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
lado1 = float(input('Digite o valor do lado 1: '))
lado2 = float(input('Digite o valor do lado 2: '))
area = lado1 * lado2
print('A área é de {} m², sendo necessário {:.2f} litros de tinta para pintar.'.format(area,area/2))

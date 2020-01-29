__autor__= 'pablosoaresz'
# Refaça o DESAFIO 035 dos triângulos, acrescentando o rescurso de mostrar que tipo de triângulo será formado:
# -Equilátero: todos os lados iguais; -Isósceles: dois lados iguais; -Escaleno: todos os lados diferentes.

'''r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos apresentados FORMAM um triângulo.')
else:
    print('Os segmentos apresentados NÃO formam um triangulo.')
'''

reta1 = float(input('Digite o tamanho da 1ª reta: '))
reta2 = float(input('Digite o tamanho da 2ª reta: '))
reta3 = float(input('Digite o tamanho da 3ª reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Estas retas FORMAM um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO!')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')
    else:
        print('ISÓSCELES!')
else:
    print('NÃO formam triângulo.')

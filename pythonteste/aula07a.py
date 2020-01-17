n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 #divisão inteiro
expo = n1 ** n2
print('A soma é {}, a subtração é {}, o produto é {},\n a divisão é {:.2f}, \n a divisão inteira é {}'.format(s, sub, m, d, di), end =' \n >>> ')
print('A exponenciação é {}'.format(expo))


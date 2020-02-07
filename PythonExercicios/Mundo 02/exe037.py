__autor__= 'pablosoaresz'
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual sera a base de conversão:
# -1 para binário; 2- para octal; 3- para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha para qual base deverá ser a conversão:
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL''')
option = int(input('Digite a opção: '))
if option == 1:
    print('O número {} convertido para BINÁRIO é: {}.'.format(num, bin(num)[2:]))
elif option == 2:
    print('O número {} convertido para OCTAL é: {}.'.format(num, oct(num)[2:]))
elif option == 3:
    print('O número {} convertido para HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')

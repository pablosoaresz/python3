# tempo = int(input('Quantos anos tem o seu carro? '))
# if tempo <= 3:
#     print('Carro novo')
# else:
#     print('Carro velho')
# Ou
# print('Carro novo' if tempo <= 3 else'Carro Velho')
# print('---FIM---')

# nome = str(input('Qual é seu nome? '))
# if nome == 'Pablo':
#     print('Que nome lindo você tem!')
# else:
#     print('{}, seu nome é tão normal.'.format(nome))
# print('Bom dia, {}.'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais!')
#Ou
print('APROVADO' if m >= 6.0 else 'REPROVADO')

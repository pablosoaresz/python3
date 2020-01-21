__autor__= 'pablosoaresz'
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00 calcule um aumento de 10%.
#Para inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário para saber qual o aumento. R$ '))
if salario > 1250:
    print('Seu aumento será de 10%, sendo R${:.2f} o novo valor.'.format(salario + (salario * 0.10)))
else:
    print('Seu aumento será de 15%, sendo R${:.2f} o novo valor.'.format(salario + (salario * 0.15)))

# Ou
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('R${:.2f}'.format(novo))

__autor__= 'pablosoaresz'
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario = float(input("Digite o valor do salário atual: R$"))
novo = salario + (salario * 15 / 100)
print("O seu salário atual é de R${:.2f} Reais e com aumento de 15% seu novo salário será de R${:.2f} Reais.".format(salario, novo))

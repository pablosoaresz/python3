__author__ = 'pablosoaresz'

# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
menu = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while menu != 5:
    menu = int(input('Digite a opção desejada:\n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa \nOpção: '))
    if menu == 1:
            soma = n1 + n2
            print('O resultado de {} + {} é {}.'.format(n1, n2,soma))
    elif menu == 2:
            produto = n1 * n2
            print('O resultado de {} x {} é {}.'.format(n1, n2, produto))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
        print('Entre {} e {}, o maior é {}.'.format(n1, n2, maior))
    elif menu == 4:
            print('Insira novamente os valores!')
            n1 = int(input('Digite o primeiro valor: '))
            n2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente Novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa!')

__autor__= 'pablosoaresz'
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensage no final, de acordo com a média
# atindiga: - Média abaixo de 5.0: REPROVADO; - Média entre 5.0 e 6.9: RECUPERAÇÃO; - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('REPROVADO com a média {:.1f}.'.format(media))
elif 5 <= media < 7:# é o mesmo que: media >= 5.0 and media < 7
    print('RECUPERAÇÃO com a média {:.1f}.'.format(media))
elif media >= 7:
    print('APROVADO com a média {:.1f}.'.format(media))

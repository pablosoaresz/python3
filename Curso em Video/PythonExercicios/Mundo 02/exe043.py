__autor__ = 'pablosoaresz'
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo: -Abaixo de 18.5: Abaixo do peso; -Entre 18.5 e 25: Peso ideal; 25 até 30: Sobrepeso;
# -Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso atual em KG: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Seu IMC é {:.1f}. Você está abaixo do peso!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f}. Você está no peso ideal!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f}. Você está com sobrepeso!'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f}. Você está com obesidade nível 1!'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.1f}. Você possui obesidade móbida!!!'.format(imc))

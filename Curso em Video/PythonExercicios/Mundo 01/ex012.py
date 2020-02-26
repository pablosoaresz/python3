__autor__= 'pablosoaresz'
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

price = float(input("Qual o valor do produto? R$ "))
off = float(input("Qual o desconto em %? "))
final_price = price - (price * off / 100)
print("O valor do produto que era R${:.2f}, agora com {}% de desconto será: R${:.2f}.".format(price, off, final_price))

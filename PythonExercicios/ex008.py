medida = float(input('Digite a distância em metros: '))

#Decímetros
dm = medida * 10

#Centímetros
cm = medida * 100

#Milímetros
mm = medida * 1000

#Decâmetros
dam = medida / 10

#Hectômetro
hm = medida / 100

#Kilômetro
km = medida / 1000

print('A distância digitada é {} metro(s), sendo {:.0f} decimetro(s), {:.0f} centimetro(s), {:.0f} milímetro(s) , e {} decâmetro(s) , {} hectômetro(s) e  {} kilômetro(s).'.format(medida, dm, cm, mm, dam, hm, km))

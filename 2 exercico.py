a = float(input('calcule o valor do salario:').replace(',','.'))
b = float(input('calcule o valor do aumento:').replace(',','.'))

c = a * (b/100)
d = a+c

print('o valor do salario vai ser de r$%.2f'%d)
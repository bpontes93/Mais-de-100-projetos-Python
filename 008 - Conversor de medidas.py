# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite a medida em metros: '))
c = m * 100
mm = m * 1000

print('\nSuas medidas respectivas são:\nMetros = {}\nCentímetros = {}\nMilímetros = {}'.format(m, c, mm))
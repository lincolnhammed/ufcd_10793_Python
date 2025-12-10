# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 
# Formula:((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0)


ano = int(input("Escolha um ano e veja se é bissexto"))

if((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
    print("é bixesto")
else:
    print("Não é bissexto")
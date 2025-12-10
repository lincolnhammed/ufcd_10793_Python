#Desenvolva um programa que leia o comprimento de três
#  retas e diga ao utilizador se elas podem ou não formar 
# um triângulo. (Soma de 2 lados tem que ser maior do 3)

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    print("Os lados podem formar um triângulo.")
else:
    print("Os lados não podem formar um triângulo.")    
 
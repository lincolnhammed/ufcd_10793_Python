# Programa que verifica se três lados podem formar um triângulo
# e indica qual o tipo (Equilátero, Isósceles ou Escaleno).

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Primeiro verifica se as medidas formam um triângulo
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    print("Os lados podem formar um triângulo.")

    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("Tipo: EQUILÁTERO (todos os lados iguais).")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Tipo: ISÓSCELES (dois lados iguais).")
    else:
        print("Tipo: ESCALENO (todos os lados diferentes).")

else:
    print("Os lados não podem formar um triângulo.")

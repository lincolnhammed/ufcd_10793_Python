#Faça um programa que leia a largura e a altura de uma 
# parede em metros, calcule a sua área e a quantidade de
#  tinta necessária para pintá-la, sabendo que cada litro 
# de tinta pinta uma área de 2 metros quadrados.

# Solicita ao usuário que digite a largura e a altura da parede
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))  

# Calcula a área da parede
area = largura * altura

# Calcula a quantidade de tinta necessária (1 litro para cada 2 metros quadrados)
tinta_necessaria = area / 2

# Exibe o resultado
print(f"A área da parede é {area} metros quadrados.")
print(f"A quantidade de tinta necessária para pintá-la é {tinta_necessaria} litros.") 

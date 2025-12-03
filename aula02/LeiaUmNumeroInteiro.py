# Faça um programa que leia um número Inteiro e exiba 
# no ecrã o seu sucessor e o seu predecessor.

# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Calcula o sucessor e o predecessor
sucessor = numero + 1
predecessor = numero - 1

# Exibe o resultado
print(f"O sucessor de {numero} é {sucessor}")
print(f"O predecessor de {numero} é {predecessor}")
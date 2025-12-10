# Faça um programa que calcule a soma entre todos os números que são 
# múltiplos de três e que se encontram no intervalo de 1 até 20.
soma = 0
for numero in range(1, 21):
    if numero % 3 == 0:
        soma += numero
print(f"A soma dos múltiplos de 3 entre 1 e 20 é: {soma}")
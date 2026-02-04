# Crie um programa onde o utilizador possa digitar 
# vários valores numéricos e colocá-los numa lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []
cont = 1

print("Digite números. Se o número for repetido, não será inserido.")

while True:
    num = int(input(f"Digite o {cont}º número: "))

    if num not in numeros:
        numeros.append(num)
        cont += 1
    else:
        print("Número repetido, não será inserido.")

    cond = input("Deseja sair? (Y) Sim | (N) Não: ").upper()

    if cond == 'Y':
        break

for i in range(len(numeros)):
    # Loop interno: percorre cada par
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Troca de posição
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Números ordenados:", numeros) 

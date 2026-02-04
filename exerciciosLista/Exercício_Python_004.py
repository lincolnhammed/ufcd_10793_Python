"""
Docstring for exerciciosLista.Exercício_Python_004

Crie um programa onde o utilizador possa digitar vários valores numéricos e
colocá-los numa lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista = []

while True:
    num = int(input("Digite um número (0 para parar): "))
    if num == 0:
        break

    existe = 0
    for i in range(len(lista)):  
        if lista[i] == num:       
            existe = 1

    if existe == 0:
        lista.append(num)

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp

print("Números únicos digitados em ordem crescente:", lista)



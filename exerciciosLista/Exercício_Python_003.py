"""
Docstring for exerciciosLista.Exercício_Python_003

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No
final, mostre qual foi o maior e o menor valor digitado e as suas respetivas
posições na lista.
"""

import random


vetor = []
print("Escreva um numero no vetor\n")
for i in range(5):

    num = (int(input(f"vetor[{i}]")))
    vetor.append(num)

maior= vetor[0]
menor= vetor[0]
posMa= 0
posMe= 0
for i in range(len(vetor)):
    if (maior<vetor[i]):
        maior=vetor[i]
        posMa = i
    if (menor>vetor[i]):
        menor=vetor[i]
        posMe = i

print(f"\nnumero maior e menor\n")
print(f"vetor[{posMa}] - maior {maior}")
print(f"vetor[{posMe}] - menor {menor}")
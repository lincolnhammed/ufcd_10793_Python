"""
Crie um programa que vai gerar cinco números aleatórios e colocar numa lista.
Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na lista.
"""


import random


vetor = []
for i in range(5):

    num = random.randint(1, 10)
    vetor.append(num)

maior= vetor[0]
menor= vetor[0]
posMa=0
posMe=0
for i in range(len(vetor)):
    print(f"vetor[{i}] - {vetor[i]}")
    if (maior<=vetor[i]):
        maior=vetor[i]
        posMa = i
    if (menor>=vetor[i]):
        menor=vetor[i]
        posMe = i

print(f"\nnumero maior e menor\n")
print(f"vetor[{posMa}] - maior {maior}")
print(f"vetor[{posMe}] - menor {menor}")
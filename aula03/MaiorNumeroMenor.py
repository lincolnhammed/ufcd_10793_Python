#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num = [0] * 3

for i in range(3):
    num[i] = int(input(f"Digite o {i+1}° número: "))

maior = num [0]
menor= num[0]

for i in range(3):
    if(num[i] >maior ):
        maior =num[i]
    if(num[i] < menor ):
       menor = num[i]

print(f"maior numero é{maior}")
print(f"menor numero é{menor}")
    